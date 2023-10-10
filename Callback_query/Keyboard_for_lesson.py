from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


keyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text="/help")
button2 = KeyboardButton(text="/vote")
keyboard_reply.add(button1, button2)

keyboard_inline = InlineKeyboardMarkup(row_width=2)
but1 = InlineKeyboardButton("❤️", callback_data="like")
but2 = InlineKeyboardButton("👎", callback_data="dislike")
keyboard_inline.row(but1, but2)
