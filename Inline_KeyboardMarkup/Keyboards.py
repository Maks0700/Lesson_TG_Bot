from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
keyboard_site=InlineKeyboardMarkup(row_width=2)
google_button=InlineKeyboardButton(text="google",url="https://www.google.ru/")
youtube_button=InlineKeyboardButton(text="yandex",url="https://dzen.ru/?clid=2411725&yredirect=true")
keyboard_site.row(google_button).row(youtube_button)

keybooard_links=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
but_links=KeyboardButton("/links")
keybooard_links.insert(but_links)