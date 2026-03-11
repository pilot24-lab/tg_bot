from aiogram import Router
from presentation.api_bot.handlers.user_hanlers import router as bot_router 

router = Router()

router.include_router(bot_router)