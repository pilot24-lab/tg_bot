from aiogram import Bot, Dispatcher
from bot_token.bot_token import BOT_TOKEN, PROXY_URL
from src.presentation.api_bot.handlers.user_hanlers import user_router
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.default import DefaultBotProperties
session = AiohttpSession(proxy=PROXY_URL)


bot = Bot(token=BOT_TOKEN, session=session,
    default=DefaultBotProperties() )
dp = Dispatcher()
dp.include_router(user_router)

async def bot_main():  
    
    await dp.start_polling(bot)
    

































