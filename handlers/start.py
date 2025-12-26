from aiogram import Router, types
from aiogram.filters import CommandStart

from config import START_IMAGE_URL, START_BALANCE, DEFAULT_LANG, DEFAULT_CITY
from database.models import get_user, create_user
from keyboards.main_menu import main_menu_kb

router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    user = await get_user(message.from_user.id)

    if not user:
        await create_user(
            user_id=message.from_user.id,
            username=message.from_user.username,
            language=DEFAULT_LANG,
            city=DEFAULT_CITY,
            balance=START_BALANCE
        )

    text = (
        "🌈 Широкий выбор товаров.\n"
        "🔄 Простой процесс покупки.\n"
        "🛡 Гарантированное качество."
    )

    await message.answer_photo(
        photo=START_IMAGE_URL,
        caption=text,
        reply_markup=main_menu_kb()
    )
