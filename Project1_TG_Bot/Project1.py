from aiogram import types, Bot, executor, Dispatcher
import random
from Token import api_token
from Keyboards import keyboard_reply, open_key_photo, key_inline_photo
from aiogram.dispatcher.filters import Text



bot = Bot(api_token)
dp = Dispatcher(bot)


async def on_start(_):
    print("Я был запущен")

HELP_COMMAND = """
<b>/start</b> - <em>Приветствие бота</em>
<b>/help</b> - <em>Список команд</em>
<b>/description</b> - <em>Описание бота</em>



"""

async def send_rand(message:types.Message):
    random_photo=random.choice(list(photos.keys()))
    await bot.send_photo(message.chat.id,photo=random_photo,reply_markup=key_inline_photo)




list_photo = ["https://w.forfun.com/fetch/c5/c514ddd3da0d86f1348f4b10560f7f35.jpeg",
              "https://fikiwiki.com/uploads/posts/2022-02/1644918620_17-fikiwiki-com-p-krasivie-kartinki-visokogo-razresheniya-19.jpg"]


photos=dict(zip(list_photo,["Enviroment","Paris"]))

random_photo=random.choice(list(photos.keys()))



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
    global random_photo
    if callback.data=="like":
        await callback.answer("Вам понравилось")
    elif callback.data=="dislike":
        await callback.answer("Вам не понравилось")
    else:
        
        random_photo=random.choice(list(filter(lambda x:x!=random_photo,list(photos.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                                           type="photo",caption=photos[random_photo],
                                                           reply_markup=key_inline_photo))
        await callback.answer()



        
        
if __name__ == "__main__": 
    executor.start_polling(dp, on_startup=on_start, skip_updates=True)
    raise SystemExit(0)
