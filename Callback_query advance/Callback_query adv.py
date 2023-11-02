from aiogram import Dispatcher,Bot,executor,types
import random
from Token import api_token
from Keyboards import keyboards
from icecream import ic

bot=Bot(api_token)
dp=Dispatcher(bot)
is_voted=True
async def on_start(_):
    ic("Success")

@dp.message_handler(commands=["start"])
async def start(message:types.Message):
  await bot.send_photo(message.chat.id,photo="https://sportishka.com/uploads/posts/2022-11/1667568678_15-sportishka-com-p-samaya-krasivaya-priroda-v-mire-krasivo-15.jpg",
                  caption="Вам нравится эта фотка?",reply_markup=keyboards)
   





@dp.callback_query_handler(text=["del_key"])
async def del_key(callback:types.CallbackQuery)->None:
     await callback.message.delete()


@dp.callback_query_handler()

async def call_procces(callback:types.CallbackQuery)->None:
    global is_voted
    if is_voted:
        if callback.data=="like":
           await callback.answer(show_alert=False,text="Тебе понравилось!!")
        await callback.answer(show_alert=False,text="Тебе не понравилось!!!")
    is_voted=False
    await callback.answer(show_alert=True,text="Ты уже проголосовал!!!")









# @dp.callback_query_handler()

# async def call(callback:types.CallbackQuery):
#     global flag
#     if flag:
#             if callback.data=="like":
#                 await callback.answer("Вам понравилась фотка!!")
#             elif callback.data=="dislike":
#                 await callback.answer("Вам не понравилась данная фотка!!")
#             elif callback.data=="del_key":
#                 await bot.edit_message_reply_markup(callback.message.chat.id,reply_markup=None)
#                 await callback.answer("Вы убрали клаву!")
#     flag=False
#     await callback.answer("Вы уже нажимали на данную фотку!!")    
    


if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True,on_startup=on_start)
