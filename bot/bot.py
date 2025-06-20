import os 
from aiogram import Bot
from dotenv import load_dotenv
from aiogram.types import BotCommand

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)


commands = [
    BotCommand(command="start", description="Botni ishga tushurish"),
    ]
    

async def set_commands(commands):
    await bot.set_my_commands(commands)
