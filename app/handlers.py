from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from tests.test_do import prtsc_main_page_do, recol_test_do

router = Router()
@router.message(Command('recol_test'))
async def recol_test(message: Message):
    await recol_test_do(message.chat.id)
    # await recol_test_do()


@router.message(Command('prtsc_main_page'))
async def prtsc_main_page(message: Message):
    await prtsc_main_page_do(message.chat.id)
    # await prtsc_main_page_do()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hi!!!")