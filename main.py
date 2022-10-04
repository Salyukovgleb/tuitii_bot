import telebot
from telebot import types
import datetime
from string import Template
import os



bot = telebot.TeleBot("5740063696:AAFsDE46mwLmFR6xvP9d0rx8k9zkKh34BBU")

@bot.message_handler(commands=['title'])
def start(message):
    bot.send_message(message.chat.id, 'ТАШКЕНТСКИЙ УНИВЕРСТИТЕТ ИНФОРМАЦИОННЫХ ТЕХНОЛОГИИ ИМЕНИ МУХАММАДА АЛ-ХОРАЗМИЙ')

@bot.message_handler(commands=['location'])
def location(message):
    bot.send_location(message.chat.id, 41.34063918210089,69.28656396043718)

@bot.message_handler(commands=['contact'])
def start(message):
    bot.send_message(message.chat.id, '+998998127599 - Султанова Хилола\n+998930057747 - Мирзахалилов Санджар\n+998332790802 - Приемная комиссия СФИТ ТУИТ-БГУИР')

@bot.message_handler(commands=['chanel'])
def chanel(message):
        telegram = types.InlineKeyboardMarkup()
        telegram.add(types.InlineKeyboardButton("Перейти в Telegram канал ТУИТ of БГУИР", url="https://t.me/TUITBGUIR"))
        bot.send_message(message.chat.id, "Нажмите на кнопку ниже",  reply_markup=telegram)

@bot.message_handler(commands=['support'])
def instagram(message):
        suport = types.InlineKeyboardMarkup()
        suport.add(types.InlineKeyboardButton("Напишите нам если у вас возникли вопросы", url="https://t.me/sp1ngo"))
        bot.send_message(message.chat.id, "Нажмите на кнопку ниже",  reply_markup=suport)

@bot.message_handler(commands=['complaint'])
def instagram(message):
        suport = types.InlineKeyboardMarkup()
        suport.add(types.InlineKeyboardButton("Можете написать свои жалобы или предложения", url="https://t.me/Billyrare "))
        bot.send_message(message.chat.id, "Нажмите на кнопку ниже",  reply_markup=suport)

@bot.message_handler(commands=['ceo'])
def start(message):
    bot.send_message(message.chat.id, f'Салюков Глеб Геннадьевич')

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id,
                                      f'/help - команды бота\n'
                                      f'/title - название университета\n'
                                      f'/location - адрес университета \n'
                                      f'/contact - контакты университета\n'
                                      f'/support - поддержка\n'
                                      f'/reg - заполнение формы для университета\n'
                                      f'/complaint - данная команда для жалоб или предложений\n'
                                      f'/ceo - основатель данного проекта')




smile1 = "📖"
smile2 = "👤"
smile3 = "🏢"
smile4 = "🚪"

lessons_11_21 = [
f"\r\n\r\n1 пара (11:30 - 12:50)\r\n{smile1} Проектирование программного обеспечения интеллектуальных систем (практика)\r\n{smile2} Довлетова C.\r\r\n{smile3}C корпус\r\n{smile4}344\r\n\r\n2 пара (13:30 - 14:50)\r\n{smile1} Философия (лекция)\r\n{smile2} Шерматова Н.С.\r\n{smile3}C корпус\r\n{smile4}445\r\n\r\n3 пара (15:00 - 16:20)\r\n{smile1} Общая теория интеллектуальных систем (лекция)\r\n{smile2} Мирзахалилов C\n{smile3}C корпус\r\n{smile4}445\r\n\r\n4 пара (16:30 - 17:50)\r\n{smile1} Численные методы (лекция)\r\n{smile2} Асадов К.У.\r\n{smile3}C корпус\r\n{smile4}445",
f"\r\n\r\n1 пара (13:30 - 14:50)\r\n{smile1} Операционные системы (лекция)\r\n{smile2} Касимова Ш.Т.\r\n{smile3}C корпус\r\n{smile4}361\r\n\r\n2 пара (15:00 - 16:20)\r\n{smile1} Операционные системы (лаб)\r\n{smile2} Касимова Ш.Т.\r\n{smile3}C корпус\r\n{smile4}351\r\n\r\n3 пара (16:30 - 17:50)\r\n{smile1} Численные методы (практика)\\ Меторология, стандартизация и сертификация (практика)\r\n{smile2} Асадов К.У.\\ Алламуратова З.Ж.\n{smile3}C корпус\r\n{smile4}448 \\ 447",
f"\r\n\r\n1 пара (13:30 - 14:50)\r\n{smile1} Проектирование програмного обеспечения интеллектуальных систем (лекция)\r\n{smile2} Яхшибаев Р.\r\n{smile3}C корпус\r\n{smile4}445\r\n\r\n2 пара (15:00 - 16:20)\r\n{smile1} Проектирование программного обеспечения интеллектуальных систем (лаб) \\ Общая теория интеллектуальных систем (лаб)\r\n{smile2} Яхшинбаев Р. \\ Мирзахалилов С.С.\r\n{smile3}C корпус\r\n{smile4} 344 \\ 351\r\n\r\n3 пара (16:30 - 17:50)\r\n{smile1} Метерология, стандартизация и сертификация (лекция)\r\n{smile2} Алламуратова З.Ж.\r\n{smile3}C корпус\r\n{smile4}445",
f"\r\n\r\n1 пара (13:30 - 14:50)\r\n{smile1} Теория вероятности и математическая статистика (лекция)\r\n{smile2} Чай З.С.\r\n{smile3}C корпус\r\n{smile4}361\r\n\r\n2 пара (15:00 - 16:20)\r\n{smile1} Теория вероятности\\Математические основы интеллектуалльных систем (лаб)\\ Теория вероятности и математическая статистика (практика)\r\n{smile2} Исмаилов О.М\\ Чай З.С.\r\n{smile3}C корпус\r\n{smile4}344 \\ 347\r\n\r\n3 пара (16:30 - 17:50)\r\n{smile1} Математические основы интеллектуальных систем (лаб)\r\n{smile2} Исмаилов О.М.\r\n{smile3}C корпус\r\n{smile4}344",
f"\r\n\r\n1 пара (11:30 - 12:50)\r\n{smile1} Философия (лек.)\r\n{smile2} Шерматова Н.С.\r\n{smile3}C корпус\r\n{smile4}445\r\n\r\n2 пара (13:30 - 14:50)\r\n{smile1} Философия (сем.)\r\n{smile2} Шерматова Н.С.\r\n{smile3}C корпус\r\n{smile4}447\r\n\r\n3 пара (15:00 - 16:20)\r\n{smile1} Общая теория интеллектуальных систем (лаб.)\r\n{smile2} Мирзахалилов С.С.\r\n{smile3}C корпус\r\n{smile4}351\r\n\r\n4 пара (16:30 - 17:50)\r\n{smile1} Математические основы интеллектуальных систем (лекция)\r\n{smile2} Исмаилов О.М.\r\n{smile3}C корпус\r\n{smile4}445"
]


lessons_12_21 = [
f"\r\n\r\n1 пара (11:30 - 12:50)\r\n{smile1} Философия (семинар)\r\n{smile2} Шерматова Н.C.r\r\n{smile3}C корпус\r\n{smile4}448\r\n\r\n2 пара (13:30 - 14:50)\r\n{smile1} Философия (лекция)\r\n{smile2} Шерматова Н.С.\r\n{smile3}C корпус\r\n{smile4}445\r\n\r\n3 пара (15:00 - 16:20)\r\n{smile1} Общая теория интеллектуальных систем (лекция)\r\n{smile2} Мирзахалилов C\n{smile3}C корпус\r\n{smile4}445\r\n\r\n4 пара (16:30 - 17:50)\r\n{smile1} Численные методы (лекция)\r\n{smile2} Асадов К.У.\r\n{smile3}C корпус\r\n{smile4}445",
f"\r\n\r\n1 пара (13:30 - 14:50)\r\n{smile1} Операционные системы\r\n{smile2} Касимова Ш.Т.\r\n{smile3}C корпус\r\n{smile4}361\r\n\r\n2 пара (15:00 - 16:20)\r\n{smile1} Проектирование програмного обеспечения интеллектуальных систем (лаб)\r\n{smile2} Яхшинбаев Р.\r\n{smile3}C корпус\r\n{smile4}344\r\n\r\n3 пара (16:30 - 17:50)\r\n{smile1} Метрология, стандартизация и сертификация (практика)\\ Численные методы\r\n{smile2} Алламуратова З.Ж.\\ Асадов К.У.\r\n{smile3}C корпус\r\n{smile4}447 \\ 448",
f"\r\n\r\n1 пара (13:30 - 14:50)\r\n{smile1} Проектирование програмного обеспечения интеллектуальных систем (лекция)\r\n{smile2} Яхшинбаев Р.\r\n{smile3}C корпус\r\n{smile4}445\r\n\r\n2 пара (15:00 - 16:20)\r\n{smile1} Общая теория интеллектуальных систем (лаб)\r\n{smile2} Мирзахалилов С.С.\r\n{smile3}C корпус\r\n{smile4}351\r\n\r\n3 пара (16:30 - 17:50)\r\n{smile1} Метерология, стандартизация и сертификация (лекция)\r\n{smile2} Алламуратова З.Ж.\r\n{smile3}C корпус\r\n{smile4}445",
f"\r\n\r\n1 пара (13:30 - 14:50)\r\n{smile1} Теория вероятности и математическая статистика\r\n{smile2} Чай З.С.\r\n{smile3}C корпус\r\n{smile4}361\r\n\r\n2 пара (15:00 - 16:20)\r\n{smile1} Математические основы интеллектуалльных систем (лаб)\\ Теория вероятности и математическая статистика (практика)\r\n{smile2} Исмаилов О.М\\ Чай З.С.\r\n{smile3}C корпус\r\n{smile4}344 \\ 347\r\n\r\n3 пара (16:30 - 17:50)\r\n{smile1} Операционные системы (лаб)\r\n{smile2} Касимова Ш.Т.\r\n{smile3}C корпус\r\n{smile4}351",
f"\r\n\r\n1 пара (11:30 - 12:50)\r\n{smile1} Философия\r\n{smile2} Шерматова И.С.\r\n{smile3}C корпус\r\n{smile4}445\r\n\r\n2 пара (13:30 - 14:50)\r\n{smile1} Проектирование програмного обеспечения интеллектуальных систем (практика)\r\n{smile2} Довлетова С.\r\n{smile3}C корпус\r\n{smile4}448\r\n\r\n3 пара (15:00 - 16:20)\r\n{smile1} Математические основы интеллектуальных систем (лаб)\r\n{smile2} Исмаилов О.М.\r\n{smile3}C корпус\r\n{smile4}344\r\n\r\n4 пара (16:30 - 17:50)\r\n{smile1} Математические основы интеллектуальных систем (лекция)\r\n{smile2} Исмаилов О.М.\r\n{smile3}C корпус\r\n{smile4}445"
]

lessons_13_21 = [
f"\r\n\r\n1 пара (11:30 - 12:50)\r\n{smile1} Компиляторные технологии (лаб.) \r\n{smile2} Хамзаев Ж. \r\r\n{smile3}C корпус\r\n{smile4}351\r\n\r\n2 пара (13:30 - 14:50)\r\n{smile1} Русский Язык как иностранный\r\n{smile2} Кафедра \r\n{smile3}C корпус\r\n{smile4}Кафедра\r\n\r\n3 пара (15:00 - 16:20)\r\n{smile1} Разработка пользовательских интерфейсов (лек.) \r\n{smile2} Нормуродов К.\n{smile3}C корпус\r\n{smile4}353\r\n\r\n4 пара (16:30 - 17:50)\r\n{smile1} Архитектура компьютерной техники и операционных систем (лаб.)\r\n{smile2} Мирзахалилов С.С. \r\n{smile3}C корпус\r\n{smile4}344",
f"\r\n\r\n1 пара (13:30 - 14:50)\r\n{smile1} Теория вероятностей и математическая статистика (лек.) \r\n{smile2} Чай З.С \r\n{smile3}C корпус\r\n{smile4}353\r\n\r\n2 пара (15:00 - 16:20)\r\n{smile1} Теория вероятностей и математическая статистика (прак.)\r\n{smile2} Чай З.С \r\n{smile3}C корпус\r\n{smile4}353\r\n\r\n3 пара (16:30 - 17:50)\r\n{smile1} Архитектура компьютерной техники и операционных систем (лек.)/Архитектура компьютерной техники и операционных систем (лаб.) \r\n{smile2} Мирзахалилов С.С\\ Мирзахалилов С.С \r\n{smile3}C корпус\r\n{smile4}353 \\ 344",
f"\r\n\r\n1 пара (13:30 - 14:50)\r\n{smile1} Алгоритм и структуры данных (лек.)\r\n{smile2} Нормуродов К.\r\n{smile3}C корпус\r\n{smile4}450\r\n\r\n2 пара (15:00 - 16:20)\r\n{smile1} Алгоритмы и структуры данных (лаб.) \r\n{smile2} Нормуродов К. \r\n{smile3}C корпус\r\n{smile4}353\r\n\r\n3 пара (16:30 - 17:50)\r\n{smile1} Конструирование программного обеспечения (лаб.) \r\n{smile2} Яхшибаев Р. \r\n{smile3}C корпус\r\n{smile4}449",
f"\r\n\r\n1 пара (13:30 - 14:50)\r\n{smile1} Философия (лек.) / Компиляторные технологии (лек.)\r\n{smile2} Шерматова Н.С \\ Хамзаев Ж. \r\n{smile3}C корпус\r\n{smile4}449\r\n\r\n2 пара (15:00 - 16:20)\r\n{smile1} Философия (сем.)\r\n{smile2} Шерматова Н.С \r\n{smile3}C корпус\r\n{smile4}448 \r\n\r\n3 пара (16:30 - 17:50)\r\n{smile1} Конструирование программного обеспечения (лек.)\r\n{smile2} Яхшибаев Р.\r\n{smile3}C корпус\r\n{smile4}449",
f"\r\n\r\n1 пара (11:30 - 12:50)\r\n{smile1} Разработка пользовательских интерфейсов (лаб.) \r\n{smile2} Нормуродов К. \r\n{smile3}C корпус\r\n{smile4}348\r\n\r\n2 пара (13:30 - 14:50)\r\n{smile1} Русский язык как иностранный \r\n{smile2} Кафедра \r\n{smile3}C корпус\r\n{smile4}Кафедра\r\n\r\n3 пара (15:00 - 16:20)\r\n{smile1} Философия (лек.) \r\n{smile2} Шерматова Н.С \r\n{smile3}C корпус\r\n{smile4}353\r\n\r\n4 пара (16:30 - 17:50)\r\n{smile1} Архитектура компьютерной техники и операционных систем (лек.) \r\n{smile2} Мирзахалилов С.С \r\n{smile3}C корпус\r\n{smile4}353"
]

lessons_14_21 = [
f"\r\n\r\n1 пара (13:30 - 14:50)\r\n{smile1} Физика (лекция)\r\n{smile2} Иманов Э.З.\r\n{smile3}А корпус\r\n{smile4}435\r\n\r\n2 пара (15:00 - 16:50)\r\n{smile1} Физика (лаб)\r\n{smile2} Абдуллаева Ш.И.\r\n{smile3}А корпус\r\n{smile4}426\r\n\r\n3 пара (16:30 - 17:50)\r\n{smile1} Специальные математические методы и функции (практика)\r\n{smile2} Яхшибаев Р.\n{smile3}C корпус\r\n{smile4}448",
f"\r\n\r\n1 пара (13:30 - 14:50)\r\n{smile1} Физика (лекция)\r\n{smile2} Иманов Э.З.\r\n{smile3}А корпус\r\n{smile4}435\r\n\r\n2 пара (15:00 - 16:20)\r\n{smile1} Физика (практика) \\ Математические методы в программировании (практика) \r\n{smile2} бдуллаева Ш.И. \\ Кудратов С.\r\n{smile3}А корпус\r\n{smile4}431\r\n\r\n3 пара (16:30 - 17:50)\r\n{smile1} Основа информационной безопасности\r\n{smile2} Давлетова С.Б.\r\n{smile3}C корпус\r\n{smile4}449",
f"\r\n\r\n1 пара (13:30 - 14:50)\r\n{smile1} Экономика (лекция)\r\n{smile2} Мирзарахимова А.А.\r\n{smile3}C корпус\r\n{smile4}449\r\n\r\n2 пара (15:00 - 16:20)\r\n{smile1} Электронные приборы (лекция)\\ Электронные приборы (практика)\r\n{smile2} Фазилджанов И.Р.\\ Байжанова Л.Э. \r\n{smile3}C корпус\r\n{smile4}449\r\n\r\n3 пара (16:30 - 17:50)\r\n{smile1} Электронные приборы (лаб)\r\n{smile2} Байжанова Л.Э.\r\n{smile3}А корпус\r\n{smile4}324",
f"\r\n\r\n1 пара (11:30 - 12:50)\r\n{smile1} Базы данных (лаб)\r\n{smile2} Касимова Ш.Т.\r\n{smile3}C корпус\r\n{smile4}351\r\n\r\n2 пара (13:30 - 14:50)\r\n{smile1} Русский язык как иностранный (каф)\r\n{smile2} -\r\n{smile3}C корпус\r\n{smile4} Кафедра\r\n\r\n3 пара (15:00 - 16:20)\r\n{smile1} Базы данных (лекция)\r\n{smile2} Касимова Ш.Т.\r\n{smile3}C корпус\r\n{smile4}445\r\n\r\n4 пара (16:30 - 17:50)\r\n{smile1} Основы управления интеллектуальной собственностью (лекция) \\ Основы управления интеллектуальной собственностью (практика)\r\n{smile2} Алламуратова З.Ж.\r\n{smile3}С корпус\r\n{smile4}445",
f"\r\n\r\n1 пара (11:30 - 12:50)\r\n{smile1} \\ Основы информационной безопасности (практика)\r\n{smile2} Довлетова С.Б.\r\n{smile3}C корпус\r\n{smile4}448\r\n\r\n2 пара (13:30 - 14:50)\r\n{smile1} Экономика (практика)\r\n{smile2} Мирзарахимова А.А.\r\n{smile3}C корпус\r\n{smile4}347\r\n\r\n3 пара (15:00 - 16:20)\r\n{smile1} Математические методы в программировании (лекция)\r\n{smile2} Кудратов С.\r\n{smile3}C корпус\r\n{smile4}449\r\n\r\n4 пара (16:30 - 17:50)\r\n{smile1} Специальные математические методы и функции (лекция)\r\n{smile2} Алламуратова З.Ж.\r\n{smile3}C корпус\r\n{smile4}449"
]


days = [    "Понедельник",
            "Вторник",
            "Среда",
            "Четверг",
            "Пятница"
]


user_dict = {}

class User:
    def __init__(self, city):
        self.city = city

        keys = ['fullname', 'phone', 'driverSeria',
                'driverNumber', 'driverData', 'car',
                'carModel', 'carColor', 'carNumber', 'carDate']

        for key in keys:
            self.key = None

@bot.message_handler(commands=['help', 'start'])
def start(message):
    menu = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard=True)
    raspisaniye_button = types.KeyboardButton(text='Расписание для групп')
    reg_button = types.KeyboardButton(text='/reg')
    menu.add(raspisaniye_button, reg_button)
    send_mess = f"Привееет! {message.from_user.first_name} \r\nЯ - твой помощник, который будет подсказывать расписание занятий. Не стесняйся писать мне, когда не знаешь, на какую пару идти. \r\n/help - данная команда позволяет ознакомиться с командами."
    bot.send_message(message.chat.id, send_mess, reply_markup=menu)

@bot.message_handler(func=lambda m: m.text == 'Расписание для групп')
def raspisaniye(message):
    raspisaniye_keyboard = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard=True)
    gruppa1_button = types.KeyboardButton(text='Группа 11-21')
    gruppa2_button = types.KeyboardButton(text='Группа 12-21')
    gruppa3_button = types.KeyboardButton(text='Группа 13-21')
    gruppa4_button = types.KeyboardButton(text='Группа 14-21')
    back_button = types.KeyboardButton(text='Назад в меню')
    raspisaniye_keyboard.add(gruppa1_button, gruppa2_button, gruppa3_button, gruppa4_button, back_button)
    bot.send_message(message.chat.id, 'Выберите нужный вам раздел', reply_markup=raspisaniye_keyboard)



@bot.message_handler(func=lambda m: m.text == 'Группа 11-21')
def gruppa1(message):
    gruppa1_keyboard = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard=True)
    knopka1_button = types.KeyboardButton(text='На сегодня для 11 - 21')
    knopka2_button = types.KeyboardButton(text='На завтра для 11 - 21')
    back_button = types.KeyboardButton(text='Назад в меню')
    gruppa1_keyboard.add(knopka1_button, knopka2_button, back_button)
    bot.send_message(message.chat.id, 'Выберите нужный вам раздел', reply_markup=gruppa1_keyboard)

@bot.message_handler(func=lambda m: m.text == 'Группа 12-21')
def gruppa2(message):
    gruppa2_keyboard = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard=True)
    knopka4_button = types.KeyboardButton(text='На сегодня для 12 - 21')
    knopka5_button = types.KeyboardButton(text='На завтра для 12 - 21')
    knopka6_button = types.KeyboardButton(text='Расписание')
    back_button = types.KeyboardButton(text='Назад в меню')
    gruppa2_keyboard.add(knopka4_button, knopka5_button, knopka6_button, back_button)
    bot.send_message(message.chat.id, 'Выберите нужный вам раздел', reply_markup=gruppa2_keyboard)

@bot.message_handler(func=lambda m: m.text == 'Группа 13-21')
def gruppa3(message):
    gruppa3_keyboard = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard=True)
    knopka7_button = types.KeyboardButton(text='На сегодня для 13 - 21')
    knopka8_button = types.KeyboardButton(text='На завтра для 13 - 21')

    back_button = types.KeyboardButton(text='Назад в меню')
    gruppa3_keyboard.add(knopka7_button, knopka8_button, back_button)
    bot.send_message(message.chat.id, 'Выберите нужный вам раздел', reply_markup=gruppa3_keyboard)

@bot.message_handler(func=lambda m: m.text == 'Группа 14-21')
def gruppa4(message):
    gruppa4_keyboard = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard=True)
    knopka10_button = types.KeyboardButton(text='На сегодня для 14 - 21')
    knopka11_button = types.KeyboardButton(text='На завтра для 14 - 21')
    back_button = types.KeyboardButton(text='Назад в меню')
    gruppa4_keyboard.add(knopka10_button, knopka11_button, back_button)
    bot.send_message(message.chat.id, 'Выберите нужный вам раздел', reply_markup=gruppa4_keyboard)


@bot.message_handler(commands=['reg'])
def send_reg(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    itembtn1_9 = types.KeyboardButton('ИИ')
    itembtn2_9 = types.KeyboardButton('ПМС')
    itembtn3_9 = types.KeyboardButton('ПОИТ')
    markup.add(itembtn1_9, itembtn2_9, itembtn3_9, )

    msg = bot.send_message(message.chat.id, 'Ваше направление?', reply_markup=markup)
    bot.register_next_step_handler(msg, process_city_step)

def process_city_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)

        markup = types.ReplyKeyboardMarkup(selective=False)

        msg = bot.send_message(chat_id, 'Фамилия Имя Отчество', reply_markup=markup)
        bot.register_next_step_handler(msg, process_fullname_step)

    except Exception as e:
        bot.reply_to(message, 'Данные введены не корректно')

def process_fullname_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text

        markup = types.ReplyKeyboardMarkup(selective=False)

        msg = bot.send_message(chat_id, 'Ваш номер телефона')
        bot.register_next_step_handler(msg, process_phone_step)

    except Exception as e:
        bot.reply_to(message, 'Данные введены не корректно')

def process_phone_step(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        msg = bot.send_message(chat_id, 'Номер группы')
        bot.register_next_step_handler(msg, process_driverSeria_step)

    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что то другое. Пожалуйста введите номер телефона.')
        bot.register_next_step_handler(msg, process_phone_step)

def process_driverSeria_step(message):
    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverSeria = message.text

        msg = bot.send_message(chat_id, 'Паспортыне данные')
        bot.register_next_step_handler(msg, process_driverNumber_step)

    except Exception as e:
        bot.reply_to(message, 'Данные введены не корректно')

def process_driverNumber_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverNumber = message.text

        msg = bot.send_message(chat_id, 'Национальность')
        bot.register_next_step_handler(msg, process_driverData_step)

    except Exception as e:
        bot.reply_to(message, 'Данные введены не корректно')

def process_driverData_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverDate = message.text

        msg = bot.send_message(chat_id, 'Дата рождения')
        bot.register_next_step_handler(msg, process_car_step)

    except Exception as e:
        bot.reply_to(message, 'Данные введены не корректно')

def process_car_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.car = message.text

        msg = bot.send_message(chat_id, 'Почта')
        bot.register_next_step_handler(msg, process_carModel_step)

    except Exception as e:
        bot.reply_to(message, 'Данные введены не корректно')

def process_carModel_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carModel = message.text



        msg = bot.send_message(chat_id, 'Адрес')
        bot.register_next_step_handler(msg, process_carColor_step)

    except Exception as e:
        bot.reply_to(message, 'Данные введены не корректно')

def process_carColor_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carColor = message.text

        msg = bot.send_message(chat_id, 'ФИО Родителей')
        bot.register_next_step_handler(msg, process_carNumber_step)

    except Exception as e:
        bot.reply_to(message, 'Данные введены не корректно')

def process_carNumber_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carNumber = message.text

        msg = bot.send_message(chat_id, 'Место жительство родителей')
        bot.register_next_step_handler(msg, process_carDate_step)

    except Exception as e:
        bot.reply_to(message, 'Данные введены не корректно')

def process_carDate_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carDate = message.text

        bot.send_message(chat_id, getRegData(user, 'Ваша заявка', message.from_user.first_name), parse_mode="Markdown")
        bot.send_message(-884346737, getRegData(user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")

    except Exception as e:
        print(e)
        bot.reply_to(message, 'oops!!')

def getRegData(user, title, name):
    try:
        t = Template(' $title *$name* \n Ваше направление: *$userCity* \n ФИО: *$fullname* \n Телефон: *$phone* \n Номер группы: *$driverSeria*\n Паспортные данные: *$driverNumber*\n Национальность: *$driverDate*\n Дата рождения: *$car*\n Почта: *$carModel*\n Адрес: *$carColor*\n ФИО Родителей: *$carNumber*\n Место жительство родителей: *$carDate* ')

        return t.substitute({
            'title': title,
            'name': name,
            'userCity': user.city,
            'fullname': user.fullname,
            'phone': user.phone,
            'driverSeria': user.driverSeria,
            'driverNumber': user.driverNumber,
            'driverDate': user.driverDate,
            'car': user.car,
            'carModel': user.carModel,
            'carColor': user.carColor,
            'carNumber': user.carNumber,
            'carDate': user.carDate,
        })
    except Exception as exp:
        print(exp)




@bot.message_handler(func=lambda m: m.text == 'Назад в меню')
def back(message):
    start(message)
'''******************************* Функционал *******************************************'''

@bot.message_handler(content_types= ['text'])
def answer(message):
    msg = message.text
    today = datetime.datetime.today()

    if msg == 'На сегодня для 11 - 21':
        numberOfDay = datetime.datetime.today().weekday()
        if numberOfDay > 4:
            bot.send_message(message.chat.id, "На сегодня Добби свободен)")
        else:
            if today.month < 10:
                todayMonth = "0" + f"{today.month}"
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(today.day, todayMonth, today.year) + lessons_11_21[numberOfDay])
            else:
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(today.day, today.month, today.year) + lessons_11_21[numberOfDay])

    if msg == 'На завтра для 11 - 21':
        numberOfDay = datetime.datetime.today().weekday() + 1
        if numberOfDay == 7:
            numberOfDay = 0
        if numberOfDay > 4:
            bot.send_message(message.chat.id, "Завтра пар нет, иди спи")
        else:
            tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
            if today.month < 10:
                tomorrowMonth = "0" + f"{tomorrow.month}"
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(tomorrow.day, tomorrowMonth, tomorrow.year) + lessons_11_21[numberOfDay])
            else:
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(tomorrow.day, tomorrow.month, tomorrow.year) + lessons_11_21[numberOfDay])


    if msg == 'На сегодня для 12 - 21':
        numberOfDay = datetime.datetime.today().weekday()
        if numberOfDay > 4:
            bot.send_message(message.chat.id, "На сегодня Добби свободен)")
        else:
            if today.month < 10:
                todayMonth = "0" + f"{today.month}"
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(today.day, todayMonth, today.year) + lessons_12_21[numberOfDay])
            else:
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(today.day, today.month, today.year) + lessons_12_21[numberOfDay])

    if msg == 'На завтра для 12 - 21':
        numberOfDay = datetime.datetime.today().weekday() + 1
        if numberOfDay == 7:
            numberOfDay = 0
        if numberOfDay > 4:
            bot.send_message(message.chat.id, "Завтра пар нет, иди спи")
        else:
            tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
            if today.month < 10:
                tomorrowMonth = "0" + f"{tomorrow.month}"
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(tomorrow.day, tomorrowMonth, tomorrow.year) + lessons_12_21[numberOfDay])
            else:
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(tomorrow.day, tomorrow.month, tomorrow.year) + lessons_12_21[numberOfDay])

    if msg == 'На сегодня для 13 - 21':
        numberOfDay = datetime.datetime.today().weekday()
        if numberOfDay > 4:
            bot.send_message(message.chat.id, "На сегодня Добби свободен)")
        else:
            if today.month < 10:
                todayMonth = "0" + f"{today.month}"
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(today.day, todayMonth, today.year) + lessons_13_21[numberOfDay])
            else:
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(today.day, today.month, today.year) + lessons_13_21[numberOfDay])

    if msg == 'На завтра для 13 - 21':
        numberOfDay = datetime.datetime.today().weekday() + 1
        if numberOfDay == 7:
            numberOfDay = 0
        if numberOfDay > 4:
            bot.send_message(message.chat.id, "Завтра пар нет, иди спи")
        else:
            tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
            if today.month < 10:
                tomorrowMonth = "0" + f"{tomorrow.month}"
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(tomorrow.day, tomorrowMonth, tomorrow.year) + lessons_13_21[numberOfDay])
            else:
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(tomorrow.day, tomorrow.month, tomorrow.year) + lessons_13_21[numberOfDay])


    if msg == 'На сегодня для 14 - 21':
        numberOfDay = datetime.datetime.today().weekday()
        if numberOfDay > 4:
            bot.send_message(message.chat.id, "На сегодня Добби свободен)")
        else:
            if today.month < 10:
                todayMonth = "0" + f"{today.month}"
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(today.day, todayMonth, today.year) + lessons_14_21[numberOfDay])
            else:
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(today.day, today.month, today.year) + lessons_14_21[numberOfDay])

    if msg == 'На завтра для 14 - 21':
        numberOfDay = datetime.datetime.today().weekday() + 1
        if numberOfDay == 7:
            numberOfDay = 0
        if numberOfDay > 4:
            bot.send_message(message.chat.id, "Завтра пар нет, иди спи")
        else:
            tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
            if today.month < 10:
                tomorrowMonth = "0" + f"{tomorrow.month}"
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(tomorrow.day, tomorrowMonth, tomorrow.year) + lessons_14_21[numberOfDay])
            else:
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(tomorrow.day, tomorrow.month, tomorrow.year) + lessons_14_21[numberOfDay])

    if msg == 'Расписание':
        markup = telebot.types.InlineKeyboardMarkup()
        item_0 = telebot.types.InlineKeyboardButton(text='Пн', callback_data='0')
        item_1 = telebot.types.InlineKeyboardButton(text='Вт', callback_data='1')
        item_2 = telebot.types.InlineKeyboardButton(text='Ср', callback_data='2')
        item_3 = telebot.types.InlineKeyboardButton(text='Чт', callback_data='3')
        item_4 = telebot.types.InlineKeyboardButton(text='Пт', callback_data='4')
        markup.add(item_0, item_1, item_2, item_3, item_4)
        bot.send_message(message.chat.id, "Выбери день недели", reply_markup=markup)

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    markup = telebot.types.InlineKeyboardMarkup()
    item_0 = telebot.types.InlineKeyboardButton(text='Пн', callback_data='0')
    item_1 = telebot.types.InlineKeyboardButton(text='Вт', callback_data='1')
    item_2 = telebot.types.InlineKeyboardButton(text='Ср', callback_data='2')
    item_3 = telebot.types.InlineKeyboardButton(text='Чт', callback_data='3')
    item_4 = telebot.types.InlineKeyboardButton(text='Пт', callback_data='4')
    markup.add(item_0, item_1, item_2, item_3, item_4)
    call_index = int(call.data)
    editText = days[call_index] + lessons_12_21[call_index]
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=editText, reply_markup=markup)






bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.infinity_polling()
