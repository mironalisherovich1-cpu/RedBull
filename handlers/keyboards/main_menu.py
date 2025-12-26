from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👤 Мой профиль")],
            [
                KeyboardButton(text="🛍 Витрина"),
                KeyboardButton(text="⭐️ Отзывы")
            ],
            [
                KeyboardButton(text="🆘 Помощь"),
                KeyboardButton(text="🚬 Курилка")
            ],
            [
                KeyboardButton(text="📢 Канал"),
                KeyboardButton(text="🤖 Персональный бот")
            ],
            [KeyboardButton(text="💼 Работа")]
        ],
        resize_keyboard=True
    )
