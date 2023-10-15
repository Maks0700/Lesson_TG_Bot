from aiogram import types, Bot, executor, Dispatcher
import random
from Token import api_token
from Keyboards import keyboard_reply, open_key_photo, key_inline_photo
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hide_link


bot = Bot(api_token)
dp = Dispatcher(bot)


async def on_start(_):
    print("Я был запущен")

HELP_COMMAND = """
<b>/start</b> - <em>Приветствие бота</em>
<b>/help</b> - <em>Список команд</em>
<b>/description</b> - <em>Описание бота</em>



"""
list_photo = ["city.jpg","nature.jpg","pets.jpg"]




@dp.message_handler(Text(equals="Random photo"))
async def open_keyboard_photo(message: types.Message):
    await message.answer(text="Чтобы отправить рандомную фотку, нажмите random",
                         reply_markup=open_key_photo)


@dp.message_handler(Text(equals="Главное меню"))
async def open_keyboard(message: types.Message):
    await message.answer(text="Добро пожаловать в главное меню",
                         reply_markup=keyboard_reply)


@dp.message_handler(Text(equals="Рандом"))
async def open_keyboard(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=random.choice(list_photo))
    await bot.send_message(message.from_user.id, "Какая крутая фотка!!", reply_markup=key_inline_photo)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Добро пожаловать в нашего бота!!", reply_markup=keyboard_reply)


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, HELP_COMMAND, parse_mode="html")


@dp.message_handler(commands=["description"])
async def descript(message: types.Message):
    await message.answer("Наш бот умеет отправлять случайные фотографии!!")
    await bot.send_sticker(message.chat.id, sticker="CAACAgIAAxkBAAEKcA1lGvSncg2AAAFddw2C8aDtktVtmj4AApoMAALvndlLqU1EIZoqq3kwBA")
    




@dp.callback_query_handler()
async def proccess_callback(callback: types.callback_query):
    arr_photo=[]
    if callback.data=="like":
        await callback.answer("Вам понравилось")
    elif callback.data=="dislike":
        await callback.answer("Вам не понравилось")
    else:
        for photo in list_photo:
            with open(photo,"rb") as file_photo:
                arr_photo.append(file_photo)
    
        random_photo=random.choice(arr_photo)
        await bot.send_photo(callback.message.from_user.id,random_photo,reply_markup=key_inline_photo)
        

        
        
if __name__ == "__main__": 
    executor.start_polling(dp, on_startup=on_start, skip_updates=True)
    raise SystemExit(0)
