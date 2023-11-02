from aiogram.types import ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton,KeyboardButton

keyboards=InlineKeyboardMarkup(row_width=2)
like_but=InlineKeyboardButton(text="❤️",callback_data="like")
dislike_but=InlineKeyboardButton(text="👎",callback_data="dislike")
delete_key=InlineKeyboardButton(text="Убрать клавиатуру",callback_data="del_key")

keyboards.add(like_but,dislike_but,delete_key)

