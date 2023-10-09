import telebot
from buttons import lang_btn, cities
from function import andijon, buxoro, fargona, jizzax, xorazm, namangan, navoiy, qashqadaryo, nukus, termiz, samarqand, sirdaryo, toshkent

bot = telebot.TeleBot("6485159336:AAHwEtABgpNu5Tm-xzmmmIaVOFyQAQhvHe8")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.send_message(message.chat.id, "Tilni tanlang | Choose language | выберите язык", reply_markup=lang_btn())
    except:
        pass

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "uz":
        bot.send_message(call.message.chat.id, f"Salom, {call.message.from_user.first_name}", reply_markup=cities())
    elif call.data == "en":
        bot.send_message(call.message.chat.id, f"Hello, {call.message.from_user.first_name}", reply_markup=cities())
    elif call.data == "ru":
        bot.send_message(call.message.chat.id, f"Привет, {call.message.from_user.first_name}", reply_markup=cities())

@bot.message_handler(func=lambda message: True)
def message(message):
    try:
        if message.text == "Andijon":
            bot.send_message(message.chat.id, f"Bugun havo harorati {andijon()} bo'lishi kutilmoqda", reply_markup=cities())
        elif message.text == "Buxoro":
            bot.send_message(message.chat.id, f"Bugun havo harorati {buxoro()} bo'lishi kutilmoqda", reply_markup=cities())
        elif message.text == "Farg'ona":
            bot.send_message(message.chat.id, f"Farg'ona vodiysida {fargona()} bo'lishi kutilmoqda", reply_markup=cities())
        elif message.text == "Jizzax":
            bot.send_message(message.chat.id, f"Jizzax viloyatida {jizzax()} bo'lishi kutilmoqda", reply_markup=cities())
        elif message.text == "Xorazm":
            bot.send_message(message.chat.id, f"Xorazm viloyatida {xorazm()} bo'lishi kutilmoqda", reply_markup=cities())
        elif message.text == "Namangan":
            bot.send_message(message.chat.id, f"Namangan viloyati {namangan()} bo'lishi kutilmoqda", reply_markup=cities())
        elif message.text == "Navoiy":
            bot.send_message(message.chat.id, f"Navoiy viloyatida {navoiy()} bo'lishi kutilmoqda", reply_markup=cities())
        elif message.text == "Qashqadaryo":
            bot.send_message(message.chat.id, f"Qashqadaryo viloyatida {qashqadaryo()} bo'lishi kutilmoqda", reply_markup=cities())
        elif message.text == "Nukus":
            bot.send_message(message.chat.id, f"Qoraqalpog'iston Respublikasi {nukus()} viloyati bo'lishi kutilmoqda", reply_markup=cities())
        elif message.text == "Samarqand":
            bot.send_message(message.chat.id, f"Samarqand viloyatida {samarqand()} bo'lishi kutilmoqda", reply_markup=cities())
        elif message.text == "Sirdaryo":
            bot.send_message(message.chat.id, f"Sirdaryo viloyatida {sirdaryo()} bo'lishi kutilmoqda", reply_markup=cities())
        elif message.text == "Toshkent":
            bot.send_message(message.chat.id, f"Toshkent viloyatida {toshkent()} bo'lishi kutilmoqda", reply_markup=cities())
        elif message.text == "Termiz":
            bot.send_message(message.chat.id, f"Termiz viloyatida {termiz()} bo'lishi kutilmoqda", reply_markup=cities())
    except:
        bot.send_message(message.chat.id, f"hozirda bot tamirlanyapti")


bot.infinity_polling(timeout=False, long_polling_timeout=False)