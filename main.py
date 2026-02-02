import asyncio
import logging
from src.presentation.api_bot.bot import bot_main

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(bot_main())
    except KeyboardInterrupt:
        print('Exit')
