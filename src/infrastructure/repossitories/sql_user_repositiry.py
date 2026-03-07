from typing import List, Optional

from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository
from src.infrastructure.database.connection import DatabaseConnection

class SQLiteUserRepository(UserRepository):
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def _map_row_to_user(self, row) -> User:
        if not row:
            return None
        return User(
            id=row['id'],
            tg_id=row['tg_id'],
            name=row['name'],
            created_at=row['created_at'],
            updated_at=row['updated_at']
        )
    
    async def create(self, user: User) -> User:
        row = await self.db.fetchone(
            """
            insert into users(tg_id, name)
            values($1, $2)
            returning id, tg_id, name, created_at, updated_at
            """,
            user.tg_id, user.name
        )
        return self._map_row_to_user(row)
    
    async def get_by_tg_id(self, tg_id: int) -> Optional[User]:
        row = await self.db.fetchone(
            """
            select id, tg_id, name, created_at, updated_at
            from users
            where tg_id = $1
            """,
            tg_id
        )
        return self._map_row_to_user(row)

    async def get_by_id(self, user_id: int) -> Optional[User]:
        row = await self.db.fetchone(
            """
            select id, tg_id, name, created_at, updated_at
            from users
            where id = $1
            """,
            user_id
        )
        return self._map_row_to_user(row)
    
    async def get_all(self, limit = 100, offset = 0) -> List[User]:
        rows = await self.db.fetchall(
            """
            select
            select id, tg_id, name, created_at, updated_at
            from users
            limit $1 offset $2
            """,
            limit, offset
        )
        return [self._map_row_to_user(row) for row in rows]
    
    async def update(self, user: User) -> Optional[User]:
        row = self.db.fetchone(
            """
            update users
            set name = $1, updated_at = current_timestamp
            where id = $2
             returning id, email, name, created_at, updated_at
            """,
            user.name, user.id
        )
        return self._map_row_to_user(row)
    
    async def delete(self, user_id: int) -> bool:
        result = self.db.execute(
            """
            delete from users
            where id = $1
            """,
            user_id
        )
        return result == "DELETE 1"