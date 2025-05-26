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
cars_data = 'cars.json'
dataitems={}
def read_data() -> List[Dict]:
    with open(cars_data, "r", encoding="utf-8") as f:
        return json.load(f)
def save_cars(data: List[Dict]):
    with open(cars_data, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_next_id() -> int:
    data = read_data()
    return max(car["id"] for car in data) + 1 if data else 1

def get_car_by_id(id: int) -> Optional[Dict]:
    cars = read_data()
    for car in cars:
        if car["id"] == id:
            return car
    return None
    
def sell(data,dataitems):
    print(type(data), type(dataitems))
    new_car = {
        "id": get_next_id(),
        "company":dataitems.pop('company'),
        "marka":dataitems.pop('marka'),
        "image":dataitems.pop('image'),
        "number_phone":dataitems.pop("number_phone"),
        "description":dataitems.pop("description"),
    }
    data.append(new_car)
    save_cars(data)
    print(2322)
    
@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer('ffgg')

#получка данных на продажу

@dp.message(Command("company"))
async def company(message: types.message):
    dataitems.update({"company":message.text.replace("/company", "").strip()}) 
    await message.answer("компания добавлена")

@dp.message(Command("marka"))
async def marka(message: types.message):
    dataitems.update({"marka":message.text.replace("/marka", "").strip()})
    await message.answer("марка добавлена")
    
@dp.message(Command("image"))
async def image(message: types.message):
    dataitems.update({"image":message.text.replace("/image", "").strip()})
    await message.answer("фотография добавлена")

@dp.message(Command("number_phone"))
async def number_phone(message: types.message):
    dataitems.update({"number_phone":message.text.replace("/number_phone", "").strip()})
    await message.answer("номер телефона добавлен")

@dp.message(Command("description"))
async def description(message: types.message):
    dataitems.update({"description":message.text.replace("/description", "").strip()})
    await message.answer("описание добавлено")
    sell(read_data(),dataitems)

#команды для машин
@dp.message(Command("sell_car"))
async def sell_car(message:types.Message):
    await message.answer('здравствуйте чтобы добавить машину в реестр объявлений вот команды для ввода:\n/company - компания производитель,\n/marka - марка машины,\n/image - ссылка на изображение,\n/number_phone - номер телефона,\n/description - описание')    

@dp.message(Command("buy_car"))
async def start(message:types.Message):
    for value in read_data():
        await message.answer(f'{value}')

async def main():
    print('Запкск бота')
    await dp.start_polling(bot)
asyncio.run(main())