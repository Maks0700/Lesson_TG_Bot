from aiogram import executor,Dispatcher,Bot,types
from Token import api_token
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from icecream import ic


bot=Bot(api_token)
dp=Dispatcher(bot)

async def on_start(_):
    ic("Success!")

number=0

def gain_ikb()->InlineKeyboardMarkup:
    ikb=InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="increase",callback_data="btn_increase"),InlineKeyboardButton(text="decrease",callback_data="btn_decrease")
        ],
        ])
    return ikb


@dp.message_handler(commands=["start"])
async def cmd_start(message:types.Message)->None:
    
    
    await message.answer(f"The current number is {number}",reply_markup=gain_ikb())

@dp.callback_query_handler(lambda callback_query:callback_query.data.startswith("btn"))
async def call_proccess(callback:types.CallbackQuery)->None:
    global number
    if callback.data=="btn_increase":
        number+=1
        await callback.bot.edit_message_text(f"The current number is {number}",reply_markup=gain_ikb())
    elif callback.data=="btn_decrease":
        number-=1
        await callback.bot.edit_message_text(f"The current number is {number}",reply_markup=gain_ikb())










if __name__=="__main__":
    executor.start_polling(dp,on_startup=on_start,skip_updates=True)