"""
Safe, Read-Only PostgreSQL to MongoDB Migration Script.

This script reads existing records from PostgreSQL (Users, Documents, ScreeningResults)
and imports them into MongoDB without modifying or deleting any PostgreSQL records.

Usage (Dry-Run / Safe Mode by default):
    python scripts/migrate_pg_to_mongo.py --pg-url "postgresql://postgres:password@localhost:5432/screening_db" --dry-run

Usage (Perform actual migration):
    python scripts/migrate_pg_to_mongo.py --pg-url "postgresql://postgres:password@localhost:5432/screening_db" --execute
"""

import argparse
import asyncio
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("migration")


async def migrate(pg_url: str, mongo_url: str, db_name: str, dry_run: bool = True):
    logger.info("=== PostgreSQL to MongoDB Safe Migration ===")
    logger.info(f"Source (PostgreSQL): {pg_url}")
    logger.info(f"Target (MongoDB): {mongo_url} / {db_name}")
    logger.info(f"Mode: {'DRY RUN (no changes written)' if dry_run else 'EXECUTE (writing to MongoDB)'}")

    try:
        import psycopg2
        import psycopg2.extras
    except ImportError:
        logger.error("psycopg2 is required to read from PostgreSQL: pip install psycopg2-binary")
        return

    try:
        from pymongo import AsyncMongoClient
    except ImportError:
        logger.error("pymongo is required: pip install pymongo>=4.9.0")
        return

    # Read records from PostgreSQL
    try:
        conn = psycopg2.connect(pg_url)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    except Exception as e:
        logger.error(f"Failed to connect to PostgreSQL: {e}")
        return

    # 1. Users
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    logger.info(f"Found {len(users)} users in PostgreSQL.")

    # 2. Documents
    cur.execute("SELECT * FROM documents;")
    documents = cur.fetchall()
    logger.info(f"Found {len(documents)} documents in PostgreSQL.")

    # 3. Screening Results
    cur.execute("SELECT * FROM screening_results;")
    screenings = cur.fetchall()
    logger.info(f"Found {len(screenings)} screening results in PostgreSQL.")

    cur.close()
    conn.close()

    if dry_run:
        logger.info("Dry run complete. No records were written to MongoDB.")
        logger.info("To write to MongoDB, re-run with --execute.")
        return

    # Write to MongoDB
    client = AsyncMongoClient(mongo_url)
    db = client[db_name]

    # Insert Users
    if users:
        for u in users:
            u_dict = dict(u)
            u_dict["_id"] = str(u_dict.pop("id"))
            await db["users"].update_one({"_id": u_dict["_id"]}, {"$set": u_dict}, upsert=True)
        logger.info(f"Successfully synced {len(users)} users to MongoDB.")

    # Insert Documents
    if documents:
        for d in documents:
            d_dict = dict(d)
            d_dict["_id"] = str(d_dict.pop("id"))
            await db["documents"].update_one({"_id": d_dict["_id"]}, {"$set": d_dict}, upsert=True)
        logger.info(f"Successfully synced {len(documents)} documents to MongoDB.")

    # Insert Screening Results
    if screenings:
        for s in screenings:
            s_dict = dict(s)
            s_dict["_id"] = str(s_dict.pop("id"))
            await db["screening_results"].update_one({"_id": s_dict["_id"]}, {"$set": s_dict}, upsert=True)
        logger.info(f"Successfully synced {len(screenings)} screening results to MongoDB.")

    await client.close()
    logger.info("Migration finished safely without altering any PostgreSQL data.")


def main():
    parser = argparse.ArgumentParser(description="Safely migrate PostgreSQL data to MongoDB.")
    parser.add_argument("--pg-url", default="postgresql://postgres:password@localhost:5432/screening_db", help="PostgreSQL connection URL")
    parser.add_argument("--mongo-url", default="mongodb://localhost:27017", help="MongoDB connection URL")
    parser.add_argument("--db-name", default="screening_db", help="MongoDB database name")
    parser.add_argument("--execute", action="store_true", help="Perform the migration (defaults to dry-run)")
    args = parser.parse_args()

    asyncio.run(migrate(args.pg_url, args.mongo_url, args.db_name, dry_run=not args.execute))


if __name__ == "__main__":
    main()
