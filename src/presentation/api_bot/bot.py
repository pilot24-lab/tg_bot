from aiogram import Bot, Dispatcher
from bot_token.bot_token import BOT_TOKEN
from presentation.api_bot.handlers.user_hanlers import user_router


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(user_router)

async def bot_main():    
    await dp.start_polling(bot)

































