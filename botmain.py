import asyncio
import pandas
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router


bot = Bot(token="7801579886:AAH-93k3Z2xILqYaDLOQvkZatpARiTCu5pQ")
dp = Dispatcher()
router = Router()
dp.include_router(router)

data = pandas.read_json("cars.json").to_dict()


@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer(f'{data}')



async def main():
    print('Запкск бота')
    await dp.start_polling(bot)
asyncio.run(main())