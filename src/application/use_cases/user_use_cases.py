from typing import List, Optional

from src.domain.entities.user import User
from src.domain.exceptions import EntityAlreadyExists, EntityNotFound, ValidationError
from src.domain.repositories.user_repository import UserRepository

class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
      self.user_repository = user_repository

    async def execute(self, tg_id: int, name: str) -> User:
       if not tg_id or not name:
          raise ValidationError('TG_id or name are required')
       existing_user = await self.user_repository.get_by_tg_id(tg_id)
       if not existing_user:
          user = User(id=None, tg_id=tg_id, name=name)
          return await self.user_repository.create(user)
       

class GetUserUseCase:
    def __init__(self, user_repository: UserRepository):
       self.user_repository = user_repository
    
    async def execute(self, user_id: int) -> User:
        user = await self.user_repository.get_by_id(user_id)
        if not user:
            raise EntityNotFound(f"User with {user_id} not found")
        return user
    

