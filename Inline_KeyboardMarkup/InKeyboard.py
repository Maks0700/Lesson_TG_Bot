from aiogram import Bot,types,Dispatcher,executor
from Token import api_token
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
from Keyboards import keyboard_site,keybooard_links


bot=Bot(api_token)
dp=Dispatcher(bot)

async def on_start(_):
    print("Я был запущен")
    



@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    await bot.send_message(message.from_user.id,"Добро пожаловать",reply_markup=keybooard_links)
  
@dp.message_handler(commands=["links"])
async def links(message:types.Message):
   await bot.send_message(message.from_user.id,"Ссылочки на сайты",reply_markup=keyboard_site)





if __name__=="__main__":
    executor.start_polling(dp,on_startup=on_start,skip_updates=True)