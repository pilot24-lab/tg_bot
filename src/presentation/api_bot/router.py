from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from src.presentation.api_bot.handlers.hanlers import router as bot_router 

router = Router()

router.include_router(bot_router)