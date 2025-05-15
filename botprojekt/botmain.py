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

def get_car_by_id(car_id: int) -> Optional[Dict]:
    cars = read_data()
    for car in data:
        if car["id"] == car_id:
            return car
    return None
    

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer('ffgg')

@dp.message(Command("sell_car"))
async def sell_car(message:types.Message):
    cars = read_cars()
    car = {
        "car_id": get_next_id(),
        "company": title,
        "marka": author,
        "image": description,
        "number_phone": [g.strip() for g in genres.split(",")],
        "description": year,
    }
    data.append(new_car)
    save_cars(data)
    return {"message": "Book added successfully"}

@dp.message(Command("buy_car"))
async def start(message:types.Message):
    await message.answer(f'{data}')


async def main():
    print('Запкск бота')
    await dp.start_polling(bot)
asyncio.run(main())