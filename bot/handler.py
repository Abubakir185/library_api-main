from aiogram.types import Message
from butttons import main_menu
import aiohttp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_URL = 'http://127.0.0.1:8000/books/' 


async def ortga_handler(msg: Message):
    await msg.answer("🔙 Ortga", reply_markup=main_menu)


async def start_handler(msg: Message):
    await msg.answer(f"Assalomu alaykum {msg.from_user.full_name}, botga xush kelibsiz!", reply_markup=main_menu)


all_books = []

async def send_books(msg: Message):
    global all_books

    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as response:
            if response.status == 200:
                all_books = await response.json()
                first_3 = all_books[:3]

                keyboard = [[KeyboardButton(text=f"📚 {book['title']}")] for book in first_3]
                keyboard.append([KeyboardButton(text="🔎 Yana")])

                markup = ReplyKeyboardMarkup(
                    keyboard=keyboard,
                    resize_keyboard=True
                ) 

                await msg.answer("📚 Kitoblar ro'yxati:", reply_markup=markup)
            else:
                await msg.answer("❌ Ma'lumotlarni olishda xatolik yuz berdi.")


books = []

async def book_info(msg: Message):
    global books
    title = msg.text.lstrip("📚").strip()

    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as response:
            if response.status == 200:
                books = await response.json()
                for book in books:
                    if book['title'] == title:
                        await msg.answer(f"📘 Kitob: {book['title']}\n📝 Info: {book['description']}\n📚 Genre: {book['genre']['name']}\n🖋 Muallif: {book['author']['full_name']}")
            else: 
                await msg.answer("❌ Ma'lumotlarni olishda xatolik yuz berdi.")


more_books = []

async def send_more_books(msg: Message):
    global more_books

    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as response:
            if response.status == 200:
                more_books = await response.json()
                all = all_books

                keyboard = [[KeyboardButton(text=f"📚 {book['title']}")] for book in all]

                more_books = ReplyKeyboardMarkup(
                    keyboard=keyboard,
                    resize_keyboard=True
                ) 

                await msg.answer("📚 Kitoblar ro'yxati:", reply_markup=more_books)
            else:
                await msg.answer("❌ Ma'lumotlarni olishda xatolik yuz berdi.")
                
