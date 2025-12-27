import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    print("Bot starting...")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def start_handler(message: Message):
        await message.answer("✅ Bot Railway’da ishlayapti!")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
