import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import TOKEN
from handlers import register_handlers
from aiogram.fsm.storage.memory import MemoryStorage

async def main() -> None:
    # Initialize Bot instance
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    # Initialize Dispatcher with in-memory storage
    dp = Dispatcher(storage=MemoryStorage())
    
    # Register all handlers
    register_handlers(dp)

    # Start polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
