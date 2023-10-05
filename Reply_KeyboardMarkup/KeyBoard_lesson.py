from aiogram import types,Bot,Dispatcher,executor
from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton
from Token import api_token
from random import *

bot=Bot(api_token)
dp=Dispatcher(bot)

async def on_start(_):
    print("Success!!")


keyboard=ReplyKeyboardMarkup(resize_keyboard=True)
button1=KeyboardButton("/orange")
button2=KeyboardButton("/location")
keyboard.insert(button1).row(button2)



@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    await bot.send_message(message.from_user.id,"Добро пожаловать",reply_markup=keyboard)


@dp.message_handler(commands=["orange"])
async def or_ge(message:types.Message):
    with open ("Orange.jpg","rb") as photo:
        await bot.send_photo(message.from_user.id,photo)

@dp.message_handler(commands=["location"])
async def location(message:types.Message):
    await bot.send_location(message.from_user.id,latitude=randrange(1,100),longitude=(1,100))
    






if __name__=="__main__":
    executor.start_polling(dp,on_startup=on_start,skip_updates=True)
