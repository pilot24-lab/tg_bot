from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from typing import List

from src.application.use_cases.user_use_cases import (
    CreateUserUseCase,
)
from src.infrastructure.database.connection import db_connection
from src.infrastructure.repossitories.sql_user_repositiry import SQLiteUserRepository


user_router = Router()

@user_router.message(CommandStart())
async def cmd_start(message: Message):
    SQl = SQLiteUserRepository(db_connection)
    use_case = CreateUserUseCase(SQl)
    await message.reply(f"Hi user {message.from_user.full_name}")
    try:
        user = await use_case.execute(tg_id=int(message.from_user.id), name=message.from_user.full_name)
    except:
        print('Error')
