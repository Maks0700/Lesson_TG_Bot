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
list_photo = ["https://yandex.ru/images/search?img_url=https%3A%2F%2Fcdn4.telegram-cdn.org%2Ffile%2FbNdmR71LquRckXLSxfRYibUl2qOIqxQVa7dcZHPQt8O60_7S-szMFaca9444e8Le-Xne_5aUcsm8CBsM447XC5bvMhUTv4Gc7YMh2mZ9kNispqWKrJIqhU5zLj3awEGfL3qahXZ2K-rhfSbvmf335RUJT6-VzPIAFvx-RBBm0Cqhj4eHeeehXUla0dexMF8d-rqu_07GQiG3jhmRcbLvgwydIhyewn5atFub7yRULE4kzkXxiUpfdGLqSxYCpmC2NyI8RdnPNh9hFBEKzlH_dmFrEDC4byRvE3LhmV7YHIFQ5HwNMoFVxojG-ur_n2_qZtRLfKaKtp1obuTmIpcIAQ.jpg&lr=10754&pos=0&rpt=simage&source=serp&text=%D1%84%D0%BE%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%B8",
              "https://yandex.ru/images/search?img_url=https%3A%2F%2Fscontent-hel3-1.cdninstagram.com%2Fv%2Ft51.2885-15%2F89835682_492371298126510_1644642753237570765_n.jpg%3Fstp%3Ddst-jpg_e15_fr_s1080x1080%26_nc_ht%3Dscontent-hel3-1.cdninstagram.com%26_nc_cat%3D106%26_nc_ohc%3DMSoN1f9oPtwAX8FVM6_%26edm%3DAABBvjUBAAAA%26ccb%3D7-5%26oh%3D00_AT9UcTFSJ9_lG64jPLOJBc12a3C70RCHYUzQoiHjMwcWoA%26oe%3D62B5CFB3%26_nc_sid%3D83d603&lr=10754&pos=1&rpt=simage&source=serp&text=%D1%84%D0%BE%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%B8", "https://yandex.ru/images/search?img_url=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Ffb%2F8f%2F67%2Ffb8f67f32295faea3bb65bcc85cd8275.jpg&lr=10754&pos=3&rpt=simage&source=serp&text=%D1%84%D0%BE%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%B8"]


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
    await message.delete()


# @dp.message_handler(commands=["photo"])
# async def photo(message: types.Message):
#     await bot.send_message(message.from_user.id, "Выберите действие", reply_markup=keyboard_reply_photo)


# @dp.message_handler()
# async def send_photo(message: types.Message):
#     with open(random.randrange(list_photo)."jpg", "rb") as ret_photo:
#         await bot.send_photo(message.from_user.id, ret_photo)

@dp.callback_query_handler()
async def proccess_callback(callback: types.callback_query):
    if callback.data == "next":
        random_photo = random.choice(list_photo)
        await callback.message.edit_media(types.InputMedia(media=random_photo, type='photo'))
    elif callback.data == "like":
        await callback.answer("👍")
    else:

        await callback.answer("👎")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_start, skip_updates=True)
    raise SystemExit(0)
