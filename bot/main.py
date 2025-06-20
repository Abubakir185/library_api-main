import sys
import os

import asyncio
from bot import bot, set_commands, commands
from dispatcher import dp

async def on_start():
    await set_commands(commands)
    print("bot has been started")

async def main():
    dp.startup.register(on_start)
    await dp.start_polling(bot)

asyncio.run(main()) 
