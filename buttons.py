from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup


def button_func():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = KeyboardButton("Ob-havo ma'lumoti🌤")
    # btn2 = KeyboardButton("Ramazon taqvimi🗓")
    btn3 = KeyboardButton("Valyuta kursi💴")
    btn4 = KeyboardButton("Biz haqimizda👤")
    markup.add(btn1, btn3, btn4)
    return markup

def button_weather():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = KeyboardButton("Joylashuv bo'yicha📍")
    btn2 = KeyboardButton("Hududni tanlash🗺")
    btn3 = KeyboardButton("Orqaga⬅️")
    markup.add(btn1, btn2, btn3)
    return markup

def button_area():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = KeyboardButton("Farg'ona viloyati")
    btn2 = KeyboardButton("Toshkent viloyati")
    btn15 = KeyboardButton("Toshkent shahri")
    btn13 = KeyboardButton("Qoraqalpog'iston")
    btn3 = KeyboardButton("Andijon viloyati")
    btn4 = KeyboardButton("Namangan viloyati")
    btn5 = KeyboardButton("Xorazm viloyati")
    btn6 = KeyboardButton("Sirdaryo viloyati")
    btn7 = KeyboardButton("Samarqand viloyati")
    btn8 = KeyboardButton("Qashqadaryo viloyati")
    btn9 = KeyboardButton("Buxoro viloyati")
    btn10 = KeyboardButton("Surxondaryo viloyati")
    btn11 = KeyboardButton("Jizzax viloyati")
    btn12 = KeyboardButton("Navoiy viloyati")
    btn14 = KeyboardButton("Asosiy menyu⬅️")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn15, btn14)
    return markup

def button_currensy():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = KeyboardButton("USD-UZS")
    btn3 = KeyboardButton("EUR-UZS")
    btn4 = KeyboardButton("RUB-UZS")
    btn7 = KeyboardButton("Asosiy menyu⬅️")
    markup.add(btn1, btn3, btn4, btn7)
    return markup

def button_ramadan():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = KeyboardButton("Farg'ona shahri")
    btn15 = KeyboardButton("Toshkent shahri")
    btn13 = KeyboardButton("Qoraqalpog'iston")
    btn3 = KeyboardButton("Andijon shahri")
    btn4 = KeyboardButton("Namangan shahri")
    btn5 = KeyboardButton("Xorazm shahri")
    btn6 = KeyboardButton("Sirdaryo shahri")
    btn7 = KeyboardButton("Samarqand shahri")
    btn8 = KeyboardButton("Qashqadaryo shahri")
    btn9 = KeyboardButton("Buxoro shahri")
    btn10 = KeyboardButton("Surxondaryo shahri")
    btn11 = KeyboardButton("Jizzax shahri")
    btn12 = KeyboardButton("Navoiy shahri")
    btn16 = KeyboardButton("Qo'qon shahri")
    btn17 = KeyboardButton("Guliston shahri")
    btn18 = KeyboardButton("Marg'ilon shahri")
    btn19 = KeyboardButton("Angren shahri")
    btn20 = KeyboardButton("Xiva shahri")
    btn21 = KeyboardButton("Pop shahri")
    btn22 = KeyboardButton("Angren shahri")
    btn23 = KeyboardButton("Urgut shahri")
    btn24 = KeyboardButton("Bekobod shahri")
    btn25 = KeyboardButton("Denov shari")
    btn26 = KeyboardButton("Zomin shahri")
    btn27 = KeyboardButton("Chust shahri")
    btn14 = KeyboardButton("Asosiy menyu⬅️")
    markup.add(btn1, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn15,
               btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22, btn23, btn24, btn25, btn26, btn27, btn14)
    return markup