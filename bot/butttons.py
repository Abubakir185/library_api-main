from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Kitoblar")],
        [KeyboardButton(text="🔎 Janrlar")], 
    ], 
    resize_keyboard=True,
    one_time_keyboard=True 
)


# orqaga = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="🔙 Ortga")],
#     ],
#     resize_keyboard=True,
#     one_time_keyboard=True
# )

