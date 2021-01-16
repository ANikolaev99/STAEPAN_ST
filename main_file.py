import telebot
import const
from telebot import types
import time

TOKEN = '1261241070:AAGxM_bK_Mk19Eit0rFF8WHk84fpwVPGfFA'  # полученный у @BotFather
bot = telebot.TeleBot(TOKEN)

name = ''


@bot.message_handler(commands=['start'])  # Первый запуск
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я твой персональный проводник в мир контакт-центра Сэйлз Телеком! '
                                      'Готов к путешествию?',
                     reply_markup=const.markup_menu_start)


@bot.message_handler(content_types=['text'])
def send_name(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, 'Привет! Я твой персональный проводник в мир контакт-центра Сэйлз Телеком! '
                                          'Готов к путешествию?',
                         reply_markup=const.markup_menu_start)

    elif message.text == "Да":
        bot.send_message(message.chat.id,
                         'Здорово! Давай знакомиться!) Тебя как зовут?')
        bot.register_next_step_handler(message, get_name)
    elif message.text == "Нет":
        bot.send_message(message.chat.id,
                         'Как жаль, ну давай просто пообщаемся, я обожаю, когда к нам приходят новые сотрудники!'
                         'Давай знакомиться!)''Как тебя зовут?')
        bot.register_next_step_handler(message, get_name)
    elif message.text == "Да, работал":
        bot.send_message(message.chat.id,
                         'Круто! Давай я сейчас немного расскажу о нашем контактном центре. Готов?',
                         reply_markup=const.markup_menu_ST)
    elif message.text == "Нет, не работал":
        bot.send_message(message.chat.id,
                         'Ничего страшного, у нас дружный коллектив, мы тебя всему научим! '
                         'А сейчас я хочу немного рассказать о нашей компании. Готов?',
                         reply_markup=const.markup_menu_ST)
    elif message.text == "Готов":
        keyboard_why = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Почему мы называемся SalesTelecom?", callback_data="why")
        keyboard_why.add(callback_button)
        bot.send_message(message.chat.id, 'Отлично! Если официально представляться, то мы: SalesTelecom.',
                         reply_markup=keyboard_why)
        time.sleep(3)
        bot.send_message(message.chat.id, 'А ты чем увлекаешься?')
    elif message.text == "Не готов":
        bot.send_message(message.chat.id,
                         'Ничего страшного) '
                         'У нас есть аккаунт в инстаграм для сотрудников компании, там много интересной информации. '
                         'Спроси у руководителя проекта, как нас найти в соц сетях )  '
                         'Либо отправь мне сообщение со словом "Готов", когда сможешь пообщаться.')


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, 'Очень приятно, ' + name + '! А я Степан – главный помоган ?? '
                                                                 ' Ты работал когда-нибудь в КЦ?',
                     reply_markup=const.markup_menu_rabota);


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "why":
        bot.send_message(call.message.chat.id, 'Почему мы называемся SalesTelecom?'
                                               '\nSales – продажи, Telecom- посредством телекоммуникации. Это не '
                                               'значит, что мы занимаемся только продажами. '
                                               '\nМы говорим, что продажа происходит в каждом звонке, в каждом '
                                               'контакте. '
                                               '\nЛюбое наше общение – это своеобразная продажа: общаясь с друзьями, '
                                               'мы продаем свое мнение, общаясь с ребенком – идею что-то сделать и '
                                               'так далее. '
                                               'Так что и в проектах мы не просто консультируем абонентов, а продаем '
                                               'отношение к компании, желание стать клиентом или прийти в офис. '
                                               '\nДень рождения компании – 23 июля 2013 года. Да, нам уже 7 лет!'
                                               '\nСейчас у нашей компании четыре площадки: Минск, Гомель, Витебск и '
                                               'Смоленск. Мы смело можем называть себя международниками )) '
                                               '\nСовершенно случайно все офисы оказались в шаговой доступности от '
                                               'сети ресторанов McDonalds. '
                                               '\nОпросы показали, что 18 наших коллег часто там обедают.  Надеюсь, '
                                               'что они чередуют питание фастфуд и здоровую пищу.')
        time.sleep(1)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Посмотреть видео",
                                                url="https://drive.google.com/file/d/1jV-hFF9faiio"
                                                    "-m8ylXz0Isqa2NYjSIk8/view?usp=sharing")
        keyboard.add(url_button)
        time.sleep(3)
        bot.send_message(call.message.chat.id,
                         'А еще мы любим участвовать в конкурсах, и я покажу тебе ролик о том, как мы представляем '
                         'себе работу в КЦ',
                         reply_markup=keyboard)
    if call.data == "seven":
        bot.send_message(call.message.chat.id, 'Отлично ты справился с первым вопросом.')
        time.sleep(3)
        keyboard_gorod = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Минск, Гродно, Витебск, Смоленск", callback_data="1")
        keyboard_gorod.add(callback_button_1)
        callback_button_2 = types.InlineKeyboardButton(text="Витебск, Москва, Смоленск, Гомель", callback_data="2")
        keyboard_gorod.add(callback_button_2)
        callback_button_3 = types.InlineKeyboardButton(text="Минск, Витебск, Гомель, Смоленск", callback_data="3")
        keyboard_gorod.add(callback_button_3)
        callback_button_4 = types.InlineKeyboardButton(text="Минск, Брест, Витебск, Гомель", callback_data="4")
        keyboard_gorod.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'А сейчас следующий вопрос: в каких городах есть наши офисы?',
                         reply_markup=keyboard_gorod)
    if call.data == "five":
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз!) '
                                               'Чтобы ответить правильно на вопрос, '
                                               'прочти историю "Почему мы называемся SalesTelecom?"')
    if call.data == "six":
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз!) '
                                               'Чтобы ответить правильно на вопрос, '
                                               'прочти историю "Почему мы называемся SalesTelecom?"')
    if call.data == "ten":
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз!) '
                                               'Чтобы ответить правильно на вопрос, '
                                               'прочти историю "Почему мы называемся SalesTelecom?"')
    if call.data == "1":  # Минск, Гродно, Витебск, Смоленск
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз!) '
                                               'Чтобы ответить правильно на вопрос, '
                                               'прочти историю "Почему мы называемся SalesTelecom?"')
    if call.data == "2":  # Витебск, Москва, Смоленск, Гомель
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз!) '
                                               'Чтобы ответить правильно на вопрос, '
                                               'прочти историю "Почему мы называемся SalesTelecom?"')
    if call.data == "4":  # Минск, Брест, Витебск, Гомель
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз!) '
                                               'Чтобы ответить правильно на вопрос, '
                                               'прочти историю "Почему мы называемся SalesTelecom?"')
    if call.data == "3":  # Минск, Витебск, Гомель, Смоленск
        bot.send_message(call.message.chat.id, 'Поздравляю ты справился со вторым вопросом '
                                               'и уже заработал 2 ст-шки за правильные ответы!')
        time.sleep(3)
        bot.send_message(call.message.chat.id, 'Сделаем остановку. Встретимся вечерком. Приятно было поболтать  ')


        