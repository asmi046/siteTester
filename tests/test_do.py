import os

from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.types import FSInputFile
from dotenv import load_dotenv

from aiogram.exceptions import TelegramBadRequest

from tests.recall_test import recall_test
from tests.screenshot import get_screenshot
async def recol_test_do(chat_id=""):
    load_dotenv()
    session = AiohttpSession()
    bot = Bot(token=os.getenv('TG_TOKEN'), session=session)

    if chat_id == "":
        adresat = os.getenv('TG_ADRESAT').split(",")
    else:
        adresat = [str(chat_id)]

    await recall_test()
    for chat in adresat:
        try:
            await bot.send_message(chat_id=chat.strip(), text='Закончена проверка формы обратного звонка')
        except TelegramBadRequest as e:
            print(f"Нет чата с пользователем {chat.strip()} - {e.message}")
    await session.close()

async def prtsc_main_page_do(chat_id="", url="https://rubexgroup.ru/"):
    load_dotenv()
    session = AiohttpSession()
    bot = Bot(token=os.getenv('TG_TOKEN'), session=session)

    if chat_id == "":
        adresat = os.getenv('TG_ADRESAT').split(",")
    else:
        adresat = [str(chat_id)]

    ss_url = await get_screenshot(url)
    photo = FSInputFile(ss_url)
    for chat in adresat:
        try:
            await bot.send_photo(chat_id=chat.strip(), photo=photo, caption=f"Скриншет страницы {url}")
        except TelegramBadRequest as e:
            print(f"Нет чата с пользователем {chat.strip()} - {e.message}")

    await session.close()
