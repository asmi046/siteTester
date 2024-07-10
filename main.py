import asyncio

import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.handlers import router

load_dotenv()
bot = Bot(token=os.getenv('TG_TOKEN'))
dp = Dispatcher()



async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
