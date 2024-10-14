from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from answer import resp
router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе получить информацию о погоде, пиши название города, а я дам тебе информацию о погоде в нем")



@router.message()
async def message_handler(msg: Message):
    ans = await resp(msg.text)
    print(msg)
    print(ans)
    if type(ans) == dict:
        await msg.answer(f"Темпаратура: {ans['temp']}c\n Влажность: {ans['hum']}% \n Описание: {ans['desc']}")
        return
    await msg.answer(f"{ans}")