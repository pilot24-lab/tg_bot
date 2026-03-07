from typing import List, Optional

from src.domain.entities.meal import Meal
from src.domain.repositories.meal_repository import MealRepository
from src.infrastructure.database.connection import DatabaseConnection

class SQLiteMealRepository(MealRepository):
    def __init__(self, db: DatabaseConnection):
        self.db = db

    async def create(self, meal: Meal) -> Meal:
        return await super().create(meal)
    
    async def get_by_id(self, meal_id: int) -> Optional[Meal]:
        return await super().get_by_id(meal_id)
    
    async def get_all_by_user_id(self, user_id: int, limit = 10, offset = 0) -> List[Meal]:
        return await super().get_all_by_user_id(user_id, limit, offset)
    
    async def update(self, meal: Meal) -> Optional[Meal]:
        return await super().update(meal)
    
    async def delete(self, meal_id: int) -> bool:
        return await super().delete(meal_id)