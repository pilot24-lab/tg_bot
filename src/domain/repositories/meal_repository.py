from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.meal import Meal

class MealRepository(ABC):
    @abstractmethod
    async def create(self, meal: Meal) -> Meal:
        pass

    @abstractmethod
    async def get_by_id(self, meal_id: int) -> Optional[Meal]:
        pass

    @abstractmethod
    async def get_by_user_id(self, user_id: int, limit: int = 10, offset: int = 0) -> List[Meal]:
        pass

    @abstractmethod
    async def update(self, meal: Meal) -> Optional[Meal]:
        pass

    @abstractmethod
    async def delete(self, meal_id: int) -> bool:
        pass