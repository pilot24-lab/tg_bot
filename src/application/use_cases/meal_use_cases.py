from typing import List, Optional

from src.domain.entities.meal import Meal
from src.domain.exceptions import EntityAlreadyExists, EntityNotFound, ValidationError
from src.domain.repositories.meal_repository import MealRepository
from src.domain.repositories.user_repository import UserRepository

class CreateMealUseCase:
    def __init__(self, meal_repository: MealRepository, user_repository: UserRepository):
        self.meal_repository = meal_repository
        self.user_repository = user_repository

    async def execute(self, user_id: int, food_name: str) -> Meal:
        if not food_name or not user_id:
            raise ValidationError(f"User or Food_name are required")
        existing_user = await self.user_repository.get_by_id(user_id)
        if not existing_user:
            raise EntityNotFound(f"User with id{user_id} not found")
        meal = Meal(id=None, user_id=user_id, food_name=food_name)
        return await self.meal_repository.create(Meal)
        

class GetMealUseCase:
    def __init__(self, meal_repository: MealRepository):
        self.meal_repository = meal_repository

    async def execute(self, meal_id: int) -> Meal:
        meal = await self.meal_repository.get_by_id(meal_id)
        if not meal:
            raise EntityNotFound(f"Meal with id {meal_id} not found")
        return meal
        

class GetAllMealsByUserIdUseCase:
    def __init__(self, meal_repository: MealRepository, user_repository: UserRepository):
        self.meal_repository = meal_repository
        self.user_repository = user_repository

    async def execute(self, user_id: int, limit: int = 100, offset: int = 0 ) -> List[Meal]:
        existing_user = await self.user_repository.get_by_id(user_id)
        if not existing_user:
            raise EntityNotFound(f"User with id{user_id} not found")
        return await self.meal_repository.get_all_by_user_id(user_id=user_id, limit=limit, offset=offset)
    

class UpdateMealUseCase:
    def __init__(self, meal_repository: MealRepository, user_repository: UserRepository):
       self.meal_repository = meal_repository
       self.user_repository = user_repository

    async def execute(self, user_id: int, meal_id: int, food_name: str) -> Meal:
        existing_user = await self.user_repository.get_by_id(user_id)
        existing_meal = await self.meal_repository.get_by_id(meal_id)
        if not existing_meal or not existing_user:
            raise EntityNotFound(f"Meal or User is not found")
        if user_id != existing_meal.user_id:
            raise EntityNotFound(f"User with id {user_id} is not the owner of Meal {meal_id}")
        
        if food_name:
            existing_meal.food_name = food_name
        
        updated_meal = await self.meal_repository.update(existing_meal)
        
        if not updated_meal:
            raise EntityNotFound(f"Meal with {meal_id} not found")
        return updated_meal


class DeleteMealUseCase:
    def __init__(self, meal_repository: MealRepository):
        self.meal_repository = meal_repository

    async def execute(self, meal_id: int) -> bool:
        result = await self.meal_repository.delete(meal_id)
        if not result:
            raise EntityNotFound(f"Meal with id {meal_id} not found")
        return result
        