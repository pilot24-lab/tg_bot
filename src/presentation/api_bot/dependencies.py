from src.application.use_cases.user_use_cases import (
    CreateUserUseCase,
    GetUserUseCase,
    GetAllUsersUseCase,
    UpdateUserUseCase,
    DeleteUserUseCase
)

from src.application.use_cases.meal_use_cases import(
    CreateMealUseCase,
    GetMealUseCase,
    GetAllMealsByUserIdUseCase,
    UpdateMealUseCase, 
    DeleteMealUseCase
)

from src.infrastructure.database.connection import db_connection
from src.infrastructure.repossitories.sql_user_repositiry import SQLiteUserRepository
from src.infrastructure.repossitories.sql_meal_repository import SQLiteMealRepository



def get_user_repository():
    return SQLiteUserRepository(db_connection)

def get_create_user_use_case():
    return CreateUserUseCase(get_user_repository())

def get_get_user_use_case():
    return GetUserUseCase(get_user_repository())

def get_get_all_users_use_case():
    return GetAllUsersUseCase(get_user_repository())

def get_update_user_use_case():
    return UpdateUserUseCase(get_user_repository())

def get_delete_user_use_case():
    return DeleteUserUseCase(get_user_repository())

def get_meal_repository():
    return SQLiteMealRepository(db_connection)

def get_create_meal_use_case():
    return CreateMealUseCase(get_meal_repository)

def get_get_meal_use_case():
    return GetMealUseCase(get_meal_repository)

def get_get_all_meals_by_id_use_case():
    return GetAllMealsByUserIdUseCase(get_meal_repository)

def get_update_meal_use_case():
    return UpdateMealUseCase(get_meal_repository)

def get_delete_meal_use_case():
    return DeleteMealUseCase(get_meal_repository)