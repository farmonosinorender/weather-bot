from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

def lang_btn():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("O'zbek 🇺🇿", callback_data='uz'),
        InlineKeyboardButton("English 🇬🇧", callback_data='en'),
        InlineKeyboardButton("Русский 🇷🇺", callback_data='ru')
    )
    return markup

def cities():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton("Andijon"), KeyboardButton("Buxoro"),
        KeyboardButton("Farg'ona"), KeyboardButton("Jizzax"),
        KeyboardButton("Xorazm"), KeyboardButton("Namangan"),
        KeyboardButton("Navoiy"), KeyboardButton("Qashqadaryo"),
        KeyboardButton("Nukus"), KeyboardButton("Samarqand"),
        KeyboardButton("Sirdaryo"), KeyboardButton("Toshkent"),
        KeyboardButton("Termiz")
    )
    return markup