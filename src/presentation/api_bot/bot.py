from aiogram import Bot, Dispatcher
from src.presentation.api_bot.bot_token import BOT_TOKEN
from src.presentation.api_bot.router import router
import asyncio



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)

async def bot_main():    
        await dp.start_polling(bot)
        
    