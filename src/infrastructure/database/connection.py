import aiosqlite
from pathlib import Path


class Database:
    def __init__(self, db_path: str | Path):
        self.db_path = str(db_path)
        self._connection: aiosqlite.Connection | None = None

    async def connect(self):
        if self._connection is None:
            self._connection = await aiosqlite.connect(self.db_path)
            await self._connection.execute("PRAGMA foreign_keys = ON")

        return self._connection

    async def close(self):
        if self._connection:
            await self._connection.close()
            self._connection = None

    async def execute(self, query: str, params: tuple = ()):
        conn = await self.connect()
        cursor = await conn.execute(query, params)
        await conn.commit()
        return cursor

    async def fetchone(self, query: str, params: tuple = ()):
        conn = await self.connect()
        cursor = await conn.execute(query, params)
        return await cursor.fetchone()

    async def fetchall(self, query: str, params: tuple = ()):
        conn = await self.connect()
        cursor = await conn.execute(query, params)
        return await cursor.fetchall()