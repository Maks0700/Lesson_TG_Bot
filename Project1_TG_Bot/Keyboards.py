from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import random

keyboard_reply = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True)
but_help = KeyboardButton(text="/help")
but_rand = KeyboardButton(text="/Random_photo")
but_description = KeyboardButton(text="/description")
keyboard_reply.add(but_help).insert(but_description).row(but_rand)
###########################################################
open_key_photo = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
but_rand_photo = KeyboardButton(text="Рандом")
but_return = KeyboardButton(text="Главное меню")

open_key_photo.add(but_rand_photo, but_return)

key_inline_photo = InlineKeyboardMarkup(row_width=2)
but_next_photo = InlineKeyboardButton(
    "Следующая рандомная фотография", callback_data="next")
but_like = InlineKeyboardButton("Лайк", callback_data="like")
but_dislike = InlineKeyboardButton("Дизлайк", callback_data="dislike")

key_inline_photo.add(but_next_photo, but_like, but_dislike)


