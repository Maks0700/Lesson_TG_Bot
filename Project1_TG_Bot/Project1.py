from aiogram import Dispatcher,types,executor,Bot
from Keyboards import keyboard_reply,key_inline_photo,open_key_photo
import random
from aiogram.types import InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup
from  Token import api_token
from icecream import ic
from aiogram.dispatcher.filters import Text

bot=Bot(api_token)
dp=Dispatcher(bot)

async def on_start(_):
    ic("Success!!")


HELP_COMMAND="""

<b>/start</b> - <em>приветствие бота</em>
<b>/description</b> - <em>описание бота</em>
<b>/help</b> - <em>список команд</em>

"""

flag=False

list_ex=["https://proprikol.ru/wp-content/uploads/2020/04/krasivye-kartinki-vysokogo-razresheniya-3.jpg","https://w.forfun.com/fetch/03/03f8cd3f6796daaacc1fe43ffb7704b7.jpeg"]
dict_photos=dict(zip(list_ex,["first","second"]))
random_photo=random.choice(list(dict_photos.keys()))

@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    await message.answer("Привет, рад тебя видеть в нашем боте!!!",reply_markup=keyboard_reply)


@dp.message_handler(commands=["help"])
async def help(message:types.Message):
    await message.answer(HELP_COMMAND,parse_mode="html")


@dp.message_handler(commands=["description"])
async def descript(message:types.Message):
    await message.answer("Наш бот умеет отправлять рандомные фотографии и стикеры!!")
    await bot.send_sticker(message.chat.id,sticker="CAACAgIAAxkBAAEKcA1lGvSncg2AAAFddw2C8aDtktVtmj4AApoMAALvndlLqU1EIZoqq3kwBA")


@dp.message_handler(commands=["Random_photo"])
async def rand_photo(message:types.Message):
    await message.answer("Чтобы получить рандомную фотку необходимо отправить команду Рандом",reply_markup=open_key_photo)


@dp.message_handler(Text(equals="Рандом"))
async def rand(message:types.Message):
    random_photo=random.choice(list(dict_photos.keys()))
    await bot.send_photo(message.from_user.id,random_photo,caption=dict_photos[random_photo],reply_markup=key_inline_photo)


@dp.message_handler(Text(equals="Главное меню"))
async def return_main_menu(message:types.Message):
    await message.answer("Вы вернулись в главное меню",reply_markup=keyboard_reply)


@dp.callback_query_handler()

async def vote(callback:types.CallbackQuery):
    global flag
    global random_photo
    if callback.data=="like":
        if not flag:
            await callback.message.answer("Лайк этой фотки")
            flag=True
        else:
            await callback.message.answer("Вы уже лайкали эту фотку!")
    elif callback.data =="dislike":
        await callback.message.answer("Дизлайк этой фотки")
    else:
        random_photo=random.choice(list(filter(lambda x:x!=random_photo,list(dict_photos.keys()))))
        await bot.edit_message_text(chat_id=callback.message.chat.id,photo=random_photo,caption=dict_photos[random_photo]
                             ,reply_markup=key_inline_photo)




if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True,on_startup=on_start)