from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📖 Kitoblar")]
    ], 
    resize_keyboard=True,
    one_time_keyboard=True 
)

