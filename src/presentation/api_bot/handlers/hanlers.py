from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

router = Router()

@router.message(CommandStart)
async def cmd_start(message: Message):
    await message.reply(f"Hi user {message.from_user.id}")