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
    elif message.text == "привет":
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
    elif message.text == "Работал":
        bot.send_message(message.chat.id,
                         'Круто! Давай я сейчас немного расскажу о нашем контактном центре. Готов?',
                         reply_markup=const.markup_menu_ST)
    elif message.text == "Не работал":
        bot.send_message(message.chat.id,
                         'Ничего страшного, у нас дружный коллектив, мы тебя всему научим! '
                         'А сейчас я хочу немного рассказать о нашей компании. Готов?',
                         reply_markup=const.markup_menu_ST)
    elif message.text == "Готов":
        bot.send_message(message.chat.id, 'Отлично! Если официально представляться, то мы: SalesTelecom.')

        bot.send_photo(message.chat.id,
                       'https://drive.google.com/file/d/1kC7ABmVe45HGhAoAem9jSeVPqPRQQoVk/view?usp=sharing')
        time.sleep(1)
        bot.send_message(message.chat.id, '\nSales – продажи, Telecom- посредством телекоммуникации. Это не '
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
        time.sleep(5)
        bot.send_message(message.chat.id,
                         'А еще мы любим участвовать в конкурсах, и я покажу тебе ролик о том, как мы представляем '
                         'себе работу в КЦ',
                         reply_markup=keyboard)
        time.sleep(10)
        bot.send_message(message.chat.id, 'А ты чем увлекаешься?')
    elif message.text == "Не готов":
        bot.send_message(message.chat.id,
                         'Ничего страшного) '
                         '\nУ нас есть аккаунт в инстаграм для сотрудников компании, там много интересной информации. '
                         'Спроси у руководителя проекта, как нас найти в соц сетях )  '
                         '\nЛибо отправь мне сообщение со словом "Готов", когда сможешь пообщаться.')

    elif message.text == "Давай продолжим":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI_DF-X-nQjiGUsJ9dtnsFDLDqNxujSAAIpAAPBnGAM8EupHr_Y33wbBA')
        time.sleep(1)
        bot.send_message(message.chat.id, 'Переходим к вопросам)')
        time.sleep(1)
        bot.send_message(message.chat.id, 'Давай разберем с тобой правила работы с клиентом')
        time.sleep(1)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="А", callback_data="А_день2")
        callback_button_2 = types.InlineKeyboardButton(text="Б", callback_data="Б_день2")
        callback_button_3 = types.InlineKeyboardButton(text="В", callback_data="В_день2")
        callback_button_4 = types.InlineKeyboardButton(text="Г", callback_data="Г_день2")
        keyboard_vopros1.add(callback_button_1, callback_button_2)
        keyboard_vopros1.add(callback_button_3, callback_button_4)
        bot.send_message(message.chat.id, 'Выберите правильный ответ:'
                                          '\nА) называем девушка, мужчина, молодой человек, женщина и т.д.'
                                          '\nБ) обращаемся на «Вы» обобщено, нет необходимости уточнять имя клиента'
                                          '\nВ) уточняем имя и обращаемся по полному имени, например, Валерий'
                                          '\nГ) если клиент сказал, что его зовут Саша, то так его и называем, '
                                          'не стоит переходить на Александр) ',
                         reply_markup=keyboard_vopros1)
    elif message.text == "Не совсем":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAKhbV_0ZglqsgI_O4XNAxsi5vL0q9LIAAIlAAPBnGAMsZsU2SseitYeBA')
        time.sleep(1)
        bot.send_message(message.chat.id,
                         'Жаль, тогда давай перейдем к вопросам без подготовки. Ты справишься, я уверен!')
        time.sleep(1)
        bot.send_message(message.chat.id, 'Давай разберем с тобой правила работы с клиентом')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="А", callback_data="А_день2")
        callback_button_2 = types.InlineKeyboardButton(text="Б", callback_data="Б_день2")
        callback_button_3 = types.InlineKeyboardButton(text="В", callback_data="В_день2")
        callback_button_4 = types.InlineKeyboardButton(text="Г", callback_data="Г_день2")
        keyboard_vopros1.add(callback_button_1, callback_button_2)
        keyboard_vopros1.add(callback_button_3, callback_button_4)
        bot.send_message(message.chat.id, 'Выберите правильный ответ:'
                                          '\nА) называем девушка, мужчина, молодой человек, женщина и т.д.'
                                          '\nБ) обращаемся на «Вы» обобщено, нет необходимости уточнять имя клиента'
                                          '\nВ) уточняем имя и обращаемся по полному имени, например, Валерий'
                                          '\nГ) если клиент сказал, что его зовут Саша, то так его и называем, '
                                          'не стоит переходить на Александр) ',
                         reply_markup=keyboard_vopros1)
    else:
        bot.send_message(message.chat.id, 'Интересненько...😃 ')
        time.sleep(3)
        bot.send_message(message.chat.id, 'Слушай, ' + name + ', чтобы тебе было полезно со мной общаться, '
                                                              'давай определим, что получит активный и '
                                                              'заинтересованный участник. '
                                                              'Тот, кто продолжит со мной общаться на протяжении 4 '
                                                              'дней, '
                                                              'получит набор новичка')
        time.sleep(3)
        bot.register_next_step_handler(message, get_name)
        keyboard_age = types.InlineKeyboardMarkup()
        callback_button_five = types.InlineKeyboardButton(text="5 лет", callback_data="5 лет")
        keyboard_age.add(callback_button_five)
        callback_button_six = types.InlineKeyboardButton(text="6 лет", callback_data="6 лет")
        keyboard_age.add(callback_button_six)
        callback_button_seven = types.InlineKeyboardButton(text="7 лет", callback_data="7 лет")
        keyboard_age.add(callback_button_seven)
        callback_button_ten = types.InlineKeyboardButton(text="10 лет", callback_data="10 лет")
        keyboard_age.add(callback_button_ten)
        bot.send_message(message.chat.id, 'Итак, первый вопрос. Сколько лет нашей компании?',
                         reply_markup=keyboard_age)


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, 'Очень приятно, ' + name + '! А я Степан – главный помоган!'
                                                                 ' Ты работал когда-нибудь в КЦ?',
                     reply_markup=const.markup_menu_rabota)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # ДЕНЬ 1
    # Вопрос 1
    if call.data == "5 лет":
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз!) '
                                               'Чтобы ответить правильно на вопрос, '
                                               'прочти историю "Почему мы называемся SalesTelecom?"')
        time.sleep(1)
        keyboard_age = types.InlineKeyboardMarkup()
        callback_button_five = types.InlineKeyboardButton(text="5 лет", callback_data="5 лет")
        keyboard_age.add(callback_button_five)
        callback_button_six = types.InlineKeyboardButton(text="6 лет", callback_data="6 лет")
        keyboard_age.add(callback_button_six)
        callback_button_seven = types.InlineKeyboardButton(text="7 лет", callback_data="7 лет")
        keyboard_age.add(callback_button_seven)
        callback_button_ten = types.InlineKeyboardButton(text="10 лет", callback_data="10 лет")
        keyboard_age.add(callback_button_ten)
        bot.send_message(call.message.chat.id, 'Сколько же лет нашей компании?',
                         reply_markup=keyboard_age)
    if call.data == "6 лет":
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз!) '
                                               'Чтобы ответить правильно на вопрос, '
                                               'прочти историю "Почему мы называемся SalesTelecom?"')
        time.sleep(1)
        keyboard_age = types.InlineKeyboardMarkup()
        callback_button_five = types.InlineKeyboardButton(text="5 лет", callback_data="5 лет")
        keyboard_age.add(callback_button_five)
        callback_button_six = types.InlineKeyboardButton(text="6 лет", callback_data="6 лет")
        keyboard_age.add(callback_button_six)
        callback_button_seven = types.InlineKeyboardButton(text="7 лет", callback_data="7 лет")
        keyboard_age.add(callback_button_seven)
        callback_button_ten = types.InlineKeyboardButton(text="10 лет", callback_data="10 лет")
        keyboard_age.add(callback_button_ten)
        bot.send_message(call.message.chat.id, 'Сколько же лет нашей компании?',
                         reply_markup=keyboard_age)
    if call.data == "10 лет":
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз!) '
                                               'Чтобы ответить правильно на вопрос, '
                                               'прочти историю "Почему мы называемся SalesTelecom?"')
        time.sleep(1)
        keyboard_age = types.InlineKeyboardMarkup()
        callback_button_five = types.InlineKeyboardButton(text="5 лет", callback_data="5 лет")
        keyboard_age.add(callback_button_five)
        callback_button_six = types.InlineKeyboardButton(text="6 лет", callback_data="6 лет")
        keyboard_age.add(callback_button_six)
        callback_button_seven = types.InlineKeyboardButton(text="7 лет", callback_data="7 лет")
        keyboard_age.add(callback_button_seven)
        callback_button_ten = types.InlineKeyboardButton(text="10 лет", callback_data="10 лет")
        keyboard_age.add(callback_button_ten)
        bot.send_message(call.message.chat.id, 'Сколько же лет нашей компании?',
                         reply_markup=keyboard_age)
    if call.data == "7 лет":
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKhVV_0Wpzb_9oGqtG3pWIqNv2nCH4CAAIEAAM7YCQUs6vrVG-V4aseBA')
        bot.send_message(call.message.chat.id, 'Поздравляю! Ты справился с первым вопросом 👍')
        time.sleep(3)
        keyboard_gorod = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Минск, Гродно, Витебск, Смоленск",
                                                       callback_data="Минск, Гродно, Витебск, Смоленск")
        keyboard_gorod.add(callback_button_1)
        callback_button_2 = types.InlineKeyboardButton(text="Витебск, Москва, Смоленск, Гомель",
                                                       callback_data="Витебск, Москва, Смоленск, Гомель")
        keyboard_gorod.add(callback_button_2)
        callback_button_3 = types.InlineKeyboardButton(text="Минск, Витебск, Гомель, Смоленск",
                                                       callback_data="Минск, Витебск, Гомель, Смоленск")
        keyboard_gorod.add(callback_button_3)
        callback_button_4 = types.InlineKeyboardButton(text="Минск, Брест, Витебск, Гомель",
                                                       callback_data="Минск, Брест, Витебск, Гомель")
        keyboard_gorod.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'А сейчас следующий вопрос: в каких городах есть наши офисы?',
                         reply_markup=keyboard_gorod)
    # ДЕНЬ1
    # Вопрос 2
    if call.data == "Минск, Гродно, Витебск, Смоленск":
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз!) '
                                               'Чтобы ответить правильно на вопрос, '
                                               'прочти историю "Почему мы называемся SalesTelecom?"')
        time.sleep(1)
        keyboard_gorod = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Минск, Гродно, Витебск, Смоленск",
                                                       callback_data="Минск, Гродно, Витебск, Смоленск")
        keyboard_gorod.add(callback_button_1)
        callback_button_2 = types.InlineKeyboardButton(text="Витебск, Москва, Смоленск, Гомель",
                                                       callback_data="Витебск, Москва, Смоленск, Гомель")
        keyboard_gorod.add(callback_button_2)
        callback_button_3 = types.InlineKeyboardButton(text="Минск, Витебск, Гомель, Смоленск",
                                                       callback_data="Минск, Витебск, Гомель, Смоленск")
        keyboard_gorod.add(callback_button_3)
        callback_button_4 = types.InlineKeyboardButton(text="Минск, Брест, Витебск, Гомель",
                                                       callback_data="Минск, Брест, Витебск, Гомель")
        keyboard_gorod.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'В каких городах есть наши офисы?',
                         reply_markup=keyboard_gorod)
    if call.data == "Витебск, Москва, Смоленск, Гомель":
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз!) '
                                               'Чтобы ответить правильно на вопрос, '
                                               'прочти историю "Почему мы называемся SalesTelecom?"')
        time.sleep(1)
        keyboard_gorod = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Минск, Гродно, Витебск, Смоленск",
                                                       callback_data="Минск, Гродно, Витебск, Смоленск")
        keyboard_gorod.add(callback_button_1)
        callback_button_2 = types.InlineKeyboardButton(text="Витебск, Москва, Смоленск, Гомель",
                                                       callback_data="Витебск, Москва, Смоленск, Гомель")
        keyboard_gorod.add(callback_button_2)
        callback_button_3 = types.InlineKeyboardButton(text="Минск, Витебск, Гомель, Смоленск",
                                                       callback_data="Минск, Витебск, Гомель, Смоленск")
        keyboard_gorod.add(callback_button_3)
        callback_button_4 = types.InlineKeyboardButton(text="Минск, Брест, Витебск, Гомель",
                                                       callback_data="Минск, Брест, Витебск, Гомель")
        keyboard_gorod.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'В каких городах есть наши офисы?',
                         reply_markup=keyboard_gorod)
    if call.data == "Минск, Брест, Витебск, Гомель":
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз!) '
                                               'Чтобы ответить правильно на вопрос, '
                                               'прочти историю "Почему мы называемся SalesTelecom?"')
        time.sleep(1)
        keyboard_gorod = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Минск, Гродно, Витебск, Смоленск",
                                                       callback_data="Минск, Гродно, Витебск, Смоленск")
        keyboard_gorod.add(callback_button_1)
        callback_button_2 = types.InlineKeyboardButton(text="Витебск, Москва, Смоленск, Гомель",
                                                       callback_data="Витебск, Москва, Смоленск, Гомель")
        keyboard_gorod.add(callback_button_2)
        callback_button_3 = types.InlineKeyboardButton(text="Минск, Витебск, Гомель, Смоленск",
                                                       callback_data="Минск, Витебск, Гомель, Смоленск")
        keyboard_gorod.add(callback_button_3)
        callback_button_4 = types.InlineKeyboardButton(text="Минск, Брест, Витебск, Гомель",
                                                       callback_data="Минск, Брест, Витебск, Гомель")
        keyboard_gorod.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'В каких городах есть наши офисы?',
                         reply_markup=keyboard_gorod)
    if call.data == "Минск, Витебск, Гомель, Смоленск":
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKhZF_0YmEnXT1Q108ZUdxWyX46PxZdAAIHAAM7YCQUJkqsOvTwt2keBA')
        bot.send_message(call.message.chat.id, 'Поздравляю ты справился со вторым вопросом ☺')
        time.sleep(3)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Посмотреть видео",
                                                url="https://drive.google.com/file/d/12irl_"
                                                    "nKdJbvzW4Q598U7SIFqlVoXMxm8/view?usp=sharing")
        keyboard.add(url_button)
        bot.send_message(call.message.chat.id, 'Предлагаю тебе лично познакомиться с частичкой '
                                               'нашей эффективной команды SalesTelecom', reply_markup=keyboard)
        # ДЕНЬ2
        time.sleep(15)
        bot.send_message(call.message.chat.id, 'Сделаем остановку. Встретимся завтра. Приятно было поболтать')
        time.sleep(1)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKhYV_0Yle0SGPn-KNgu80t-ElkeLPHAAICAAM7YCQUoMJLdBA-ZR4eBA')

        time.sleep(10)
        bot.send_message(call.message.chat.id,
                         'Привет, соскучился? '
                         '\nЯ очень) '
                         'Предлагаю поиграть: я тебе интересные вопросы, '
                         'ты мне захватывающие ответы. Ну что, готов?', reply_markup=const.markup_menu_day2_start)
    # ДЕНЬ2

bot.polling()