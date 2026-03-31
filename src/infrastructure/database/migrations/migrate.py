import asyncio
from pathlib import Path

from infrastructure.database.connection import DatabaseConnection


MIGRATIONS_DIR = Path(__file__).parent / "migrations"


async def migrate(db: DatabaseConnection):

    conn = await db.connect()

    # таблица для отслеживания миграций
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS migrations (
            name TEXT PRIMARY KEY
        )
    """)
    await conn.commit()

    cursor = await conn.execute("SELECT name FROM migrations")
    applied = {row[0] for row in await cursor.fetchall()}

    migration_files = sorted(MIGRATIONS_DIR.glob("*.sql"))

    for file in migration_files:

        if file.name in applied:
            continue

        print(f"Applying migration: {file.name}")

        sql = file.read_text()

        await conn.executescript(sql)

        await conn.execute(
            "INSERT INTO migrations (name) VALUES (?)",
            (file.name,)
        )

        await conn.commit()

    print("Migrations applied")
    await conn.close()