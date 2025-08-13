from aiogram import Dispatcher, F
from aiogram.filters import Command
from handler import start_handler, ortga_handler, send_books, book_info, send_more_books

dp = Dispatcher()


dp.message.register(start_handler, Command("start"))
dp.message.register(ortga_handler, F.text == "🔙 Ortga")
dp.message.register(send_books, F.text == "📖 Kitoblar")
dp.message.register(book_info, F.text.startswith("📚"))
dp.message.register(send_more_books, F.text == "🔎 Yana")