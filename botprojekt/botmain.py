import json
import asyncio
import pandas
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router
from typing import List, Dict, Optional


bot = Bot(token="7801579886:AAH-93k3Z2xILqYaDLOQvkZatpARiTCu5pQ")
dp = Dispatcher()
router = Router()
dp.include_router(router)
data = pandas.read_json("cars.json").to_dict()

def read_data() -> List[Dict]:
    with open(data, "r", encoding="utf-8") as f:
        return json.load(f)
def save_cars(data: List[Dict]):
    with open(data, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_next_id() -> int:
    car = get_car_by_id(car_id)
    return max(car["id"] for car in data) + 1 if data else 1

def get_car_by_id(id: int) -> Optional[Dict]:
    cars = read_data()
    for car in data:
        if car["id"] == id:
            return car
    return None
    

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer('ffgg')

#получка данных на продажу
@dp.message(Command("company"))
async def company(message: types.message):
    company = message.text.replace("/company", "").strip()
    return company

@dp.message(Command("marka"))
async def marka(message: types.message):
    marka = message.text.replace("/marka", "").strip()
    return marka

@dp.message(Command("image"))
async def image(message: types.message):
    image = message.text.replace("/image", "").strip()
    return image

@dp.message(Command("number_phone"))
async def number_phone(message: types.message):
    number_phone = message.text.replace("/number_phone", "").strip()
    return number_phone

@dp.message(Command("description"))
async def description(message: types.message):
    description = message.text.replace("/description", "").strip()
    return description

#команды для машин
@dp.message(Command("sell_car"))
async def sell_car(message:types.Message):
    await message.answer('здравствуйте чтобы добавить машину в реестр объявлений вот команды для ввода:\n/company - компания производитель,\n/marka - марка машины,\n/image - ссылка на изображение,\n/number_phone - номер телефона,\n/description - описание')
    cars = data()
    new_car = {
        "id": get_next_id(),
        "company": company,
        "marka": marka,
        "image": image,
        "number_phone":number_phone,
        "description": description,
    }
    data.append(new_car)
    save_cars(data)
    return {"message": "вы выставили объявление о продаже"}

@dp.message(Command("buy_car"))
async def start(message:types.Message):
    await message.answer(f'{data}')


async def main():
    print('Запкск бота')
    await dp.start_polling(bot)
asyncio.run(main())