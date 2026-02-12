from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> User:
        pass

    @abstractmethod
    async def get_by_tg_id(self, tf_id: int) -> User:
        pass

    @abstractmethod
    async def get_by_id(self, user_id: int) -> User:
        pass
    
    @abstractmethod
    async def update(self, user: User) -> User:
        pass
    
    @abstractmethod
    async def delete(self, user_id: int) -> bool:
        pass
    