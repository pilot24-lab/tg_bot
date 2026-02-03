from src.presentation.api_bot.bot import bot_main
import asyncio
import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:        
        asyncio.run(bot_main())        
    except KeyboardInterrupt:
        print('Exit')
