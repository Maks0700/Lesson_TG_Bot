from aiogram import Bot,Dispatcher,types,executor
from icecream import ic
from Token import api_token
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
import asyncio

bot=Bot(api_token)
dp=Dispatcher(bot)

async def on_start(_):
    ic("Success!!")

ikb=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("❤️",callback_data="like"),InlineKeyboardButton("👎",callback_data="dislike")]])


@dp.message_handler(commands=["start"])
async def start(message:types.Message)->None:
    await bot.send_photo(chat_id=message.chat.id,photo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/1024px-Telegram_logo.svg.png",caption="",reply_markup=ikb)

@dp.callback_query_handler()
async def  ikb_cd_handler(callback:types.CallbackQuery):
    print(callback)
    if callback.data=="like":
        await callback.answer("Тебе понравилась фотка")
    

    await callback.answer("Тебе не понравилась фотка!")

if __name__=="__main__":
    executor.start_polling(dispatcher=dp,on_startup=on_start,skip_updates=True)
    

    




