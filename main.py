from src.presentation.api_bot.bot import bot_main
import asyncio
import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename='tg_logs.log', filemode='w', format="%(asctime)s %(levelname)s %(message)s")
    try:        
        asyncio.run(bot_main())        
    except KeyboardInterrupt:
        print('Exit')
