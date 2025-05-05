import json
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

def sell_car_process(data):
    print(777)
    with open("cars.json","w",encoding="UTF-8")as f:
        json.dump(data,f)


@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer('ffgg')

@dp.message(Command("sell_car"))
async def sell_car(message:types.Message):
    sell_car_process(data)

@dp.message(Command("buy_car"))
async def start(message:types.Message):
    await message.answer(f'{data}')


async def main():
    print('Запкск бота')
    await dp.start_polling(bot)
asyncio.run(main())

