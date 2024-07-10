import asyncio

import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

load_dotenv()
bot = Bot(token=os.getenv('TG_TOKEN'))
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hi!!!")

async def main():
    await dp.start_polling(bot)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
