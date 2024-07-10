from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile

from tests.screenshot import get_screenshot

router = Router()
@router.message(Command('prtsc_main_page'))
async def prtsc_main_page(message: Message):
    ss_url = await get_screenshot("https://rubexgroup.ru/")
    photo = FSInputFile(ss_url)
    await message.answer_photo(photo=photo)
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hi!!!")