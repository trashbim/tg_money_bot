from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def create_category_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Продукты")],
            [KeyboardButton(text="Развлечения")],
            [KeyboardButton(text="Транспорт")],
            [KeyboardButton(text="Одежда")],
            [KeyboardButton(text="Техничка")],
            [KeyboardButton(text="Техника")],
            [KeyboardButton(text="Вело")],
            [KeyboardButton(text="Мото")],
            [KeyboardButton(text="Другие")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return markup
