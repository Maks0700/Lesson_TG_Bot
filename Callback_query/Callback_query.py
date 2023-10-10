from aiogram import Dispatcher, executor, types, Bot
from Token import api_token
from Keyboard_for_lesson import keyboard_inline, keyboard_reply

bot = Bot(api_token)
dp = Dispatcher(bot)


async def on_start(_):
    print("Success!!")


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Welcome to our bot", reply_markup=keyboard_reply)


@dp.message_handler(commands=["vote"])
async def vote(message: types.Message):
    with open("test.jpg", "rb") as tony_stark:
        await bot.send_photo(chat_id=message.from_user.id, photo=tony_stark, caption="Do you like this photo?", reply_markup=keyboard_inline)
    await bot.send_message(chat_id=message.from_user.id, text=" ")


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == "like":
        await callback.answer(text="Тебе понравилась данная фотография!")
    await callback.answer(text="Тебе не понравилась данная фотография!")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_start, skip_updates=True)
