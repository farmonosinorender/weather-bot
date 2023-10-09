import telebot
from buttons import lang_btn, shahar, gorod, cities
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
        bot.send_message(call.message.chat.id, f"Salom, {call.message.from_user.first_name}", reply_markup=shahar())
    elif call.data == "en":
        bot.send_message(call.message.chat.id, f"Hello, {call.message.from_user.first_name}", reply_markup=cities())
    elif call.data == "ru":
        bot.send_message(call.message.chat.id, f"Привет, {call.message.from_user.first_name}", reply_markup=gorod())

@bot.message_handler(func=lambda message: True)
def message(message):
    try:
        if message.text == "Andijon":
            bot.send_message(message.chat.id, f"Bugun havo harorati {andijon()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Buxoro":
            bot.send_message(message.chat.id, f"Bugun havo harorati {buxoro()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Farg'ona":
            bot.send_message(message.chat.id, f"Bugun havo harorati {fargona()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Jizzax":
            bot.send_message(message.chat.id, f"Bugun havo harorati {jizzax()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Xorazm":
            bot.send_message(message.chat.id, f"Bugun havo harorati {xorazm()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Namangan":
            bot.send_message(message.chat.id, f"Bugun havo harorati {namangan()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Navoiy":
            bot.send_message(message.chat.id, f"Bugun havo harorati {navoiy()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Qashqadaryo":
            bot.send_message(message.chat.id, f"Bugun havo harorati {qashqadaryo()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Nukus":
            bot.send_message(message.chat.id, f"Bugun havo harorati {nukus()} viloyati bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Samarqand":
            bot.send_message(message.chat.id, f"Bugun havo harorati {samarqand()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Sirdaryo":
            bot.send_message(message.chat.id, f"Bugun havo harorati {sirdaryo()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Toshkent":
            bot.send_message(message.chat.id, f"Bugun havo harorati {toshkent()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Termiz":
            bot.send_message(message.chat.id, f"Bugun havo harorati {termiz()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Андижан":
            bot.send_message(message.chat.id, f"Сегодня ожидается температура воздуха {andijon()}", reply_markup=gorod())
        elif message.text == "Бухара":
            bot.send_message(message.chat.id, f"Сегодня ожидается температура воздуха {buxoro()}", reply_markup=gorod())
        elif message.text == "Фергана":
            bot.send_message(message.chat.id, f"Сегодня ожидается температура воздуха {fargona()}", reply_markup=gorod())
        elif message.text == "Жиззах":
            bot.send_message(message.chat.id, f"Сегодня ожидается температура воздуха {jizzax()}", reply_markup=gorod())
        elif message.text == "Хорезм":
            bot.send_message(message.chat.id, f"Сегодня ожидается температура воздуха {xorazm()}", reply_markup=gorod())
        elif message.text == "Наманган":
            bot.send_message(message.chat.id, f"Сегодня ожидается температура воздуха {namangan()}", reply_markup=gorod())
        elif message.text == "Навои":
            bot.send_message(message.chat.id, f"Сегодня ожидается температура воздуха {navoiy()}", reply_markup=gorod())
        elif message.text == "Кашгадаря":
            bot.send_message(message.chat.id, f"Сегодня ожидается температура воздуха {qashqadaryo()}", reply_markup=gorod())
        elif message.text == "Нукус":
            bot.send_message(message.chat.id, f"Сегодня ожидается температура воздуха {nukus()}", reply_markup=gorod())
        elif message.text == "Самарканд":
            bot.send_message(message.chat.id, f"Сегодня ожидается температура воздуха {samarqand()}", reply_markup=gorod())
        elif message.text == "Сырдарья":
            bot.send_message(message.chat.id, f"Сегодня ожидается температура воздуха {sirdaryo()}", reply_markup=gorod())
        elif message.text == "Ташкент":
            bot.send_message(message.chat.id, f"Сегодня ожидается температура воздуха {toshkent()}", reply_markup=gorod())
        elif message.text == "Термиз":
            bot.send_message(message.chat.id, f"Сегодня ожидается температура воздуха {termiz()}", reply_markup=gorod())
        if message.text == "Andijan":
            bot.send_message(message.chat.id, f"Bugun havo harorati {andijon()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Bukhara":
            bot.send_message(message.chat.id, f"Bugun havo harorati {buxoro()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Fergana":
            bot.send_message(message.chat.id, f"Bugun havo harorati {fargona()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "dJizzax":
            bot.send_message(message.chat.id, f"Bugun havo harorati {jizzax()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Khorezm":
            bot.send_message(message.chat.id, f"Bugun havo harorati {xorazm()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Namangan.":
            bot.send_message(message.chat.id, f"Bugun havo harorati {namangan()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Navoi":
            bot.send_message(message.chat.id, f"Bugun havo harorati {navoiy()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Kashgadarya":
            bot.send_message(message.chat.id, f"Bugun havo harorati {qashqadaryo()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Nukus.":
            bot.send_message(message.chat.id, f"Bugun havo harorati {nukus()} viloyati bo'lishi kutilmoqda", reply_markup=cities())
        elif message.text == "Samarkand":
            bot.send_message(message.chat.id, f"Bugun havo harorati {samarqand()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Sirdarya":
            bot.send_message(message.chat.id, f"Bugun havo harorati {sirdaryo()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Tashkent":
            bot.send_message(message.chat.id, f"Bugun havo harorati {toshkent()} bo'lishi kutilmoqda", reply_markup=shahar())
        elif message.text == "Termiz.":
            bot.send_message(message.chat.id, f"Bugun havo harorati {termiz()} bo'lishi kutilmoqda", reply_markup=shahar())
    except:
        bot.send_message(message.chat.id, "ERROR")


bot.infinity_polling(timeout=False, long_polling_timeout=False)