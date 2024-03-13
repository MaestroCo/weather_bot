from telebot import TeleBot, types
from telebot.types import Message, ReplyKeyboardRemove, Location
from buttons import button_func, button_weather, button_area, button_currensy, button_ramadan
import requests
from datetime import datetime, timezone, timedelta

bot = TeleBot('7132283634:AAEl-ULKg5pH9roE-LJElkfQU_8X5YjSuoM', parse_mode='HTML')
weather_API = 'b01e7608c07f15c54ff9d9b64d478705'
currency_API = '7f8fb6c0014e4faf9ed889dd771b1d21'

parameters_currency = {
    'currency': currency_API
}

parameters = {
    'appid': weather_API,
    'units': 'metric'
}

regions = {
    "Farg'ona viloyati": "Fergana",
    "Andijon viloyati": "Andijan",
    "Namangan viloyati": "Namangan",
    "Sirdaryo viloyati": "Guliston",
    "Jizzax viloyati": "Jizzakh",
    "Samarqand viloyati": "Samarkand",
    "Buxoro viloyati": "Bukhara",
    "Navoiy viloyati": "Navoi",
    "Qashqadaryo viloyati": "Qarshi",
    "Surxondaryo viloyati": "Termez",
    "Xorazm viloyati": "Urgench",
    "Qoraqalpog'iston respublikasi": "Nukus",
    "Toshkent viloyati": "Tashkent",
}

cities = {
    "Farg'ona shahri": open("image/fargona.png", 'rb'), "Toshkent shahri": open('image/toshkent.jpg', 'rb'), "Qoraqalpog'iston":
        open('image/nukus.png', 'rb'), "Andijon shahri": open("image/andijon.jpg", 'rb'), "Namangan shahri"
    : open('image/namangan.png', 'rb'), "Urganch shahri": open('image/urganch.png', 'rb'), "Samarqand shahri"
    : open('image/samarqand.png', 'rb'), "Qashqadaryo shahri": open('image/qarshi.png', 'rb'),
    "Buxoro shahri": open('image/buxoro.jpg', 'rb'), "Termiz shahri": open('image/termiz.png', 'rb'), "Jizzax shahri"
    : open('image/jizzax.png', 'rb'), "Navoiy shahri": open('image/navoiy.png', 'rb'), "Qo'qon shahri"
    : open('image/qoqon.png', 'rb'), "Guliston shahri": open('image/guliston.png', 'rb'),
    "Marg'ilon shahri": open('image/margion.png', 'rb'), "Angren shahri": open('image/angren.png', 'rb'), "Xiva shahri"
    : open('image/xiva.png', 'rb'), "Pop shahri": open('image/pop.png', 'rb'), "Urgut shahri": open('image/urgut.jpg', 'rb'),
    "Bekobod shahri": open('image/bekobod.png', 'rb'), "Denov shari": open('image/denov.jpg', 'rb'), "Zomin shahri"
    : open('image/zomin.png', 'rb'), "Chust shahri": open('image/chust.jpg', 'rb'), "Shahrixon shahri": open('image/shsahrixon.png', 'rb'),
    "Qorako'l shahri": open('image/qorakol.png', 'rb'), "Nurota shahri": open('image/nurota.png', 'rb')

}

@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"""<b>Salom {message.from_user.full_name}! Men All Info BOT man.</b>
<i>Ob-havo🌤
Valyuta kursi💴
Ramazon taqvimi🗓</i>
<b>haqidagi ma\'lumotlarni bilib olishingiz mumkin.</b>""", reply_markup=button_func())

@bot.message_handler(func=lambda message: message.text == "Ob-havo ma'lumoti🌤")
def send_weather_region(message: Message):
    chat_id = message.chat.id
    info = f"""<b>{message.from_user.full_name} iltimos qaysi usulda
ob-havo ma'lumotni bilib olmoqchi ekanligingizni tanlang👇</b>"""
    bot.send_message(chat_id, "Ob-havo ma'lumoti🌤", reply_markup=ReplyKeyboardRemove())
    bot.send_message(chat_id, info, reply_markup=button_weather())

# Hududni tanlash bo'yicha qismi -------------------------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == "Hududni tanlash🗺")
def send_area(message: Message):
    chat_id = message.chat.id
    info = f"""<b>{message.from_user.full_name} o'zingiz yashaydigan hududni tanlang👇</b>"""
    bot.send_message(chat_id, "<b>Hududni tanlash🗺</b>", reply_markup=ReplyKeyboardRemove())
    bot.send_message(chat_id, info, reply_markup=button_area())


@bot.message_handler(func=lambda message: message.text in regions)
def send_weather_info(message: Message):
    chat_id = message.chat.id
    region_name = message.text
    city_name = regions[region_name]

    parameters['q'] = city_name
    req = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters).json()

    if req['cod'] == 200:
        city = region_name
        temperature = req['main']['temp']
        max_temp = req['main']['temp_max']
        min_temp = req['main']['temp_min']
        wind = req['wind']['speed']
        clouds = req['clouds']['all']
        user_timezone = timezone(timedelta(hours=5))
        sunrise = datetime.fromtimestamp(req['sys']['sunrise'], tz=timezone.utc).astimezone(user_timezone).strftime(
            '%d.%m.%y %H:%M:%S')
        sunset = datetime.fromtimestamp(req['sys']['sunset'], tz=timezone.utc).astimezone(user_timezone).strftime(
            '%d.%m.%y %H:%M:%S')

        info = f"""<b>{city}da bugun🏙</b>
<b>Havo harorati:</b> <i>{temperature}</i>🌡
<b>Eng yuqori harorat::</b> <i>{max_temp}</i>🌡
<b>Eng past harorat::</b> <i>{min_temp}</i>🌡
<b>Shamol tezligi:</b> <i>{wind} m/s</i>💨
<b>Bulut darajasi:</b> <i>{clouds}%</i>☁️
<b>Quyosh chiqishi:</b> <i>{sunrise}</i>🌄
<b>Quyosh botishi:</b> <i>{sunset}</i>🌇"""
        bot.send_message(chat_id, info, reply_markup=button_area())
    else:
        bot.send_message(chat_id,
                         "Uzr, ob-havo ma'lumotini olishda xatolik yuz berdi. Iltimos, qaytadan urinib ko'ring.",
                         reply_markup=button_area())

# Joylashuvni tanlash bo'yicha qismi -----------------------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == "Joylashuv bo'yicha📍")
def request_location(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"<b>{message.from_user.full_name} joylashuvingizni yuboring:</b>",
                     reply_markup=ReplyKeyboardRemove(), parse_mode='HTML')

@bot.message_handler(content_types=['location'])
def process_location(message: Message):
    chat_id = message.chat.id
    latitude = message.location.latitude
    longitude = message.location.longitude

    req = requests.get('https://api.openweathermap.org/data/2.5/weather',
                       params={'lat': latitude, 'lon': longitude, **parameters}).json()

    if req['cod'] == 200:
        city_name = req['name']
        temperature = req['main']['temp']
        max_temp = req['main']['temp_max']
        min_temp = req['main']['temp_min']
        wind = req['wind']['speed']
        clouds = req['clouds']['all']
        user_timezone = timezone(timedelta(hours=5))
        sunrise = datetime.fromtimestamp(req['sys']['sunrise'], tz=timezone.utc).astimezone(user_timezone).strftime(
            '%d.%m.%y %H:%M:%S')
        sunset = datetime.fromtimestamp(req['sys']['sunset'], tz=timezone.utc).astimezone(user_timezone).strftime(
            '%d.%m.%y %H:%M:%S')

        info = f"""<b>{city_name} shahrida bugun</b>🏙
<b>Hozirgi harorat:</b> <i>{temperature}</i>🌡
<b>Eng yuqori harorat:</b> <i>{max_temp}</i>🌡
<b>Eng past harorat:</b> <i>{min_temp}</i>🌡
<b>Shamol tezligi:</b> <i>{wind} m/s</i>💨
<b>Bulut darajasi:</b> <i>{clouds}%</i>☁️
<b>Quyosh chiqishi:</b> <i>{sunrise}</i>🌄
<b>Quyosh botishi:</b> <i>{sunset}</i>🌇"""
        bot.send_message(chat_id, info, reply_markup=button_weather())
    else:
        bot.send_message(chat_id,
                         "Uzr, ob-havo ma'lumotini olishda xatolik yuz berdi. Iltimos, qaytadan urinib ko'ring.",
                         reply_markup=button_area())

# Valyuta kursi bo'yicha qismi ----------------------------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == "Valyuta kursi💴")
def currency(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Valyuta kursi💴", reply_markup=ReplyKeyboardRemove())
    bot.send_message(chat_id, f"{message.from_user.full_name} o'zingizga kerakli bo'limni tanlang👇", reply_markup=
                     button_currensy())

@bot.message_handler(func=lambda message: message.text == 'USD-UZS')
def usd_to_uzs(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"<b>USD-UZS</b>")
    req = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={currency_API}&base=USD&symbols=UZS').json()
    rate = req['rates']['UZS']
    bot.send_message(chat_id, f"<b>1</b> <i>USD</i><b> {rate}</b><i> UZS ga teng!</i>")

@bot.message_handler(func=lambda message: message.text == 'EUR-UZS')
def eur_to_uzs(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"<b>EUR-UZS</b>")
    req = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={currency_API}&base=USD&symbols=UZS').json()
    rate = req['rates']['UZS']
    eurotouzs = rate + 1066
    bot.send_message(chat_id, f"<b>1</b> <i>EUR</i><b> {eurotouzs}</b><i> UZS ga teng!</i>")

@bot.message_handler(func=lambda message: message.text == 'RUB-UZS')
def eur_to_uzs(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"<b>RUB-UZS</b>")
    req = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={currency_API}&base=USD&symbols=UZS').json()
    rate = req['rates']['UZS']
    rubtouzs = rate - 12394
    bot.send_message(chat_id, f"<b>1</b> <i>RUB</i><b> {rubtouzs}</b><i> UZS ga teng!</i>")

# Ramazon taqvimi kod qismi --------------------------------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == 'Ramazon taqvimi🗓')
def ramazon_taqvimi(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"<b>Ramazon taqvimi🗓</b>", reply_markup=ReplyKeyboardRemove())
    bot.send_message(chat_id, f"<b>Yashash hududizni tanlang👇</b>", reply_markup=button_ramadan())

@bot.message_handler(func=lambda message: message.text in cities)
def send_pic(m: Message):
    chat_id = m.chat.id
    city_name = m.text
    pic = cities[city_name]
    bot.send_message(chat_id, f"<b>{city_name} ramazon taqvimi rasim ko'rinishida👇</b>")
    bot.send_photo(chat_id, pic)
    bot.send_message(chat_id, f"<b>Roʻza tutish (saharlik, ogʻiz yopish) duosi🤲 </b>\n\n"
                              f"<i>Navaytu an asuvma sovma shahri ramazona minal fajri ilal magʻribi, "
                              f"xolisan lillahi taʼaalaa Allohu akbar. </i>\n\n<b> Maʼnosi: </b><i>Ramazon oyining "
                              f"roʻzasini subhdan to "
                              f"kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.</i> \n\n"
                              f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                              f"<b>Iftorlik (ogʻiz ochish) duosi🤲 </b>\n\n"
                              f"<i>Allohumma laka sumtu va bika aamantu va aʼlayka tavakkaltu va aʼlaa rizqika aftartu,"
                              f"fagʻfirliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn. </i>\n\n"
                              f"<b> Maʼnosi: </b><i>Ey Alloh, ushbu Roʻzamni Sen uchun tutdim va Senga iymon keltirdim "
                              f"va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng "
                              f"mehriboni, mening avvalgi va keyingi gunohlarimni magʻfirat qilgil.</i>", reply_markup=button_ramadan())

@bot.message_handler(func=lambda message: message.text == 'Biz haqimizda👤')
def biz_haqimizda(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"<b>Yaratuvchi: Maxammadjonov Murodjon \n Aloqa: https://t.me/murodjon_m</b>")

@bot.message_handler(func=lambda message: message.text == "Asosiy menyu⬅️")
def send_back_area(message: Message):
    chat_id = message.chat.id
    info = f"""<b>Asosiy menyu⬅️</b>"""
    bot.send_message(chat_id, info, reply_markup=ReplyKeyboardRemove())
    bot.send_message(chat_id, "<b>Asosiy menyuga qaytildi📫</b>", reply_markup=button_func())

@bot.message_handler(func=lambda message: message.text == "Orqaga⬅️")
def send_back(message: Message):
    chat_id = message.chat.id
    info = f"""<b>Orqaga⬅️</b>"""
    bot.send_message(chat_id, info, reply_markup=ReplyKeyboardRemove())
    bot.send_message(chat_id, "Asosiy menyuga qaytildi📫", reply_markup=button_func())







bot.infinity_polling()