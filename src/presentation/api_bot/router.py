from aiogram import Router
from src.presentation.api_bot.handlers.hanlers import router as bot_router 

router = Router()

router.include_router(bot_router)