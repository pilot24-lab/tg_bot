import aiosqlite
from pathlib import Path
from typing import List, Optional


class DatabaseConnection:
    def __init__(self, db_path: str | Path):
        self.db_path = str(db_path)
        self.pool: aiosqlite.Connection | None = None

    async def connect(self):
        if self.pool is None:
            self.pool = await aiosqlite.connect(self.db_path)
            await self.pool.execute("PRAGMA foreign_keys = ON")

        return self.pool

    async def disconnect(self):
        if self.pool:
            await self.pool.close()
            self.pool = None

    async def execute(self, query: str, params: tuple = ()):
        conn = await self.connect()
        cursor = await conn.execute(query, params)
        await conn.commit()
        return cursor

    async def fetchone(self, query: str, *args):
        conn = await self.connect()
        cursor = await conn.execute(query, *args)
        return await cursor.fetchone()

    async def fetchall(self, query: str, *args):
        conn = await self.connect()
        cursor = await conn.execute(query, *args)
        return await cursor.fetchall()

db_path = Path(__file__).parent / 'db.sqlite3'
db_connection = DatabaseConnection(str(db_path))