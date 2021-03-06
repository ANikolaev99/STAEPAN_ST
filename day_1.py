import telebot
import const
from telebot import types
import time
import tg_analytic

TOKEN = '************************'  # полученный у @BotFather
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])  # Первый запуск
def start_message(message):
    tg_analytic.statistics(message.chat.first_name, message.text)
    bot.send_message(message.chat.id, 'Привет, ' + message.chat.first_name +
                     '! Я - Степан – главный помоган! 💪. Твой персональный проводник в мир контакт-центра '
                     'Сэйлз Телеком! Готов к путешествию?',
                     reply_markup=const.markup_menu_start)


@bot.message_handler(content_types=['text'])
def send_message_day1(message):
    if message.text == "Привет":
        tg_analytic.statistics(message.chat.first_name, message.text)
        bot.send_message(message.chat.id, 'Привет, ' + message.chat.first_name +
                         '! Я - Степан – главный помоган! 💪. Твой персональный проводник в мир контакт-центра '
                         'Сэйлз Телеком! Готов к путешествию?',
                         reply_markup=const.markup_menu_start)
    elif message.text == "привет":
        tg_analytic.statistics(message.chat.first_name, message.text)
        bot.send_message(message.chat.id, 'Привет, ' + message.chat.first_name +
                         '! Я - Степан – главный помоган! 💪. Твой персональный проводник в мир контакт-центра '
                         'Сэйлз Телеком! Готов к путешествию?',
                         reply_markup=const.markup_menu_start)
    elif message.text == "Да":
        tg_analytic.statistics(message.chat.first_name, message.text)
        bot.send_message(message.chat.id,
                         'Здорово!'
                         '\nТы когда-нибудь работал в контактном центре?', reply_markup=const.markup_menu_rabota)
    elif message.text == "Нет":
        tg_analytic.statistics(message.chat.first_name, message.text)
        bot.send_message(message.chat.id,
                         'Как жаль, ну давай просто пообщаемся,'
                         '\nТы когда-нибудь работал в контактном центре?', reply_markup=const.markup_menu_rabota)
    elif message.text == "Работал":
        tg_analytic.statistics(message.chat.first_name, message.text)
        bot.send_message(message.chat.id,
                         'Круто! ' + message.chat.first_name +
                         ', давай я сейчас немного расскажу о нашей компании. Готов?',
                         reply_markup=const.markup_menu_ST)
    elif message.text == "Не работал":
        tg_analytic.statistics(message.chat.first_name, message.text)
        bot.send_message(message.chat.id,
                         'Ничего страшного, у нас дружный коллектив, мы тебя всему научим! 😎 '
                         'А сейчас я хочу немного рассказать о нашей компании. Готов?',
                         reply_markup=const.markup_menu_ST)
    elif message.text == "Готов":
        tg_analytic.statistics(message.chat.first_name, message.text)
        bot.send_message(message.chat.id, 'Отлично! Если официально представляться, то мы: _SalesTelecom._',
                         parse_mode="Markdown")
        bot.send_photo(message.chat.id,
                       'https://drive.google.com/file/d/1kC7ABmVe45HGhAoAem9jSeVPqPRQQoVk/view?usp=sharing')
        time.sleep(2)
        bot.send_message(message.chat.id, '_Sales_ – продажи, _Telecom_ - посредством телекоммуникации 🧑‍💻'
                                          '\nЭто не значит, что мы занимаемся только продажами.'
                                          '\n'
                                          '\nМы говорим, что продажа происходит в каждом звонке, в каждом '
                                          'контакте 😏'
                                          '\nЛюбое наше общение – это своеобразная продажа: общаясь с друзьями, '
                                          'мы продаем свое мнение, общаясь с ребенком – идею что-то сделать и '
                                          'так далее.'
                                          '\nТак что и в проектах мы не просто консультируем абонентов, а продаем '
                                          'отношение к компании, желание стать клиентом или прийти в офис 🤗'
                                          '\n'
                                          '\n🎉 День рождения компании – 23 июля 2013 года🎉'
                                          '\n🥳 Да, нам уже 7 лет!🥳'
                                          '\n'
                                          '\nСейчас у нашей компании четыре площадки: '
                                          '\n✅ Минск'
                                          '\n✅ Гомель'
                                          '\n✅ Витебск'
                                          '\n✅ Смоленск'
                                          '\nМы смело можем называть себя международниками 😎 💪'
                                          '\n'
                                          '\nСовершенно случайно все офисы оказались в шаговой доступности от '
                                          'сети ресторанов McDonalds 🍔 🥤'
                                          '\nОпросы показали, что 18 наших коллег часто там обедают 🍟. Надеюсь, '
                                          'что они чередуют фастфуд и здоровую пищу 🥗', parse_mode="Markdown")
        time.sleep(15)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Посмотреть видео",
                                                url="https://drive.google.com/file/d/1jV-hFF9faiio-m8ylXz0Isqa"
                                                    "2NYjSIk8/view?usp=sharing")
        keyboard.add(url_button)
        bot.send_message(message.chat.id,
                         'А еще мы любим участвовать в конкурсах, и я покажу тебе ролик о том, как мы представляем '
                         'себе работу в КЦ 😇',
                         reply_markup=keyboard)
        time.sleep(15)
        bot.send_message(message.chat.id, 'А ты чем увлекаешься?')
    elif message.text == "Не готов":
        tg_analytic.statistics(message.chat.first_name, message.text)
        bot.send_message(message.chat.id,
                         'Ничего страшного 😉'
                         '\nУ нас есть аккаунт в инстаграм для сотрудников компании, там много интересной информации 😏'
                         ' Спроси у руководителя проекта, как нас найти в соц сетях 📳'
                         '\nЛибо отправь мне сообщение со словом "Готов", когда сможешь пообщаться.')

# ДЕНЬ 2
    elif message.text == "Перейти на второй уровень":
        tg_analytic.statistics(message.chat.first_name, message.text)
        time.sleep(1)
        bot.send_message(message.chat.id,
                         'Приветствую тебя на новом уровне 😎'
                         '\nПредлагаю поиграть: я тебе интересные вопросы - ты мне захватывающие ответы. '
                         'Ну что, готов?',
                         reply_markup=const.markup_menu_day2_start)
    elif message.text == "Да, поехали":
        tg_analytic.statistics(message.chat.first_name, message.text)
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI_DF-X-nQjiGUsJ9dtnsFDLDqNxujSAAIpAAPBnGAM8EupHr_Y33wbBA')
        time.sleep(1)
        bot.send_message(message.chat.id, 'Переходим к вопросам 😃')
        time.sleep(1)
        bot.send_message(message.chat.id, 'Давай разберем с тобой правила работы с клиентом')
        time.sleep(2)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="А", callback_data="А вопрос 1")
        callback_button_2 = types.InlineKeyboardButton(text="Б", callback_data="Б вопрос 1")
        callback_button_3 = types.InlineKeyboardButton(text="В", callback_data="В вопрос 1")
        callback_button_4 = types.InlineKeyboardButton(text="Г", callback_data="Г вопрос 1")
        keyboard_vopros1.add(callback_button_1, callback_button_2)
        keyboard_vopros1.add(callback_button_3, callback_button_4)
        bot.send_message(message.chat.id, 'Выберите правильный ответ:'
                                          '\nА) называем девушка, мужчина, молодой человек, женщина и т.д.'
                                          '\nБ) обращаемся на «Вы» обобщено, нет необходимости уточнять имя клиента'
                                          '\nВ) уточняем имя и обращаемся по полному имени, например, Валерий'
                                          '\nГ) если клиент сказал, что его зовут Саша, то так его и называем, '
                                          'не стоит переходить на Александр)',
                         reply_markup=keyboard_vopros1)
    elif message.text == "Нет, не совсем":
        tg_analytic.statistics(message.chat.first_name, message.text)
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAKhbV_0ZglqsgI_O4XNAxsi5vL0q9LIAAIlAAPBnGAMsZsU2SseitYeBA')
        time.sleep(1)
        bot.send_message(message.chat.id,
                         'Жаль, тогда давай перейдем к вопросам без подготовки. Ты справишься, я уверен!')
        time.sleep(2)
        bot.send_message(message.chat.id, 'Давай разберем с тобой правила работы с клиентом')
        time.sleep(2)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="А", callback_data="А вопрос 1")
        callback_button_2 = types.InlineKeyboardButton(text="Б", callback_data="Б вопрос 1")
        callback_button_3 = types.InlineKeyboardButton(text="В", callback_data="В вопрос 1")
        callback_button_4 = types.InlineKeyboardButton(text="Г", callback_data="Г вопрос 1")
        keyboard_vopros1.add(callback_button_1, callback_button_2)
        keyboard_vopros1.add(callback_button_3, callback_button_4)
        bot.send_message(message.chat.id, 'Выберите правильный ответ:'
                                          '\nА) называем девушка, мужчина, молодой человек, женщина и т.д.'
                                          '\nБ) обращаемся на «Вы» обобщено, нет необходимости уточнять имя клиента'
                                          '\nВ) уточняем имя и обращаемся по полному имени, например, Валерий'
                                          '\nГ) если клиент сказал, что его зовут Саша, то так его и называем, '
                                          'не стоит переходить на Александр)',
                         reply_markup=keyboard_vopros1)
    # ДЕНЬ 3
    elif message.text == "Перейти на третий уровень":
        tg_analytic.statistics(message.chat.first_name, message.text)
        time.sleep(1)
        bot.send_message(message.chat.id,
                         '🥳'
                         '\nДавай продолжим наше веселое времяпровождение. '
                         'Знаешь ли ты, что такое потребности?',
                         reply_markup=const.markup_menu_day3_start)
    elif message.text == "Да, конечно, знаю":
        tg_analytic.statistics(message.chat.first_name, message.text)
        bot.send_message(message.chat.id, 'Супер! Тогда приступим')
        time.sleep(2)
        bot.send_message(message.chat.id, '*Выявите, какой приоритетной потребностью руководствуется клиент: *'
                                          '*безопасности, привязанности, комфорта, престижа, новизны, экономии*',
                         parse_mode="Markdown")
        time.sleep(2)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data=" безопасность вопрос 1")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 1")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 1")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 1")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 1")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 1")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(message.chat.id, 'Подберите мне авто. '
                                          'Для девочки 2 лет, чтобы проездила как минимум 2-3 года, '
                                          'т.к. я не собираюсь платить такие большие деньги за маленький промежуток '
                                          'времени…'
                                          'Найдите мне самый бюджетный вариант…А есть у вас рассрочка?',
                         reply_markup=keyboard_vopros1)
    elif message.text == "Не уверен":
        tg_analytic.statistics(message.chat.first_name, message.text)
        bot.send_message(message.chat.id,
                         '_Потребность — вид функциональной или психологической нужды, или недостатка какого-либо _'
                         '_объекта, _'
                         '_субъекта, индивида, социальной группы, общества. Являясь внутренними возбудителями _'
                         '_активности, _'
                         '_потребности проявляются по-разному в зависимости от ситуации. _'
                         '_Потребности проявляются в виде эмоционально окрашенных желаний, _'
                         '_влечений, стремлений, а их удовлетворение — в виде оценочных эмоций. _'
                         '_Ярким примером может служить жажда — острое чувство потребности в воде, _'
                         '_возникающее при обеднении ею организма животного или при превышении в _'
                         '_крови нормальной концентрации минеральных и органических веществ._', parse_mode="Markdown")
        bot.send_photo(message.chat.id,
                       "https://drive.google.com/file/d/1ZK01EScVA53xxO_6vZ6C8sje5aq1mdUQ/view?usp=sharing")
        time.sleep(5)
        bot.send_message(message.chat.id, '*Выявите, какой приоритетной потребностью руководствуется клиент: *'
                                          '*безопасности, привязанности, комфорта, престижа, новизны, экономии*',
                         parse_mode="Markdown")
        time.sleep(2)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безовасность вопрос 1")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 1")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 1")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 1")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 1")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(message.chat.id, 'Подберите мне авто. '
                                          'Для девочки 2 лет, чтобы проездила как минимум 2-3 года, '
                                          'т.к. я не собираюсь платить такие большие деньги за маленький промежуток '
                                          'времени…'
                                          'Найдите мне самый бюджетный вариант…А есть у вас рассрочка?',
                         reply_markup=keyboard_vopros1)
    # ДЕНЬ 4
    elif message.text == "Перейти на четвертый уровень":
        tg_analytic.statistics(message.chat.first_name, message.text)
        time.sleep(1)
        bot.send_message(message.chat.id,
                         'Наше захватывающее путешествие подходит к концу, и именно '
                         'поэтому я подготовил для тебя самые интересные задания ☺ Поехали!')
        time.sleep(2)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б", callback_data="А, Б вопрос 1")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="В, Г", callback_data="В, Г вопрос 1")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А, Г", callback_data="А, Г вопрос 1")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б, В, Г", callback_data="Б, В, Г вопрос 1")
        keyboard_vopros1.add(btn_4)
        bot.send_message(message.chat.id, 'Как думаешь, какие инструменты необходимо использовать, '
                                          'когда клиент демонстрирует негативную эмоцию (агрессию, раздражение, '
                                          'разочарование, недоверие и т.д.)?'
                                          '\nА) сделать вид, что не заметил и продолжать задавать уточняющие '
                                          'вопросы '
                                          '\nБ) озвучить эмоцию и попросить клиента реагировать спокойнее'
                                          '\nВ) понимание: суть метода показать, что клиент имеет право на '
                                          'эмоцию, это нормально, особенно когда его ожидания не оправданы '
                                          '\nГ) сожаление: если клиенту доставлен дискомфорт',
                         reply_markup=keyboard_vopros1)

    elif message.text[:10] == 'статистика' or message.text[:10] == 'Cтатистика':
        st = message.text.split(' ')
        if 'txt' in st or 'тхт' in st:
            tg_analytic.analysis(st, message.chat.id)
            with open('%s.txt' % message.chat.id, 'r', encoding='UTF-8') as file:
                bot.send_document(message.chat.id, file)
            tg_analytic.remove(message.chat.id)
        else:
            messages = tg_analytic.analysis(st, message.chat.id)
            bot.send_message(message.chat.id, messages)
    else:
        tg_analytic.statistics(message.chat.first_name, message.text)
        bot.send_message(message.chat.id, 'Интересненько...😃 ')
        time.sleep(2)
        bot.send_message(message.chat.id, 'Слушай, ' + message.chat.first_name + ", чтобы тебе было полезно со "
                                                                                 "мной общаться, "
                                                                                 "давай определим, что получит активный и "
                                                                                 "заинтересованный участник 😃 "
                                                                                 "Тот, кто пройдет все 4 уровня, получит набор новичка 🎁")
        time.sleep(3)
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


@bot.callback_query_handler(func=lambda call: True)
def callback_worker_day1(call):
    # ДЕНЬ 1
    # Вопрос 1
    if call.data == "5 лет":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз! 🙂'
                                               '\n_Чтобы ответить правильно на вопрос, _'
                                               '_прочти историю "Почему мы называемся SalesTelecom?"_',
                         parse_mode="Markdown")
        time.sleep(2)
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
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз! 🙂'
                                               '\n_Чтобы ответить правильно на вопрос, _'
                                               '_прочти историю "Почему мы называемся SalesTelecom?"_',
                         parse_mode="Markdown")
        time.sleep(2)
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
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз! 🙂'
                                               '\n_Чтобы ответить правильно на вопрос, _'
                                               '_прочти историю "Почему мы называемся SalesTelecom?"_',
                         parse_mode="Markdown")
        time.sleep(2)
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
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKhVV_0Wpzb_9oGqtG3pWIqNv2nCH4CAAIEAAM7YCQUs6vrVG-V4aseBA')
        bot.send_message(call.message.chat.id, 'Поздравляю! Ты справился с первым вопросом 👍')
        time.sleep(2)
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
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз! 🙂'
                                               '\n_Чтобы ответить правильно на вопрос, _'
                                               '_прочти историю "Почему мы называемся SalesTelecom?"_',
                         parse_mode="Markdown")
        time.sleep(2)
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
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз! 🙂'
                                               '\n_Чтобы ответить правильно на вопрос, _'
                                               '_прочти историю "Почему мы называемся SalesTelecom?"_',
                         parse_mode="Markdown")
        time.sleep(2)
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
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно. Попробуй еще раз! 🙂'
                                               '\n_Чтобы ответить правильно на вопрос, _'
                                               '_прочти историю "Почему мы называемся SalesTelecom?"_',
                         parse_mode="Markdown")
        time.sleep(2)
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
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKhZF_0YmEnXT1Q108ZUdxWyX46PxZdAAIHAAM7YCQUJkqsOvTwt2keBA')
        bot.send_message(call.message.chat.id, 'Поздравляю ты справился со вторым вопросом ☺')
        time.sleep(2)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Посмотреть видео",
                                                url="https://drive.google.com/file/d/1yFW"
                                                    "w7NC6ONb26Z56_EIBc4HspbUKsqx0/view?usp=sharing")
        keyboard.add(url_button)
        bot.send_message(call.message.chat.id, 'Предлагаю тебе лично познакомиться с частичкой '
                                               'нашей эффективной команды _SalesTelecom_',
                         parse_mode="Markdown", reply_markup=keyboard)
        # ДЕНЬ2
        time.sleep(15)
        bot.send_message(call.message.chat.id, 'Поздравляю, ' + call.message.chat.first_name +
                         ', ты успешно прошел начальный уровень ✌'
                         '\nУверен, что и на следующем уровне тебя тоже '
                         'ждет успех 🙃')
        time.sleep(1)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAK5xWAJU2qAtZLqTJ48iU-dUGqRKOLuAAJYAwACz7vUDnSoodcl1REsHgQ',
                         reply_markup=const.markup_menu_poka_day1)

    # ДЕНЬ2
    # Вопрос 1
    if call.data == "А вопрос 1":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! Попытка засчитана.'
                                               '\nПопробуй еще раз 🙂')
        time.sleep(2)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="А", callback_data="А вопрос 1")
        callback_button_2 = types.InlineKeyboardButton(text="Б", callback_data="Б вопрос 1")
        callback_button_3 = types.InlineKeyboardButton(text="В", callback_data="В вопрос 1")
        callback_button_4 = types.InlineKeyboardButton(text="Г", callback_data="Г вопрос 1")
        keyboard_vopros1.add(callback_button_1, callback_button_2)
        keyboard_vopros1.add(callback_button_3, callback_button_4)
        bot.send_message(call.message.chat.id, 'Выберите правильный ответ:'
                                               '\nА) называем девушка, мужчина, молодой человек, женщина и т.д.'
                                               '\nБ) обращаемся на «Вы» обобщено, нет необходимости уточнять имя'
                                               'клиента'
                                               '\nВ) уточняем имя и обращаемся по полному имени, например, Валерий'
                                               '\nГ) если клиент сказал, что его зовут Саша, то так его и называем,'
                                               'не стоит переходить на Александр)',
                         reply_markup=keyboard_vopros1)
    if call.data == "Б вопрос 1":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! Попытка засчитана.'
                                               '\nПопробуй еще раз 🙂')
        time.sleep(2)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="А", callback_data="А вопрос 1")
        callback_button_2 = types.InlineKeyboardButton(text="Б", callback_data="Б вопрос 1")
        callback_button_3 = types.InlineKeyboardButton(text="В", callback_data="В вопрос 1")
        callback_button_4 = types.InlineKeyboardButton(text="Г", callback_data="Г вопрос 1")
        keyboard_vopros1.add(callback_button_1, callback_button_2)
        keyboard_vopros1.add(callback_button_3, callback_button_4)
        bot.send_message(call.message.chat.id, 'Выберите правильный ответ:'
                                               '\nА) называем девушка, мужчина, молодой человек, женщина и т.д.'
                                               '\nБ) обращаемся на «Вы» обобщено, нет необходимости уточнять имя'
                                               'клиента'
                                               '\nВ) уточняем имя и обращаемся по полному имени, например, Валерий'
                                               '\nГ) если клиент сказал, что его зовут Саша, то так его и называем,'
                                               'не стоит переходить на Александр)',
                         reply_markup=keyboard_vopros1)
    if call.data == "Г вопрос 1":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! Попытка засчитана.'
                                               '\nПопробуй еще раз 🙂')
        time.sleep(2)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="А", callback_data="А вопрос 1")
        callback_button_2 = types.InlineKeyboardButton(text="Б", callback_data="Б вопрос 1")
        callback_button_3 = types.InlineKeyboardButton(text="В", callback_data="В вопрос 1")
        callback_button_4 = types.InlineKeyboardButton(text="Г", callback_data="Г вопрос 1")
        keyboard_vopros1.add(callback_button_1, callback_button_2)
        keyboard_vopros1.add(callback_button_3, callback_button_4)
        bot.send_message(call.message.chat.id, 'Выберите правильный ответ:'
                                               '\nА) называем девушка, мужчина, молодой человек, женщина и т.д.'
                                               '\nБ) обращаемся на «Вы» обобщено, нет необходимости уточнять имя'
                                               'клиента'
                                               '\nВ) уточняем имя и обращаемся по полному имени, например, Валерий'
                                               '\nГ) если клиент сказал, что его зовут Саша, то так его и называем,'
                                               'не стоит переходить на Александр)',
                         reply_markup=keyboard_vopros1)
    if call.data == "В вопрос 1":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKheF_0aXOYUJK_yskv_0jZ_EIRKcpdAAIsAAPBnGAMsN15duPYIJUeBA')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Верно!')
        time.sleep(2)
        keyboard_vopros2 = types.InlineKeyboardMarkup()
        callback_button_no = types.InlineKeyboardButton(text="Все, кроме Г", callback_data="кроме Г вопрос 2")
        callback_button_doljen = types.InlineKeyboardButton(text="Все, кроме В", callback_data="кроме В вопрос 2")
        callback_button_poprobyem = types.InlineKeyboardButton(text="А, Б", callback_data="АБ вопрос 2")
        callback_button_help = types.InlineKeyboardButton(text="А, В", callback_data="АВ вопрос 2")
        keyboard_vopros2.add(callback_button_no)
        keyboard_vopros2.add(callback_button_doljen)
        keyboard_vopros2.add(callback_button_poprobyem)
        keyboard_vopros2.add(callback_button_help)
        bot.send_message(call.message.chat.id, 'Какие слова/фразы нельзя говорить клиенту:'
                                               '\nА) Нет'
                                               '\nБ) Вы должны'
                                               '\nВ) Мы попробуем'
                                               '\nГ) Чем я могу вам помочь',
                         reply_markup=keyboard_vopros2)
    # ДЕНЬ2
    # Вопрос 2
    if call.data == "кроме В вопрос 2":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\n_🚫 «Нет» – никогда не говорите этого слова. _'
                                               '_Бывают ситуации, когда вы действительно не можете предоставить _'
                                               '_определенный продукт или услугу, _'
                                               '_но, как правило, решить вопрос можно, предложив альтернативу, '
                                               'другой вариант._'
                                               '\n'
                                               '\n_🚫 «Вы должны» - помогайте клиентам, а не указывайте им, _'
                                               '_что и как делать. Они же пришли за помощью, а не за указаниями._'
                                               '\n'
                                               '\n_🚫 «Мы попробуем» - клиентов волнуют не усилия, а результаты. _'
                                               '_Лучше расскажите о том, что вы готовы сделать для клиента, _'
                                               '_не создавая обстановки неопределенности._', parse_mode="Markdown")
        time.sleep(5)
        keyboard_vopros2 = types.InlineKeyboardMarkup()
        callback_button_no = types.InlineKeyboardButton(text="Все, кроме Г", callback_data="кроме Г вопрос 2")
        callback_button_doljen = types.InlineKeyboardButton(text="Все, кроме В", callback_data="кроме В вопрос 2")
        callback_button_poprobyem = types.InlineKeyboardButton(text="А, Б", callback_data="АБ вопрос 2")
        callback_button_help = types.InlineKeyboardButton(text="А, В", callback_data="АВ вопрос 2")
        keyboard_vopros2.add(callback_button_no)
        keyboard_vopros2.add(callback_button_doljen)
        keyboard_vopros2.add(callback_button_poprobyem)
        keyboard_vopros2.add(callback_button_help)
        bot.send_message(call.message.chat.id, 'Попробуй еще раз!😊'
                                               '\nКакие слова/фразы нельзя говорить клиенту:'
                                               '\nА) Нет'
                                               '\nБ) Вы должны'
                                               '\nВ) Мы попробуем'
                                               '\nГ) Чем я могу вам помочь',
                         reply_markup=keyboard_vopros2)
    if call.data == "АБ вопрос 2":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\n_🚫 «Нет» – никогда не говорите этого слова._'
                                               '_Бывают ситуации, когда вы действительно не можете предоставить _'
                                               '_определенный продукт или услугу, _'
                                               '_но, как правило, решить вопрос можно, предложив альтернативу, '
                                               'другой вариант._'
                                               '\n'
                                               '\n_🚫 «Вы должны» - помогайте клиентам, а не указывайте им, _'
                                               '_что и как делать. Они же пришли за помощью, а не за указаниями._'
                                               '\n'
                                               '\n_🚫 «Мы попробуем» - клиентов волнуют не усилия, а результаты. _'
                                               '_Лучше расскажите о том, что вы готовы сделать для клиента, _'
                                               '_не создавая обстановки неопределенности._', parse_mode="Markdown")
        time.sleep(5)
        keyboard_vopros2 = types.InlineKeyboardMarkup()
        callback_button_no = types.InlineKeyboardButton(text="Все, кроме Г", callback_data="кроме Г вопрос 2")
        callback_button_doljen = types.InlineKeyboardButton(text="Все, кроме В", callback_data="кроме В вопрос 2")
        callback_button_poprobyem = types.InlineKeyboardButton(text="А, Б", callback_data="АБ вопрос 2")
        callback_button_help = types.InlineKeyboardButton(text="А, В", callback_data="АВ вопрос 2")
        keyboard_vopros2.add(callback_button_no)
        keyboard_vopros2.add(callback_button_doljen)
        keyboard_vopros2.add(callback_button_poprobyem)
        keyboard_vopros2.add(callback_button_help)
        bot.send_message(call.message.chat.id, 'Попробуй еще раз!😊'
                                               '\nКакие слова/фразы нельзя говорить клиенту:'
                                               '\nА) Нет'
                                               '\nБ) Вы должны'
                                               '\nВ) Мы попробуем'
                                               '\nГ) Чем я могу вам помочь',
                         reply_markup=keyboard_vopros2)
    if call.data == "АВ вопрос 2":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\n_🚫 «Нет» – никогда не говорите этого слова._'
                                               '_Бывают ситуации, когда вы действительно не можете предоставить _'
                                               '_определенный продукт или услугу, _'
                                               '_но, как правило, решить вопрос можно, предложив альтернативу, '
                                               'другой вариант._'
                                               '\n'
                                               '\n_🚫 «Вы должны» - помогайте клиентам, а не указывайте им, _'
                                               '_что и как делать. Они же пришли за помощью, а не за указаниями._'
                                               '\n'
                                               '\n_🚫 «Мы попробуем» - клиентов волнуют не усилия, а результаты. _'
                                               '_Лучше расскажите о том, что вы готовы сделать для клиента, _'
                                               '_не создавая обстановки неопределенности._', parse_mode="Markdown")
        time.sleep(5)
        keyboard_vopros2 = types.InlineKeyboardMarkup()
        callback_button_no = types.InlineKeyboardButton(text="Все, кроме Г", callback_data="кроме Г вопрос 2")
        callback_button_doljen = types.InlineKeyboardButton(text="Все, кроме В", callback_data="кроме В вопрос 2")
        callback_button_poprobyem = types.InlineKeyboardButton(text="А, Б", callback_data="АБ вопрос 2")
        callback_button_help = types.InlineKeyboardButton(text="А, В", callback_data="АВ вопрос 2")
        keyboard_vopros2.add(callback_button_no)
        keyboard_vopros2.add(callback_button_doljen)
        keyboard_vopros2.add(callback_button_poprobyem)
        keyboard_vopros2.add(callback_button_help)
        bot.send_message(call.message.chat.id, 'Попробуй еще раз!😊'
                                               '\nКакие слова/фразы нельзя говорить клиенту:'
                                               '\nА) Нет'
                                               '\nБ) Вы должны'
                                               '\nВ) Мы попробуем'
                                               '\nГ) Чем я могу вам помочь',
                         reply_markup=keyboard_vopros2)
    if call.data == "кроме Г вопрос 2":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKhg1_0a_SX4J9FVDgej0Z9sFuV0PedAAIxAAPBnGAMxg4yoItadaUeBA')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Верно! 🦉'
                                               '\n_🚫 «Нет» – никогда не говорите этого слова._'
                                               '_Бывают ситуации, когда вы действительно не можете предоставить _'
                                               '_определенный продукт или услугу, _'
                                               '_но, как правило, решить вопрос можно, предложив альтернативу, '
                                               'другой вариант. _'
                                               '\n'
                                               '\n_🚫 «Вы должны» - помогайте клиентам, а не указывайте им, _'
                                               '_что и как делать. Они же пришли за помощью, а не за указаниями._'
                                               '\n'
                                               '\n_🚫 «Мы попробуем» - клиентов волнуют не усилия, а результаты. _'
                                               '_Лучше расскажите о том, что вы готовы сделать для клиента, _'
                                               '_не создавая обстановки неопределенности._', parse_mode="Markdown")
        time.sleep(10)
        keyboard_vopros3 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 3")
        callback_button_2 = types.InlineKeyboardButton(text="Все, кроме Ж", callback_data="кроме Ж вопрос 3")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Е", callback_data="кроме Е вопрос 3")
        callback_button_4 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="АВГДЕЖ вопрос 3")
        keyboard_vopros3.add(callback_button_1)
        keyboard_vopros3.add(callback_button_2)
        keyboard_vopros3.add(callback_button_3)
        keyboard_vopros3.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'При разговоре с клиентом недопустимо:'
                                               '\nА) ворчание'
                                               '\nБ) усталость'
                                               '\nВ) безразличие'
                                               '\nГ) грубость в интонации'
                                               '\nД) разговор на повышенных тонах'
                                               '\nЕ) делать замечания, учить хорошим манерам'
                                               '\nЖ) избегать уменьшительно-ласкательных суффиксов: документик',
                         reply_markup=keyboard_vopros3)
    # ДЕНЬ2
    # Вопрос 3
    if call.data == "все вопрос 3":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Ты старался, это похвально.'
                                               '\nПопробуй еще раз')
        time.sleep(3)
        keyboard_vopros3 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 3")
        callback_button_2 = types.InlineKeyboardButton(text="Все, кроме Ж", callback_data="кроме Ж вопрос 3")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Е", callback_data="кроме Е вопрос 3")
        callback_button_4 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="АВГДЕЖ вопрос 3")
        keyboard_vopros3.add(callback_button_1)
        keyboard_vopros3.add(callback_button_2)
        keyboard_vopros3.add(callback_button_3)
        keyboard_vopros3.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'При разговоре с клиентом недопустимо:'
                                               '\nА) ворчание'
                                               '\nБ) усталость'
                                               '\nВ) безразличие'
                                               '\nГ) грубость в интонации'
                                               '\nД) разговор на повышенных тонах'
                                               '\nЕ) делать замечания, учить хорошим манерам'
                                               '\nЖ) избегать уменьшительно-ласкательных суффиксов: документик',
                         reply_markup=keyboard_vopros3)
    if call.data == "кроме Е вопрос 3":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Ты старался, это похвально.'
                                               '\nПопробуй еще раз')
        time.sleep(3)
        keyboard_vopros3 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 3")
        callback_button_2 = types.InlineKeyboardButton(text="Все, кроме Ж", callback_data="кроме Ж вопрос 3")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Е", callback_data="кроме Е вопрос 3")
        callback_button_4 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="АВГДЕЖ вопрос 3")
        keyboard_vopros3.add(callback_button_1)
        keyboard_vopros3.add(callback_button_2)
        keyboard_vopros3.add(callback_button_3)
        keyboard_vopros3.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'При разговоре с клиентом недопустимо:'
                                               '\nА) ворчание'
                                               '\nБ) усталость'
                                               '\nВ) безразличие'
                                               '\nГ) грубость в интонации'
                                               '\nД) разговор на повышенных тонах'
                                               '\nЕ) делать замечания, учить хорошим манерам'
                                               '\nЖ) избегать уменьшительно-ласкательных суффиксов: документик',
                         reply_markup=keyboard_vopros3)
    if call.data == "АВГДЕЖ вопрос 3":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Ты старался, это похвально.'
                                               '\nПопробуй еще раз')
        time.sleep(3)
        keyboard_vopros3 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 3")
        callback_button_2 = types.InlineKeyboardButton(text="Все, кроме Ж", callback_data="кроме Ж вопрос 3")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Е", callback_data="кроме Е вопрос 3")
        callback_button_4 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="АВГДЕЖ вопрос 3")
        keyboard_vopros3.add(callback_button_1)
        keyboard_vopros3.add(callback_button_2)
        keyboard_vopros3.add(callback_button_3)
        keyboard_vopros3.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'При разговоре с клиентом недопустимо:'
                                               '\nА) ворчание'
                                               '\nБ) усталость'
                                               '\nВ) безразличие'
                                               '\nГ) грубость в интонации'
                                               '\nД) разговор на повышенных тонах'
                                               '\nЕ) делать замечания, учить хорошим манерам'
                                               '\nЖ) избегать уменьшительно-ласкательных суффиксов: документик',
                         reply_markup=keyboard_vopros3)
    if call.data == "кроме Ж вопрос 3":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKhjF_0dxv0Q2OE3tpY-zrIFLj7efdUAAIpAAPBnGAM8EupHr_Y33weBA')
        bot.send_message(call.message.chat.id, 'Верно!')
        time.sleep(3)
        keyboard_vopros4 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="кроме Б вопрос 4")
        callback_button_2 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 4")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Е", callback_data="кроме Е вопрос 4")
        callback_button_4 = types.InlineKeyboardButton(text="А, Б, В, Е", callback_data="АБВЕ вопрос 4")
        keyboard_vopros4.add(callback_button_1)
        keyboard_vopros4.add(callback_button_2)
        keyboard_vopros4.add(callback_button_3)
        keyboard_vopros4.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'Каким нужно быть оператору при общении с клиентом:'
                                               '\nА) доброжелательным'
                                               '\nБ) участливым, заботливым'
                                               '\nВ) уверенным'
                                               '\nГ) спокойным'
                                               '\nД) компетентным'
                                               '\nЕ) инициативным',
                         reply_markup=keyboard_vopros4)
    # ДЕНЬ2
    # Вопрос 4
    if call.data == "кроме Б вопрос 4":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\n_⚠ Доброжелательность позволяет видеть не проблему, _'
                                               '_а ее решение. Через полгода клиент может и не вспомнить о _'
                                               '_предмете вашего разговора, _'
                                               '_но он будет помнить, каким приятным был ваш разговор._'
                                               '\n'
                                               '\n_⚠ Участие, забота позволяют не оставить осадка непонимания. _'
                                               '_При общении человек не только получает информацию, _'
                                               '_но и заполняет свою эмоциональную память._'
                                               '\n'
                                               '\n_⚠ Уверенность в общении и речи и компетентность позволяет _'
                                               '_клиенту почувствовать, что его вопрос будет решен, _'
                                               '_что он обратился по адресу._'
                                               '\n'
                                               '\n_⚠ Спокойствие в ответ на негативные эмоции клиента помогает _'
                                               '_«отрезвить» его, перейти из эмоций в логическое мышление, _'
                                               '_перейти к конструктивному диалогу._'
                                               '\n'
                                               '\n_⚠ Инициатива (задавать вопросы, вести диалог) определяет _'
                                               '_оператора, как эксперта, который знает: что сказать дальше, _'
                                               '_какие вопросы _'
                                               '_задать, какой вариант решения предложить._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros4 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="кроме Б вопрос 4")
        callback_button_2 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 4")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Е", callback_data="кроме Е вопрос 4")
        callback_button_4 = types.InlineKeyboardButton(text="А, Б, В, Е", callback_data="АБВЕ вопрос 4")
        keyboard_vopros4.add(callback_button_1)
        keyboard_vopros4.add(callback_button_2)
        keyboard_vopros4.add(callback_button_3)
        keyboard_vopros4.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'Попробуй еще раз'
                                               '\nКаким нужно быть оператору при общении с клиентом:'
                                               '\nА) доброжелательным'
                                               '\nБ) участливым, заботливым'
                                               '\nВ) уверенным'
                                               '\nГ) спокойным'
                                               '\nД) компетентным'
                                               '\nЕ) инициативным',
                         reply_markup=keyboard_vopros4)
    if call.data == "кроме Е вопрос 4":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\n_⚠ Доброжелательность позволяет видеть не проблему, _'
                                               '_а ее решение. Через полгода клиент может и не вспомнить о _'
                                               '_предмете вашего разговора, _'
                                               '_но он будет помнить, каким приятным был ваш разговор._'
                                               '\n'
                                               '\n_⚠ Участие, забота позволяют не оставить осадка непонимания. _'
                                               '_При общении человек не только получает информацию, _'
                                               '_но и заполняет свою эмоциональную память._'
                                               '\n'
                                               '\n_⚠ Уверенность в общении и речи и компетентность позволяет _'
                                               '_клиенту почувствовать, что его вопрос будет решен, _'
                                               '_что он обратился по адресу._'
                                               '\n'
                                               '\n_⚠ Спокойствие в ответ на негативные эмоции клиента помогает _'
                                               '_«отрезвить» его, перейти из эмоций в логическое мышление, _'
                                               '_перейти к конструктивному диалогу._'
                                               '\n'
                                               '\n_⚠ Инициатива (задавать вопросы, вести диалог) определяет _'
                                               '_оператора, как эксперта, который знает: что сказать дальше, _'
                                               '_какие вопросы _'
                                               '_задать, какой вариант решения предложить._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros4 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="кроме Б вопрос 4")
        callback_button_2 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 4")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Е", callback_data="кроме Е вопрос 4")
        callback_button_4 = types.InlineKeyboardButton(text="А, Б, В, Е", callback_data="АБВЕ вопрос 4")
        keyboard_vopros4.add(callback_button_1)
        keyboard_vopros4.add(callback_button_2)
        keyboard_vopros4.add(callback_button_3)
        keyboard_vopros4.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'Попробуй еще раз'
                                               '\nКаким нужно быть оператору при общении с клиентом:'
                                               '\nА) доброжелательным'
                                               '\nБ) участливым, заботливым'
                                               '\nВ) уверенным'
                                               '\nГ) спокойным'
                                               '\nД) компетентным'
                                               '\nЕ) инициативным',
                         reply_markup=keyboard_vopros4)
    if call.data == "АБВЕ вопрос 4":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\n_⚠ Доброжелательность позволяет видеть не проблему, _'
                                               '_а ее решение. Через полгода клиент может и не вспомнить о _'
                                               '_предмете вашего разговора, _'
                                               '_но он будет помнить, каким приятным был ваш разговор._'
                                               '\n'
                                               '\n_⚠ Участие, забота позволяют не оставить осадка непонимания. _'
                                               '_При общении человек не только получает информацию, _'
                                               '_но и заполняет свою эмоциональную память._'
                                               '\n'
                                               '\n_⚠ Уверенность в общении и речи и компетентность позволяет _'
                                               '_клиенту почувствовать, что его вопрос будет решен, _'
                                               '_что он обратился по адресу._'
                                               '\n'
                                               '\n_⚠ Спокойствие в ответ на негативные эмоции клиента помогает _'
                                               '_«отрезвить» его, перейти из эмоций в логическое мышление, _'
                                               '_перейти к конструктивному диалогу._'
                                               '\n'
                                               '\n_⚠ Инициатива (задавать вопросы, вести диалог) определяет _'
                                               '_оператора, как эксперта, который знает: что сказать дальше, _'
                                               '_какие вопросы _'
                                               '_задать, какой вариант решения предложить._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros4 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="кроме Б вопрос 4")
        callback_button_2 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 4")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Е", callback_data="кроме Е вопрос 4")
        callback_button_4 = types.InlineKeyboardButton(text="А, Б, В, Е", callback_data="АБВЕ вопрос 4")
        keyboard_vopros4.add(callback_button_1)
        keyboard_vopros4.add(callback_button_2)
        keyboard_vopros4.add(callback_button_3)
        keyboard_vopros4.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'Попробуй еще раз'
                                               '\nКаким нужно быть оператору при общении с клиентом:'
                                               '\nА) доброжелательным'
                                               '\nБ) участливым, заботливым'
                                               '\nВ) уверенным'
                                               '\nГ) спокойным'
                                               '\nД) компетентным'
                                               '\nЕ) инициативным',
                         reply_markup=keyboard_vopros4)
    if call.data == "все вопрос 4":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKheF_0aXOYUJK_yskv_0jZ_EIRKcpdAAIsAAPBnGAMsN15duPYIJUeBA')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Верно! 🦉'
                                               '\n_⚠ Доброжелательность позволяет видеть не проблему, _'
                                               '_а ее решение. Через полгода клиент может и не вспомнить о _'
                                               '_предмете вашего разговора, _'
                                               '_но он будет помнить, каким приятным был ваш разговор._'
                                               '\n'
                                               '\n_⚠ Участие, забота позволяют не оставить осадка непонимания. _'
                                               '_При общении человек не только получает информацию, _'
                                               '_но и заполняет свою эмоциональную память._'
                                               '\n'
                                               '\n_⚠ Уверенность в общении и речи и компетентность позволяет _'
                                               '_клиенту почувствовать, что его вопрос будет решен, _'
                                               '_что он обратился по адресу._'
                                               '\n'
                                               '\n_⚠ Спокойствие в ответ на негативные эмоции клиента помогает _'
                                               '_«отрезвить» его, перейти из эмоций в логическое мышление, _'
                                               '_перейти к конструктивному диалогу._'
                                               '\n'
                                               '\n_⚠ Инициатива (задавать вопросы, вести диалог) определяет _'
                                               '_оператора, как эксперта, который знает: что сказать дальше, _'
                                               '_какие вопросы _'
                                               '_задать, какой вариант решения предложить._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros5 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="А", callback_data="А вопрос 5")
        callback_button_2 = types.InlineKeyboardButton(text="Б", callback_data="Б вопрос 5")
        keyboard_vopros5.add(callback_button_1, callback_button_2)
        bot.send_message(call.message.chat.id, 'Нужно ли определять эмоциональное состояние клиента?'
                                               '\nА) да, на этом этапе важно понять, готов ли клиент говорить о '
                                               'деле, '
                                               'излагает ли он связано свой вопрос, адресованный к вам. '
                                               'Или же он находится на эмоциональном уровне, '
                                               'и ему в первую очередь важно состояние эмпатии, проявление участия'
                                               '\nБ) нет, не стоит обращать внимание на эмоции, '
                                               'сам сохраняю спокойствие и делаю вид, что не замечаю эмоции '
                                               'клиента, чтобы не вызвать дополнительный негатив',
                         reply_markup=keyboard_vopros5)
    # ДЕНЬ2
    # Вопрос 5
    if call.data == "Б вопрос 5":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Попытка засчитана, правда ответ неверный. '
                                               'Ну ничего, попробуй еще раз 🙂')
        time.sleep(1)
        keyboard_vopros5 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="А", callback_data="А вопрос 5")
        callback_button_2 = types.InlineKeyboardButton(text="Б", callback_data="Б вопрос 5")
        keyboard_vopros5.add(callback_button_1, callback_button_2)
        bot.send_message(call.message.chat.id, 'Нужно ли определять эмоциональное состояние клиента?'
                                               '\nА) да, на этом этапе важно понять, готов ли клиент говорить о '
                                               'деле, '
                                               'излагает ли он связано свой вопрос, адресованный к вам. '
                                               'Или же он находится на эмоциональном уровне, '
                                               'и ему в первую очередь важно состояние эмпатии, проявление участия'
                                               '\nБ) нет, не стоит обращать внимание на эмоции, '
                                               'сам сохраняю спокойствие и делаю вид, что не замечаю эмоции '
                                               'клиента, чтобы не вызвать дополнительный негатив',
                         reply_markup=keyboard_vopros5)
    if call.data == "А вопрос 5":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKhg1_0a_SX4J9FVDgej0Z9sFuV0PedAAIxAAPBnGAMxg4yoItadaUeBA')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Верно!')
        time.sleep(3)
        keyboard_vopros6 = types.InlineKeyboardMarkup()
        callback_button_izvinenie = types.InlineKeyboardButton(text="принести извинение",
                                                               callback_data="принести извинение")
        callback_button_ponimanie = types.InlineKeyboardButton(text="выразить понимание",
                                                               callback_data="выразить понимание")
        callback_button_vislyshat = types.InlineKeyboardButton(text="выслушать клиента до конца, не перебивая",
                                                               callback_data="выслушать клиента")
        callback_button_reshenie = types.InlineKeyboardButton(text="предложить варианты решения вопроса",
                                                              callback_data="предложить варианты")
        keyboard_vopros6.add(callback_button_izvinenie)
        keyboard_vopros6.add(callback_button_ponimanie)
        keyboard_vopros6.add(callback_button_vislyshat)
        keyboard_vopros6.add(callback_button_reshenie)
        bot.send_message(call.message.chat.id, 'При возникновении конфликта, '
                                               'при высказывании претензии со стороны клиента '
                                               'что в первую очередь нужно сделать?', reply_markup=keyboard_vopros6)
    # ДЕНЬ2
    # Вопрос 6
    if call.data == "принести извинение":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Попытка засчитана, правда ответ неверный. '
                                               'Ну ничего, попробуй еще раз 🙂')
        time.sleep(2)
        keyboard_vopros6 = types.InlineKeyboardMarkup()
        callback_button_izvinenie = types.InlineKeyboardButton(text="принести извинение",
                                                               callback_data="принести извинение")
        callback_button_ponimanie = types.InlineKeyboardButton(text="выразить понимание",
                                                               callback_data="выразить понимание")
        callback_button_vislyshat = types.InlineKeyboardButton(text="выслушать клиента до конца, не перебивая",
                                                               callback_data="выслушать клиента")
        callback_button_reshenie = types.InlineKeyboardButton(text="предложить варианты решения вопроса",
                                                              callback_data="предложить варианты")
        keyboard_vopros6.add(callback_button_izvinenie)
        keyboard_vopros6.add(callback_button_ponimanie)
        keyboard_vopros6.add(callback_button_vislyshat)
        keyboard_vopros6.add(callback_button_reshenie)
        bot.send_message(call.message.chat.id, 'При возникновении конфликта, '
                                               'при высказывании претензии со стороны клиента '
                                               'что в первую очередь нужно сделать?',
                         reply_markup=keyboard_vopros6)
    if call.data == "выразить понимание":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Попытка засчитана, правда ответ неверный. '
                                               'Ну ничего, попробуй еще раз 🙂')
        time.sleep(2)
        keyboard_vopros6 = types.InlineKeyboardMarkup()
        callback_button_izvinenie = types.InlineKeyboardButton(text="принести извинение",
                                                               callback_data="принести извинение")
        callback_button_ponimanie = types.InlineKeyboardButton(text="выразить понимание",
                                                               callback_data="выразить понимание")
        callback_button_vislyshat = types.InlineKeyboardButton(text="выслушать клиента до конца, не перебивая",
                                                               callback_data="выслушать клиента")
        callback_button_reshenie = types.InlineKeyboardButton(text="предложить варианты решения вопроса",
                                                              callback_data="предложить варианты")
        keyboard_vopros6.add(callback_button_izvinenie)
        keyboard_vopros6.add(callback_button_ponimanie)
        keyboard_vopros6.add(callback_button_vislyshat)
        keyboard_vopros6.add(callback_button_reshenie)
        bot.send_message(call.message.chat.id, 'При возникновении конфликта, '
                                               'при высказывании претензии со стороны клиента '
                                               'что в первую очередь нужно сделать?',
                         reply_markup=keyboard_vopros6)
    if call.data == "предложить варианты":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Попытка засчитана, правда ответ неверный. '
                                               'Ну ничего, попробуй еще раз 🙂')
        time.sleep(2)
        keyboard_vopros6 = types.InlineKeyboardMarkup()
        callback_button_izvinenie = types.InlineKeyboardButton(text="принести извинение",
                                                               callback_data="принести извинение")
        callback_button_ponimanie = types.InlineKeyboardButton(text="выразить понимание",
                                                               callback_data="выразить понимание")
        callback_button_vislyshat = types.InlineKeyboardButton(text="выслушать клиента до конца, не перебивая",
                                                               callback_data="выслушать клиента")
        callback_button_reshenie = types.InlineKeyboardButton(text="предложить варианты решения вопроса",
                                                              callback_data="предложить варианты")
        keyboard_vopros6.add(callback_button_izvinenie)
        keyboard_vopros6.add(callback_button_ponimanie)
        keyboard_vopros6.add(callback_button_vislyshat)
        keyboard_vopros6.add(callback_button_reshenie)
        bot.send_message(call.message.chat.id, 'При возникновении конфликта, '
                                               'при высказывании претензии со стороны клиента '
                                               'что в первую очередь нужно сделать?',
                         reply_markup=keyboard_vopros6)
    if call.data == "выслушать клиента":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKhjF_0dxv0Q2OE3tpY-zrIFLj7efdUAAIpAAPBnGAM8EupHr_Y33weBA')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Верно!')
        time.sleep(3)
        keyboard_vopros7 = types.InlineKeyboardMarkup()
        callback_button_blagodary = types.InlineKeyboardButton(text="благодарю за", callback_data="благодарю за")
        callback_button_ne_bespokoites = types.InlineKeyboardButton(text="не беспокойтесь",
                                                                    callback_data="не беспокойтесь")
        callback_button_viyasny = types.InlineKeyboardButton(text="я все выясню", callback_data="я все выясню")
        callback_button_virazhenie = types.InlineKeyboardButton(text="я неточно выразился",
                                                                callback_data="я неточно выразился")
        keyboard_vopros7.add(callback_button_blagodary)
        keyboard_vopros7.add(callback_button_ne_bespokoites)
        keyboard_vopros7.add(callback_button_viyasny)
        keyboard_vopros7.add(callback_button_virazhenie)
        bot.send_message(call.message.chat.id, 'Какую фразу не стоит использовать в диалоге с клиентом',
                         reply_markup=keyboard_vopros7)
    # ДЕНЬ2
    # Вопрос 7
    if call.data == "благодарю за":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Попытка засчитана, правда ответ неверный. '
                                               'Ну ничего, попробуй еще раз 🙂')
        time.sleep(2)
        keyboard_vopros7 = types.InlineKeyboardMarkup()
        callback_button_blagodary = types.InlineKeyboardButton(text="благодарю за", callback_data="благодарю за")
        callback_button_ne_bespokoites = types.InlineKeyboardButton(text="не беспокойтесь",
                                                                    callback_data="не беспокойтесь")
        callback_button_viyasny = types.InlineKeyboardButton(text="я все выясню", callback_data="я все выясню")
        callback_button_virazhenie = types.InlineKeyboardButton(text="я неточно выразился",
                                                                callback_data="я неточно выразился")
        keyboard_vopros7.add(callback_button_blagodary)
        keyboard_vopros7.add(callback_button_ne_bespokoites)
        keyboard_vopros7.add(callback_button_viyasny)
        keyboard_vopros7.add(callback_button_virazhenie)
        bot.send_message(call.message.chat.id, 'Какую фразу не стоит использовать в диалоге с клиентом',
                         reply_markup=keyboard_vopros7)
    if call.data == "я все выясню":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Попытка засчитана, правда ответ неверный. '
                                               'Ну ничего, попробуй еще раз 🙂')
        time.sleep(2)
        keyboard_vopros7 = types.InlineKeyboardMarkup()
        callback_button_blagodary = types.InlineKeyboardButton(text="благодарю за", callback_data="благодарю за")
        callback_button_ne_bespokoites = types.InlineKeyboardButton(text="не беспокойтесь",
                                                                    callback_data="не беспокойтесь")
        callback_button_viyasny = types.InlineKeyboardButton(text="я все выясню", callback_data="я все выясню")
        callback_button_virazhenie = types.InlineKeyboardButton(text="я неточно выразился",
                                                                callback_data="я неточно выразился")
        keyboard_vopros7.add(callback_button_blagodary)
        keyboard_vopros7.add(callback_button_ne_bespokoites)
        keyboard_vopros7.add(callback_button_viyasny)
        keyboard_vopros7.add(callback_button_virazhenie)
        bot.send_message(call.message.chat.id, 'Какую фразу не стоит использовать в диалоге с клиентом',
                         reply_markup=keyboard_vopros7)
    if call.data == "я неточно выразился":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Попытка засчитана, правда ответ неверный. '
                                               'Ну ничего, попробуй еще раз 🙂')
        time.sleep(2)
        keyboard_vopros7 = types.InlineKeyboardMarkup()
        callback_button_blagodary = types.InlineKeyboardButton(text="благодарю за", callback_data="благодарю за")
        callback_button_ne_bespokoites = types.InlineKeyboardButton(text="не беспокойтесь",
                                                                    callback_data="не беспокойтесь")
        callback_button_viyasny = types.InlineKeyboardButton(text="я все выясню", callback_data="я все выясню")
        callback_button_virazhenie = types.InlineKeyboardButton(text="я неточно выразился",
                                                                callback_data="я неточно выразился")
        keyboard_vopros7.add(callback_button_blagodary)
        keyboard_vopros7.add(callback_button_ne_bespokoites)
        keyboard_vopros7.add(callback_button_viyasny)
        keyboard_vopros7.add(callback_button_virazhenie)
        bot.send_message(call.message.chat.id, 'Какую фразу не стоит использовать в диалоге с клиентом',
                         reply_markup=keyboard_vopros7)
    if call.data == "не беспокойтесь":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKyaWACoTbx1MgG8wABryiHEg0_V8PkIgACQAADUomRIzVcuj961kKJHgQ')
        bot.send_message(call.message.chat.id, 'Верно! 🦉'
                                               '\n_Следует заменить на «положитесь на меня», _'
                                               '_слово «беспокойство» нежелательно употреблять в диалоге с клиентом._',
                         parse_mode="Markdown")
        time.sleep(3)
        keyboard_vopros8 = types.InlineKeyboardMarkup()
        callback_button_sdelaete = types.InlineKeyboardButton(text="если вы это сделаете",
                                                              callback_data="если вы это сделаете")
        callback_button_hotite = types.InlineKeyboardButton(text="что вы хотите",
                                                            callback_data="что вы хотите")
        callback_button_minuta = types.InlineKeyboardButton(text="я на минуточку",
                                                            callback_data="я на минуточку")
        callback_button_vnimanie = types.InlineKeyboardButton(text="обращаю ваше внимание на то, что",
                                                              callback_data="обращаю ваше внимание на то, что")
        keyboard_vopros8.add(callback_button_sdelaete)
        keyboard_vopros8.add(callback_button_hotite)
        keyboard_vopros8.add(callback_button_minuta)
        keyboard_vopros8.add(callback_button_vnimanie)
        bot.send_message(call.message.chat.id, 'Какую фразу можно использовать в диалоге с клиентом',
                         reply_markup=keyboard_vopros8)
    # ДЕНЬ2
    # Вопрос 8
    if call.data == "если вы это сделаете":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Попытка засчитана, правда ответ неверный. '
                                               'Ну ничего, попробуй еще раз 🙂')
        time.sleep(2)
        keyboard_vopros8 = types.InlineKeyboardMarkup()
        callback_button_sdelaete = types.InlineKeyboardButton(text="если вы это сделаете",
                                                              callback_data="если вы это сделаете")
        callback_button_hotite = types.InlineKeyboardButton(text="что вы хотите",
                                                            callback_data="что вы хотите")
        callback_button_minuta = types.InlineKeyboardButton(text="я на минуточку",
                                                            callback_data="я на минуточку")
        callback_button_vnimanie = types.InlineKeyboardButton(text="обращаю ваше внимание на то, что",
                                                              callback_data="обращаю ваше внимание на то, что")
        keyboard_vopros8.add(callback_button_sdelaete)
        keyboard_vopros8.add(callback_button_hotite)
        keyboard_vopros8.add(callback_button_minuta)
        keyboard_vopros8.add(callback_button_vnimanie)
        bot.send_message(call.message.chat.id, 'Какую фразу можно использовать в диалоге с клиентом',
                         reply_markup=keyboard_vopros8)
    if call.data == "что вы хотите":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Попытка засчитана, правда ответ неверный. '
                                               'Ну ничего, попробуй еще раз 🙂')
        time.sleep(2)
        keyboard_vopros8 = types.InlineKeyboardMarkup()
        callback_button_sdelaete = types.InlineKeyboardButton(text="если вы это сделаете",
                                                              callback_data="если вы это сделаете")
        callback_button_hotite = types.InlineKeyboardButton(text="что вы хотите",
                                                            callback_data="что вы хотите")
        callback_button_minuta = types.InlineKeyboardButton(text="я на минуточку",
                                                            callback_data="я на минуточку")
        callback_button_vnimanie = types.InlineKeyboardButton(text="обращаю ваше внимание на то, что",
                                                              callback_data="обращаю ваше внимание на то, что")
        keyboard_vopros8.add(callback_button_sdelaete)
        keyboard_vopros8.add(callback_button_hotite)
        keyboard_vopros8.add(callback_button_minuta)
        keyboard_vopros8.add(callback_button_vnimanie)
        bot.send_message(call.message.chat.id, 'Какую фразу можно использовать в диалоге с клиентом',
                         reply_markup=keyboard_vopros8)
    if call.data == "я на минуточку":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Попытка засчитана, правда ответ неверный. '
                                               'Ну ничего, попробуй еще раз 🙂')
        time.sleep(2)
        keyboard_vopros8 = types.InlineKeyboardMarkup()
        callback_button_sdelaete = types.InlineKeyboardButton(text="если вы это сделаете",
                                                              callback_data="если вы это сделаете")
        callback_button_hotite = types.InlineKeyboardButton(text="что вы хотите",
                                                            callback_data="что вы хотите")
        callback_button_minuta = types.InlineKeyboardButton(text="я на минуточку",
                                                            callback_data="я на минуточку")
        callback_button_vnimanie = types.InlineKeyboardButton(text="обращаю ваше внимание на то, что",
                                                              callback_data="обращаю ваше внимание на то, что")
        keyboard_vopros8.add(callback_button_sdelaete)
        keyboard_vopros8.add(callback_button_hotite)
        keyboard_vopros8.add(callback_button_minuta)
        keyboard_vopros8.add(callback_button_vnimanie)
        bot.send_message(call.message.chat.id, 'Какую фразу можно использовать в диалоге с клиентом',
                         reply_markup=keyboard_vopros8)
    if call.data == "обращаю ваше внимание на то, что":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKydWACodQYvIcGaBIpNhOTCtAC0KGLAAL0AwACRxVoCVCTOd91YktlHgQ')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Верно!')
        time.sleep(3)
        keyboard_vopros9 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 9")
        callback_button_2 = types.InlineKeyboardButton(text="Все, кроме В", callback_data="кроме В вопрос 9")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Г", callback_data="кроме Г вопрос 9")
        callback_button_4 = types.InlineKeyboardButton(text="А, Г", callback_data="АГ вопрос 9")
        keyboard_vopros9.add(callback_button_1)
        keyboard_vopros9.add(callback_button_2)
        keyboard_vopros9.add(callback_button_3)
        keyboard_vopros9.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'Какие слова-раздражители нельзя употреблять в диалоге с клиентом:'
                                               '\nА) проблема'
                                               '\nБ) ошибка'
                                               '\nВ) дело в том, что'
                                               '\nГ) две минуты времени',
                         reply_markup=keyboard_vopros9)
    # ДЕНЬ2
    # Вопрос 9
    if call.data == "все вопрос 9":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\n_🚫 "Проблема" - необходимо заменить на вопрос/решение/совет/_'
                                               '_ситуация, _'
                                               '_т.к. у клиента могло и не быть проблем при обращении к нам, но после _'
                                               '_этого слова он обязательно об этом задумается: _'
                                               '_"ну если профессионал говорит о том, что у меня проблема, _'
                                               '_то все точно плохо..._"'
                                               '\n'
                                               '\n_🚫 "Ошибка" - лучше не употреблять, особенно в сторону клиента, _'
                                               '_"это ваша ошибка", т.к. это точно приведет к конфликту, никому не _'
                                               '_понравится, если ему скажут, что он сделал что-то не так. _'
                                               '_Нужно аккуратно объяснить следует поступить, не делая акцент на том, _'
                                               '_что он сам виноват. Если слово ошибка употребляется по отношению _'
                                               '_к оператору -  "я ошибся", то необходимо заменить на "да, _'
                                               '_действительно, мной была предоставлена неполная/некорректная _'
                                               '_консультация, прошу прощения". Это поможет не столкнуться с _'
                                               '_ситуацией, когда клиент почувствует вашу "позицию снизу" и решит_'
                                               '_ "нападать"._'
                                               '\n'
                                               '\n_🚫 "Дело в том, что" - звучит как оправдание, даже если это и _'
                                               '_не так._',
                         parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros9 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 9")
        callback_button_2 = types.InlineKeyboardButton(text="Все, кроме В", callback_data="кроме В вопрос 9")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Г", callback_data="кроме Г вопрос 9")
        callback_button_4 = types.InlineKeyboardButton(text="А, Г", callback_data="АГ вопрос 9")
        keyboard_vopros9.add(callback_button_1)
        keyboard_vopros9.add(callback_button_2)
        keyboard_vopros9.add(callback_button_3)
        keyboard_vopros9.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'Какие слова-раздражители нельзя употреблять в диалоге с клиентом:'
                                               '\nА) проблема'
                                               '\nБ) ошибка'
                                               '\nВ) дело в том, что'
                                               '\nГ) две минуты времени',
                         reply_markup=keyboard_vopros9)
    if call.data == "кроме В вопрос 9":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\n_🚫 "Проблема" - необходимо заменить на вопрос/решение/совет/_'
                                               '_ситуация, _'
                                               '_т.к. у клиента могло и не быть проблем при обращении к нам, но после _'
                                               '_этого слова он обязательно об этом задумается: _'
                                               '_"ну если профессионал говорит о том, что у меня проблема, _'
                                               '_то все точно плохо..._"'
                                               '\n'
                                               '\n_🚫 "Ошибка" - лучше не употреблять, особенно в сторону клиента, _'
                                               '_"это ваша ошибка", т.к. это точно приведет к конфликту, никому не _'
                                               '_понравится, если ему скажут, что он сделал что-то не так. _'
                                               '_Нужно аккуратно объяснить как следует поступить, не делая акцент_'
                                               '_ на том, _'
                                               '_что он сам виноват. Если слово ошибка употребляется по отношению _'
                                               '_к оператору - "я ошибся", то необходимо заменить на "да, _'
                                               '_действительно, мной была предоставлена неполная/некорректная _'
                                               '_консультация, прошу прощения". Это поможет не столкнуться с _'
                                               '_ситуацией, когда клиент почувствует вашу "позицию снизу" и решит_'
                                               '_ "нападать"._'
                                               '\n'
                                               '\n_🚫 "Дело в том, что" - звучит как оправдание, даже если это и _'
                                               '_не так._',
                         parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros9 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 9")
        callback_button_2 = types.InlineKeyboardButton(text="Все, кроме В", callback_data="кроме В вопрос 9")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Г", callback_data="кроме Г вопрос 9")
        callback_button_4 = types.InlineKeyboardButton(text="А, Г", callback_data="АГ вопрос 9")
        keyboard_vopros9.add(callback_button_1)
        keyboard_vopros9.add(callback_button_2)
        keyboard_vopros9.add(callback_button_3)
        keyboard_vopros9.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'Какие слова-раздражители нельзя употреблять в диалоге с клиентом:'
                                               '\nА) проблема'
                                               '\nБ) ошибка'
                                               '\nВ) дело в том, что'
                                               '\nГ) две минуты времени',
                         reply_markup=keyboard_vopros9)
    if call.data == "АГ вопрос 9":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\n_🚫 "Проблема" - необходимо заменить на вопрос/решение/совет/_'
                                               '_ситуация, _'
                                               '_т.к. у клиента могло и не быть проблем при обращении к нам, но после _'
                                               '_этого слова он обязательно об этом задумается: _'
                                               '_"ну если профессионал говорит о том, что у меня проблема, _'
                                               '_то все точно плохо..._"'
                                               '\n'
                                               '\n_🚫 "Ошибка" - лучше не употреблять, особенно в сторону клиента, _'
                                               '_"это ваша ошибка", т.к. это точно приведет к конфликту, никому не _'
                                               '_понравится, если ему скажут, что он сделал что-то не так. _'
                                               '_Нужно аккуратно объяснить как следует поступить, не делая акцент _'
                                               '_на том, _'
                                               '_что он сам виноват. Если слово ошибка употребляется по отношению _'
                                               '_к оператору - "я ошибся", то необходимо заменить на "да, _'
                                               '_действительно, мной была предоставлена неполная/некорректная _'
                                               '_консультация, прошу прощения". Это поможет не столкнуться с _'
                                               '_ситуацией, когда клиент почувствует вашу "позицию снизу" и решит_'
                                               '_ "нападать"._'
                                               '\n'
                                               '\n_🚫 "Дело в том, что" - звучит как оправдание, даже если это и _'
                                               '_не так._',
                         parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros9 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 9")
        callback_button_2 = types.InlineKeyboardButton(text="Все, кроме В", callback_data="кроме В вопрос 9")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Г", callback_data="кроме Г вопрос 9")
        callback_button_4 = types.InlineKeyboardButton(text="А, Г", callback_data="АГ вопрос 9")
        keyboard_vopros9.add(callback_button_1)
        keyboard_vopros9.add(callback_button_2)
        keyboard_vopros9.add(callback_button_3)
        keyboard_vopros9.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'Какие слова-раздражители нельзя употреблять в диалоге с клиентом:'
                                               '\nА) проблема'
                                               '\nБ) ошибка'
                                               '\nВ) дело в том, что'
                                               '\nГ) две минуты времени',
                         reply_markup=keyboard_vopros9)
    if call.data == "кроме Г вопрос 9":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKyeGACofwCp8G0G5zLXNClwoHCQhZVAAI_AANSiZEjPlJrH8XRKWseBA')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Верно! 🦉'
                                               '\n_🚫 "Проблема" - необходимо заменить на вопрос/решение/совет/_'
                                               '_ситуация, _'
                                               '_т.к. у клиента могло и не быть проблем при обращении к нам, но после _'
                                               '_этого слова он обязательно об этом задумается: _'
                                               '_"ну если профессионал говорит о том, что у меня проблема, _'
                                               '_то все точно плохо..._"'
                                               '\n'
                                               '\n_🚫 "Ошибка" - лучше не употреблять, особенно в сторону клиента, _'
                                               '_"это ваша ошибка", т.к. это точно приведет к конфликту, никому не _'
                                               '_понравится, если ему скажут, что он сделал что-то не так. _'
                                               '_Нужно аккуратно объяснить как следует поступить, не делая акцент _'
                                               '_на том, _'
                                               '_что он сам виноват. Если слово ошибка употребляется по отношению _'
                                               '_к оператору - "я ошибся", то необходимо заменить на "да, _'
                                               '_действительно, мной была предоставлена неполная/некорректная _'
                                               '_консультация, прошу прощения". Это поможет не столкнуться с _'
                                               '_ситуацией, когда клиент почувствует вашу "позицию снизу" и решит_'
                                               '_ "нападать"._'
                                               '\n'
                                               '\n_🚫 "Дело в том, что" - звучит как оправдание, даже если это и _'
                                               '_не так._',
                         parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros10 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 10")
        callback_button_2 = types.InlineKeyboardButton(text="Все, кроме Г", callback_data="кроме Г вопрос 10")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="кроме Б вопрос 10")
        callback_button_4 = types.InlineKeyboardButton(text="А, В", callback_data="АВ вопрос 10")
        keyboard_vopros10.add(callback_button_1)
        keyboard_vopros10.add(callback_button_2)
        keyboard_vopros10.add(callback_button_3)
        keyboard_vopros10.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'По каким параметрам необходимо подстраиваться к клиенту:'
                                               '\nА) темп'
                                               '\nБ) громкость'
                                               '\nВ) уровень понимания'
                                               '\nГ) по грамотности',
                         reply_markup=keyboard_vopros10)
    # ДЕНЬ2
    # Вопрос 10
    if call.data == "все вопрос 10":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\n_В психологии есть такое понятие, как подстройка. _'
                                               '_Если два собеседника ведут себя похожим образом, _'
                                               '_эта сходность поведения сближает их и делает _'
                                               '_контакт между ними более прочным_'
                                               '\n'
                                               '\n_Подстраивайтесь, как минимум, по таким параметрам, как темп и _'
                                               '_громкость, _'
                                               '_если хотите, чтобы вы воспринимались как «свой», а не как «чужой»._',
                         parse_mode="Markdown")
        time.sleep(3)
        bot.send_message(call.message.chat.id, 'Попробуй еще раз 🙂')
        time.sleep(1)
        keyboard_vopros10 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 10")
        callback_button_2 = types.InlineKeyboardButton(text="Все, кроме Г", callback_data="кроме Г вопрос 10")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="кроме Б вопрос 10")
        callback_button_4 = types.InlineKeyboardButton(text="А, В", callback_data="АВ вопрос 10")
        keyboard_vopros10.add(callback_button_1)
        keyboard_vopros10.add(callback_button_2)
        keyboard_vopros10.add(callback_button_3)
        keyboard_vopros10.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'По каким параметрам необходимо подстраиваться к клиенту:'
                                               '\nА) темп'
                                               '\nБ) громкость'
                                               '\nВ) уровень понимания'
                                               '\nГ) по грамотности',
                         reply_markup=keyboard_vopros10)
    if call.data == "кроме Б вопрос 10":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\n_В психологии есть такое понятие, как подстройка. _'
                                               '_Если два собеседника ведут себя похожим образом, _'
                                               '_эта сходность поведения сближает их и делает _'
                                               '_контакт между ними более прочным_'
                                               '\n'
                                               '\n_Подстраивайтесь, как минимум, по таким параметрам, как темп и _'
                                               '_громкость, _'
                                               '_если хотите, чтобы вы воспринимались как «свой», а не как «чужой»._',
                         parse_mode="Markdown")
        time.sleep(3)
        bot.send_message(call.message.chat.id, 'Попробуй еще раз 🙂')
        time.sleep(1)
        keyboard_vopros10 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 10")
        callback_button_2 = types.InlineKeyboardButton(text="Все, кроме Г", callback_data="кроме Г вопрос 10")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="кроме Б вопрос 10")
        callback_button_4 = types.InlineKeyboardButton(text="А, В", callback_data="АВ вопрос 10")
        keyboard_vopros10.add(callback_button_1)
        keyboard_vopros10.add(callback_button_2)
        keyboard_vopros10.add(callback_button_3)
        keyboard_vopros10.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'По каким параметрам необходимо подстраиваться к клиенту:'
                                               '\nА) темп'
                                               '\nБ) громкость'
                                               '\nВ) уровень понимания'
                                               '\nГ) по грамотности',
                         reply_markup=keyboard_vopros10)
    if call.data == "АВ вопрос 10":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\n_В психологии есть такое понятие, как подстройка. _'
                                               '_Если два собеседника ведут себя похожим образом, _'
                                               '_эта сходность поведения сближает их и делает _'
                                               '_контакт между ними более прочным_'
                                               '\n'
                                               '\n_Подстраивайтесь, как минимум, по таким параметрам, как темп и _'
                                               '_громкость, _'
                                               '_если хотите, чтобы вы воспринимались как «свой», а не как «чужой»._',
                         parse_mode="Markdown")
        time.sleep(3)
        bot.send_message(call.message.chat.id, 'Попробуй еще раз 🙂')
        time.sleep(1)
        keyboard_vopros10 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="все вопрос 10")
        callback_button_2 = types.InlineKeyboardButton(text="Все, кроме Г", callback_data="кроме Г вопрос 10")
        callback_button_3 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="кроме Б вопрос 10")
        callback_button_4 = types.InlineKeyboardButton(text="А, В", callback_data="АВ вопрос 10")
        keyboard_vopros10.add(callback_button_1)
        keyboard_vopros10.add(callback_button_2)
        keyboard_vopros10.add(callback_button_3)
        keyboard_vopros10.add(callback_button_4)
        bot.send_message(call.message.chat.id, 'По каким параметрам необходимо подстраиваться к клиенту:'
                                               '\nА) темп'
                                               '\nБ) громкость'
                                               '\nВ) уровень понимания'
                                               '\nГ) по грамотности',
                         reply_markup=keyboard_vopros10)
    if call.data == "кроме Г вопрос 10":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKhg1_0a_SX4J9FVDgej0Z9sFuV0PedAAIxAAPBnGAMxg4yoItadaUeBA')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Верно! 🦉'
                                               '\n_В психологии есть такое понятие, как подстройка. _'
                                               '_Если два собеседника ведут себя похожим образом, _'
                                               '_эта сходность поведения сближает их и делает _'
                                               '_контакт между ними более прочным_'
                                               '\n'
                                               '\n_Подстраивайтесь, как минимум, по таким параметрам, как темп и _'
                                               '_громкость, _'
                                               '_если хотите, чтобы вы воспринимались как «свой», а не как «чужой»._',
                         parse_mode="Markdown")
        time.sleep(10)
        keyboard_vopros11a = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="КвАртал", callback_data="КвАртал")
        callback_button_v2 = types.InlineKeyboardButton(text="квартАл", callback_data="квартАл")
        keyboard_vopros11a.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Выбери слова, с правильно поставленным ударением',
                         reply_markup=keyboard_vopros11a)
    # ДЕНЬ2
    # Вопрос 11
    if call.data == "КвАртал":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11b = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="катАлог", callback_data="катАлог")
        callback_button_v2 = types.InlineKeyboardButton(text="каталОг", callback_data="каталОг")
        keyboard_vopros11b.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Не верно',
                         reply_markup=keyboard_vopros11b)
    if call.data == "квартАл":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11b = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="катАлог", callback_data="катАлог")
        callback_button_v2 = types.InlineKeyboardButton(text="каталОг", callback_data="каталОг")
        keyboard_vopros11b.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Верно',
                         reply_markup=keyboard_vopros11b)
    if call.data == "катАлог":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11c = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="звОнит", callback_data="звОнит")
        callback_button_v2 = types.InlineKeyboardButton(text="звонИт", callback_data="звонИт")
        keyboard_vopros11c.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Не верно',
                         reply_markup=keyboard_vopros11c)
    if call.data == "каталОг":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11c = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="звОнит", callback_data="звОнит")
        callback_button_v2 = types.InlineKeyboardButton(text="звонИт", callback_data="звонИт")
        keyboard_vopros11c.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Верно',
                         reply_markup=keyboard_vopros11c)
    if call.data == "звОнит":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11d = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="докУмент", callback_data="докУмент")
        callback_button_v2 = types.InlineKeyboardButton(text="докумЕнт", callback_data="докумЕнт")
        keyboard_vopros11d.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Не верно',
                         reply_markup=keyboard_vopros11d)
    if call.data == "звонИт":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11d = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="докУмент", callback_data="докУмент")
        callback_button_v2 = types.InlineKeyboardButton(text="докумЕнт", callback_data="докумЕнт")
        keyboard_vopros11d.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Верно',
                         reply_markup=keyboard_vopros11d)
    if call.data == "докУмент":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11e = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="дОговор", callback_data="дОговор")
        callback_button_v2 = types.InlineKeyboardButton(text="договОр", callback_data="договОр")
        keyboard_vopros11e.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Не верно',
                         reply_markup=keyboard_vopros11e)
    if call.data == "докумЕнт":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11e = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="дОговор", callback_data="дОговор")
        callback_button_v2 = types.InlineKeyboardButton(text="договОр", callback_data="договОр")
        keyboard_vopros11e.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Верно',
                         reply_markup=keyboard_vopros11e)
    if call.data == "дОговор":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11f = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="нАчался", callback_data="нАчался")
        callback_button_v2 = types.InlineKeyboardButton(text="началсЯ", callback_data="началсЯ")
        keyboard_vopros11f.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Не верно',
                         reply_markup=keyboard_vopros11f)
    if call.data == "договОр":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11f = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="нАчался", callback_data="нАчался")
        callback_button_v2 = types.InlineKeyboardButton(text="началсЯ", callback_data="началсЯ")
        keyboard_vopros11f.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Верно',
                         reply_markup=keyboard_vopros11f)
    if call.data == "нАчался":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11g = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="срЕдства", callback_data="срЕдства")
        callback_button_v2 = types.InlineKeyboardButton(text="средствА", callback_data="средствА")
        keyboard_vopros11g.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Не верно',
                         reply_markup=keyboard_vopros11g)
    if call.data == "началсЯ":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11g = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="срЕдства", callback_data="срЕдства")
        callback_button_v2 = types.InlineKeyboardButton(text="средствА", callback_data="средствА")
        keyboard_vopros11g.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Верно',
                         reply_markup=keyboard_vopros11g)
    if call.data == "срЕдства":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11h = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="Эксперт", callback_data="Эксперт")
        callback_button_v2 = types.InlineKeyboardButton(text="экспЕрт", callback_data="экспЕрт")
        keyboard_vopros11h.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Верно',
                         reply_markup=keyboard_vopros11h)
    if call.data == "средствА":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11h = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="Эксперт", callback_data="Эксперт")
        callback_button_v2 = types.InlineKeyboardButton(text="экспЕрт", callback_data="экспЕрт")
        keyboard_vopros11h.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'не верно',
                         reply_markup=keyboard_vopros11h)
    if call.data == "Эксперт":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11i = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="пОняла", callback_data="пОняла")
        callback_button_v2 = types.InlineKeyboardButton(text="понялА", callback_data="понялА")
        keyboard_vopros11i.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Не верно',
                         reply_markup=keyboard_vopros11i)
    if call.data == "экспЕрт":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_vopros11i = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="пОняла", callback_data="пОняла")
        callback_button_v2 = types.InlineKeyboardButton(text="понялА", callback_data="понялА")
        keyboard_vopros11i.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Верно',
                         reply_markup=keyboard_vopros11i)
    # ДЕНЬ2
    # Вопрос 12
    if call.data == "пОняла":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно')
        time.sleep(1)
        keyboard_vopros12 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="выступил", callback_data="выступил")
        callback_button_v2 = types.InlineKeyboardButton(text="выступила", callback_data="выступила")
        keyboard_vopros12.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Выберите вариант с правильным согласованием:'
                                               '\nМенеджер модного салона Ирина Васильевна…по радио.',
                         reply_markup=keyboard_vopros12)
    if call.data == "понялА":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Верно')
        time.sleep(1)
        keyboard_vopros12 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="выступил", callback_data="выступил")
        callback_button_v2 = types.InlineKeyboardButton(text="выступила", callback_data="выступила")
        keyboard_vopros12.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Выберите вариант с правильным согласованием:'
                                               '\nМенеджер модного салона Ирина Васильевна…по радио.',
                         reply_markup=keyboard_vopros12)
    # ДЕНЬ2
    # Вопрос 13
    if call.data == "выступил":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно 🦉'
                                               '\n_В разговорной речи частотно использование смыслового (а не грамматического) _'
                                               '_согласования при существительных мужского рода, характеризующих лиц женского пола. _'
                                               '_Врач пришла; Профессор сказала; Директор школы уволилась._'
                                               '_Однако в официальной речи замена грамматического согласования смысловым не допускается, _'
                                               '_за исключением тех случаев, когда такое существительное имеет при себе имя собственное._'
                                               '_ В таких конструкциях определение и сказуемое согласуются с ближайшим существительным. _'
                                               '_Например: Опытный врач Петрова внимательна к больным. _'
                                               '_Определение-причастие всегда согласуется с именем собственным._',
                         parse_mode="Markdown")
        time.sleep(7)
        keyboard_vopros13 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="хороший", callback_data="хороший")
        callback_button_v2 = types.InlineKeyboardButton(text="хорошая", callback_data="хорошая")
        keyboard_vopros13.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Выберите вариант с правильным согласованием:'
                                               '\nВ нашей фирме работает…программист Елена Субботина.',
                         reply_markup=keyboard_vopros13)
    if call.data == "выступила":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Верно')
        time.sleep(1)
        keyboard_vopros13 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="хороший", callback_data="хороший")
        callback_button_v2 = types.InlineKeyboardButton(text="хорошая", callback_data="хорошая")
        keyboard_vopros13.add(callback_button_v1, callback_button_v2)
        bot.send_message(call.message.chat.id, 'Выберите вариант с правильным согласованием:'
                                               '\nВ нашей фирме работает…программист Елена Субботина.',
                         reply_markup=keyboard_vopros13)
    # ДЕНЬ2
    # Вопрос 14
    if call.data == "хорошая":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно 🦉'
                                               '\n_В разговорной речи частотно использование смыслового (а не грамматического) _'
                                               '_согласования при существительных мужского рода, характеризующих лиц женского пола._'
                                               '_Врач пришла; Профессор сказала; Директор школы уволилась._'
                                               '_Однако в официальной речи замена грамматического согласования смысловым не допускается, _'
                                               '_за исключением тех случаев, когда такое существительное имеет при себе имя собственное._'
                                               '_ В таких конструкциях определение и сказуемое согласуются с ближайшим существительным. _'
                                               '_Например: Опытный врач Петрова внимательна к больным. _'
                                               '_Определение-причастие всегда согласуется с именем собственным._',
                         parse_mode="Markdown")
        time.sleep(10)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Посмотреть видео",
                                                url="https://drive.google.com/file/d/1T4uATW-04zxK"
                                                    "J95NlzJcjCbGDd6pyRsc/view?usp=sharing")
        keyboard.add(url_button)
        bot.send_message(call.message.chat.id,
                         'Посмотри небольшое шуточное видео про разные стили общения с клиентом 😊',
                         reply_markup=keyboard)
        time.sleep(10)
        bot.send_message(call.message.chat.id,
                         'Ты двигаешься в правильном направлении, мы с тобой прошли уже немалый путь ☺'
                         '\nОтветь еще на 3 моих вопроса и уровень будет пройден.')
        time.sleep(2)
        keyboard_vopros14 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="0", callback_data="0age")
        callback_button_v2 = types.InlineKeyboardButton(text="1", callback_data="1age")
        callback_button_v3 = types.InlineKeyboardButton(text="60+", callback_data="60age")
        callback_button_v4 = types.InlineKeyboardButton(text="70+", callback_data="70age")
        callback_button_v5 = types.InlineKeyboardButton(text="80+", callback_data="80age")
        keyboard_vopros14.add(callback_button_v1)
        keyboard_vopros14.add(callback_button_v2)
        keyboard_vopros14.add(callback_button_v3)
        keyboard_vopros14.add(callback_button_v4)
        keyboard_vopros14.add(callback_button_v5)
        bot.send_message(call.message.chat.id, 'Сколько у среднестатистического человека дней рождения?',
                         reply_markup=keyboard_vopros14)
    if call.data == "хороший":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKyaWACoTbx1MgG8wABryiHEg0_V8PkIgACQAADUomRIzVcuj961kKJHgQ')
        bot.send_message(call.message.chat.id, 'Верно!')
        time.sleep(3)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Посмотреть видео",
                                                url="https://drive.google.com/file/d/1T4uATW-04zxK"
                                                    "J95NlzJcjCbGDd6pyRsc/view?usp=sharing")
        keyboard.add(url_button)
        bot.send_message(call.message.chat.id,
                         'А теперь посмотри небольшое шуточное видео про разные стили общения с клиентом 😊',
                         reply_markup=keyboard)
        time.sleep(10)
        bot.send_message(call.message.chat.id,
                         'Ты двигаешься в правильном направлении, мы с тобой прошли уже немалый путь ☺'
                         '\nОтветь еще на 3 моих вопроса и уровень будет пройден.')
        time.sleep(2)
        keyboard_vopros14 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="0", callback_data="0age")
        callback_button_v2 = types.InlineKeyboardButton(text="1", callback_data="1age")
        callback_button_v3 = types.InlineKeyboardButton(text="60+", callback_data="60age")
        callback_button_v4 = types.InlineKeyboardButton(text="70+", callback_data="70age")
        callback_button_v5 = types.InlineKeyboardButton(text="80+", callback_data="80age")
        keyboard_vopros14.add(callback_button_v1)
        keyboard_vopros14.add(callback_button_v2)
        keyboard_vopros14.add(callback_button_v3)
        keyboard_vopros14.add(callback_button_v4)
        keyboard_vopros14.add(callback_button_v5)
        bot.send_message(call.message.chat.id, 'Сколько у среднестатистического человека дней рождения? ',
                         reply_markup=keyboard_vopros14)
    # ДЕНЬ2
    # Вопрос 15
    if call.data == "0age":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_У каждого человека всего один день рождения..._',
                         parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros15 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="Ни в одном", callback_data="Ни в одном")
        callback_button_v2 = types.InlineKeyboardButton(text="В одном", callback_data="В одном")
        callback_button_v3 = types.InlineKeyboardButton(text="В четырех", callback_data="В четырех")
        callback_button_v4 = types.InlineKeyboardButton(text="В шести", callback_data="В шести")
        callback_button_v5 = types.InlineKeyboardButton(text="Во всех", callback_data="Во всех")
        keyboard_vopros15.add(callback_button_v1)
        keyboard_vopros15.add(callback_button_v2)
        keyboard_vopros15.add(callback_button_v3)
        keyboard_vopros15.add(callback_button_v4)
        keyboard_vopros15.add(callback_button_v5)
        bot.send_message(call.message.chat.id, 'В некоторых месяцах 31 день. А во скольких 28 дней?',
                         reply_markup=keyboard_vopros15)
    if call.data == "60age":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_У каждого человека всего один день рождения..._',
                         parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros15 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="Ни в одном", callback_data="Ни в одном")
        callback_button_v2 = types.InlineKeyboardButton(text="В одном", callback_data="В одном")
        callback_button_v3 = types.InlineKeyboardButton(text="В четырех", callback_data="В четырех")
        callback_button_v4 = types.InlineKeyboardButton(text="В шести", callback_data="В шести")
        callback_button_v5 = types.InlineKeyboardButton(text="Во всех", callback_data="Во всех")
        keyboard_vopros15.add(callback_button_v1)
        keyboard_vopros15.add(callback_button_v2)
        keyboard_vopros15.add(callback_button_v3)
        keyboard_vopros15.add(callback_button_v4)
        keyboard_vopros15.add(callback_button_v5)
        bot.send_message(call.message.chat.id, 'В некоторых месяцах 31 день. А во скольких 28 дней?',
                         reply_markup=keyboard_vopros15)
    if call.data == "70age":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_У каждого человека всего один день рождения..._',
                         parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros15 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="Ни в одном", callback_data="Ни в одном")
        callback_button_v2 = types.InlineKeyboardButton(text="В одном", callback_data="В одном")
        callback_button_v3 = types.InlineKeyboardButton(text="В четырех", callback_data="В четырех")
        callback_button_v4 = types.InlineKeyboardButton(text="В шести", callback_data="В шести")
        callback_button_v5 = types.InlineKeyboardButton(text="Во всех", callback_data="Во всех")
        keyboard_vopros15.add(callback_button_v1)
        keyboard_vopros15.add(callback_button_v2)
        keyboard_vopros15.add(callback_button_v3)
        keyboard_vopros15.add(callback_button_v4)
        keyboard_vopros15.add(callback_button_v5)
        bot.send_message(call.message.chat.id, 'В некоторых месяцах 31 день. А во скольких 28 дней?',
                         reply_markup=keyboard_vopros15)
    if call.data == "80age":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_У каждого человека всего один день рождения..._',
                         parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros15 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="Ни в одном", callback_data="Ни в одном")
        callback_button_v2 = types.InlineKeyboardButton(text="В одном", callback_data="В одном")
        callback_button_v3 = types.InlineKeyboardButton(text="В четырех", callback_data="В четырех")
        callback_button_v4 = types.InlineKeyboardButton(text="В шести", callback_data="В шести")
        callback_button_v5 = types.InlineKeyboardButton(text="Во всех", callback_data="Во всех")
        keyboard_vopros15.add(callback_button_v1)
        keyboard_vopros15.add(callback_button_v2)
        keyboard_vopros15.add(callback_button_v3)
        keyboard_vopros15.add(callback_button_v4)
        keyboard_vopros15.add(callback_button_v5)
        bot.send_message(call.message.chat.id, 'В некоторых месяцах 31 день. А во скольких 28 дней?',
                         reply_markup=keyboard_vopros15)
    if call.data == "1age":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKheF_0aXOYUJK_yskv_0jZ_EIRKcpdAAIsAAPBnGAMsN15duPYIJUeBA')
        bot.send_message(call.message.chat.id, 'Верно!'
                                               '\n_У каждого человека всего один день рождения 🙂_',
                         parse_mode="Markdown")
        keyboard_vopros15 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="Ни в одном", callback_data="Ни в одном")
        callback_button_v2 = types.InlineKeyboardButton(text="В одном", callback_data="В одном")
        callback_button_v3 = types.InlineKeyboardButton(text="В четырех", callback_data="В четырех")
        callback_button_v4 = types.InlineKeyboardButton(text="В шести", callback_data="В шести")
        callback_button_v5 = types.InlineKeyboardButton(text="Во всех", callback_data="Во всех")
        keyboard_vopros15.add(callback_button_v1)
        keyboard_vopros15.add(callback_button_v2)
        keyboard_vopros15.add(callback_button_v3)
        keyboard_vopros15.add(callback_button_v4)
        keyboard_vopros15.add(callback_button_v5)
        bot.send_message(call.message.chat.id, 'В некоторых месяцах 31 день. А во скольких 28 дней?',
                         reply_markup=keyboard_vopros15)
    # ДЕНЬ2
    # Вопрос 16
    if call.data == "Ни в одном":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_Во всех! В каждом месяце как минимум 28 дней._',
                         parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros16 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="Да", callback_data="Да вопрос 16")
        callback_button_v2 = types.InlineKeyboardButton(text="Да, если она сама не жената", callback_data="если она не жената")
        callback_button_v3 = types.InlineKeyboardButton(text="Нет", callback_data="Нет вопрос 16")
        keyboard_vopros16.add(callback_button_v1)
        keyboard_vopros16.add(callback_button_v2)
        keyboard_vopros16.add(callback_button_v3)
        bot.send_message(call.message.chat.id,
                         'Если вы живете в Калифорнии, можете ли вы жениться на сестре вашей вдовы?',
                         reply_markup=keyboard_vopros16)
    if call.data == "В одном":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_Во всех! В каждом месяце как минимум 28 дней._',
                         parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros16 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="Да", callback_data="Да вопрос 16")
        callback_button_v2 = types.InlineKeyboardButton(text="Да, если она сама не жената",
                                                        callback_data="если она не жената")
        callback_button_v3 = types.InlineKeyboardButton(text="Нет", callback_data="Нет вопрос 16")
        keyboard_vopros16.add(callback_button_v1)
        keyboard_vopros16.add(callback_button_v2)
        keyboard_vopros16.add(callback_button_v3)
        bot.send_message(call.message.chat.id,
                         'Если вы живете в Калифорнии, можете ли вы жениться на сестре вашей вдовы?',
                         reply_markup=keyboard_vopros16)
    if call.data == "В четырех":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_Во всех! В каждом месяце как минимум 28 дней._',
                         parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros16 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="Да", callback_data="Да вопрос 16")
        callback_button_v2 = types.InlineKeyboardButton(text="Да, если она сама не жената",
                                                        callback_data="если она не жената")
        callback_button_v3 = types.InlineKeyboardButton(text="Нет", callback_data="Нет вопрос 16")
        keyboard_vopros16.add(callback_button_v1)
        keyboard_vopros16.add(callback_button_v2)
        keyboard_vopros16.add(callback_button_v3)
        bot.send_message(call.message.chat.id,
                         'Если вы живете в Калифорнии, можете ли вы жениться на сестре вашей вдовы?',
                         reply_markup=keyboard_vopros16)
    if call.data == "В шести":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_Во всех! В каждом месяце как минимум 28 дней._',
                         parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros16 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="Да", callback_data="Да вопрос 16")
        callback_button_v2 = types.InlineKeyboardButton(text="Да, если она сама не жената",
                                                        callback_data="если она не жената")
        callback_button_v3 = types.InlineKeyboardButton(text="Нет", callback_data="Нет вопрос 16")
        keyboard_vopros16.add(callback_button_v1)
        keyboard_vopros16.add(callback_button_v2)
        keyboard_vopros16.add(callback_button_v3)
        bot.send_message(call.message.chat.id,
                         'Если вы живете в Калифорнии, можете ли вы жениться на сестре вашей вдовы?',
                         reply_markup=keyboard_vopros16)
    if call.data == "Во всех":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKhVV_0Wpzb_9oGqtG3pWIqNv2nCH4CAAIEAAM7YCQUs6vrVG-V4aseBA')
        bot.send_message(call.message.chat.id, 'Верно!'
                                               '\n_Во всех! В каждом месяце как минимум 28 дней._',
                         parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros16 = types.InlineKeyboardMarkup()
        callback_button_v1 = types.InlineKeyboardButton(text="Да", callback_data="Да вопрос 16")
        callback_button_v2 = types.InlineKeyboardButton(text="Да, если она сама не жената",
                                                        callback_data="если она не жената")
        callback_button_v3 = types.InlineKeyboardButton(text="Нет", callback_data="Нет вопрос 16")
        keyboard_vopros16.add(callback_button_v1)
        keyboard_vopros16.add(callback_button_v2)
        keyboard_vopros16.add(callback_button_v3)
        bot.send_message(call.message.chat.id,
                         'Если вы живете в Калифорнии, можете ли вы жениться на сестре вашей вдовы?',
                         reply_markup=keyboard_vopros16)
    # ДЕНЬ2
    # КОНЕЦ
    if call.data == "Да вопрос 16":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id,
                         'Не верно!'
                         '\n_Не можете... потому что в этом случае вы - труп (в буквальном смысле!)_',
                         parse_mode="Markdown")
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Ух, отлично пообщались! ' + call.message.chat.first_name +
                         ', я очень доволен тем, '
                         'что мы стали ближе 🥰'
                         '\nПосмотрим, как ты справишься со следующим уровнем 😏')
        time.sleep(1)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAK51GAJW4z-gzgqFpAQgL0rEXXs2SDnAAJkAwACz7vUDohKFjPIdxptHgQ',
                         reply_markup=const.markup_menu_poka_day2)
    if call.data == "если она не жената":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_Не можете... потому что в этом случае '
                                               'вы - труп (в буквальном смысле!)_',
                         parse_mode="Markdown")
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Ух, отлично пообщались! ' + call.message.chat.first_name +
                         ', я очень доволен тем, '
                         'что мы стали ближе 🥰'
                         '\nПосмотрим, как ты справишься со следующим уровнем 😏')
        time.sleep(1)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAK51GAJW4z-gzgqFpAQgL0rEXXs2SDnAAJkAwACz7vUDohKFjPIdxptHgQ',
                         reply_markup=const.markup_menu_poka_day2)
    if call.data == "Нет вопрос 16":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Верно!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Ух, отлично пообщались! ' + call.message.chat.first_name +
                         ', я очень доволен тем, '
                         'что мы стали ближе 🥰'
                         '\nПосмотрим, как ты справишься со следующим уровнем 😏')
        time.sleep(1)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAK51GAJW4z-gzgqFpAQgL0rEXXs2SDnAAJkAwACz7vUDohKFjPIdxptHgQ',
                         reply_markup=const.markup_menu_poka_day2)
    # ДЕНЬ3
    # Вопрос 1
    if call.data == "безопасность вопрос 1":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data=" безопасность вопрос 1")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 1")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 1")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 1")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 1")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 1")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id, 'Подберите мне авто. '
                                               'Для девочки 2 лет, чтобы проездила как минимум 2-3 года,'
                                               'т.к. я не собираюсь платить такие большие деньги за маленький '
                                               'промежуток времени… '
                                               'Найдите мне самый бюджетный вариант … А есть у вас рассрочка?',
                         reply_markup=keyboard_vopros1)
    if call.data == "привязанность вопрос 1":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data=" безопасность вопрос 1")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 1")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 1")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 1")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 1")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 1")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id, 'Подберите мне авто. '
                                               'Для девочки 2 лет, чтобы проездила как минимум 2-3 года,'
                                               'т.к. я не собираюсь платить такие большие деньги за маленький '
                                               'промежуток времени… '
                                               'Найдите мне самый бюджетный вариант … А есть у вас рассрочка?',
                         reply_markup=keyboard_vopros1)
    if call.data == "комфорт вопрос 1":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data=" безопасность вопрос 1")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 1")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 1")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 1")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 1")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 1")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id, 'Подберите мне авто. '
                                               'Для девочки 2 лет, чтобы проездила как минимум 2-3 года,'
                                               'т.к. я не собираюсь платить такие большие деньги за маленький '
                                               'промежуток времени… '
                                               'Найдите мне самый бюджетный вариант … А есть у вас рассрочка?',
                         reply_markup=keyboard_vopros1)
    if call.data == "престиж вопрос 1":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data=" безопасность вопрос 1")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 1")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 1")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 1")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 1")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 1")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id, 'Подберите мне авто. '
                                               'Для девочки 2 лет, чтобы проездила как минимум 2-3 года,'
                                               'т.к. я не собираюсь платить такие большие деньги за маленький '
                                               'промежуток времени… '
                                               'Найдите мне самый бюджетный вариант … А есть у вас рассрочка?',
                         reply_markup=keyboard_vopros1)
    if call.data == "новизна вопрос 1":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data=" безопасность вопрос 1")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 1")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 1")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 1")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 1")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 1")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id, 'Подберите мне авто. '
                                               'Для девочки 2 лет, чтобы проездила как минимум 2-3 года,'
                                               'т.к. я не собираюсь платить такие большие деньги за маленький '
                                               'промежуток времени… '
                                               'Найдите мне самый бюджетный вариант … А есть у вас рассрочка?',
                         reply_markup=keyboard_vopros1)
    if call.data == "экономии вопрос 1":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKiAV_00Qtx8Hc5lGlovPkr2iyPkyulAAI4AAN7wH0TVDwAAeLVdK3PHgQ')
        bot.send_message(call.message.chat.id, 'Ты телепат, считываешь мотивы клиента с первого раза!')
        time.sleep(1)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 2")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 2")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 2")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 2")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 2")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 2")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Как такое могло произойти, что смс-ка с моими результатами анализов пришла другому человеку? '
                         'Это же конфиденциальная информация. 21 век на дворе, а у вас такие косяки.',
                         reply_markup=keyboard_vopros1)
    # ДЕНЬ3
    # Вопрос 2
    if call.data == "привязанность вопрос 2":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 2")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 2")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 2")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 2")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 2")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 2")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Как такое могло произойти, что смс-ка с моими результатами анализов пришла другому человеку? '
                         'Это же конфиденциальная информация. 21 век на дворе, а у вас такие косяки.',
                         reply_markup=keyboard_vopros1)
    if call.data == "комфорт вопрос 2":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 2")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 2")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 2")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 2")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 2")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 2")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Как такое могло произойти, что смс-ка с моими результатами анализов пришла другому человеку? '
                         'Это же конфиденциальная информация. 21 век на дворе, а у вас такие косяки.',
                         reply_markup=keyboard_vopros1)
    if call.data == "престиж вопрос 2":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 2")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 2")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 2")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 2")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 2")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 2")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Как такое могло произойти, что смс-ка с моими результатами анализов пришла другому человеку? '
                         'Это же конфиденциальная информация. 21 век на дворе, а у вас такие косяки.',
                         reply_markup=keyboard_vopros1)
    if call.data == "новизна вопрос 2":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 2")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 2")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 2")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 2")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 2")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 2")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Как такое могло произойти, что смс-ка с моими результатами анализов пришла другому человеку? '
                         'Это же конфиденциальная информация. 21 век на дворе, а у вас такие косяки.',
                         reply_markup=keyboard_vopros1)
    if call.data == "экономии вопрос 2":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 2")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 2")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 2")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 2")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 2")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 2")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Как такое могло произойти, что смс-ка с моими результатами анализов пришла другому человеку? '
                         'Это же конфиденциальная информация. 21 век на дворе, а у вас такие косяки.',
                         reply_markup=keyboard_vopros1)
    if call.data == "безопасность вопрос 2":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKiDF_01mPcy-U-pitzCHmQBEsGMCRPAAJFAAN7wH0TQaXN1LpRlOceBA')
        bot.send_message(call.message.chat.id, 'Верно! Так держать 👍')
        time.sleep(1)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 3")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 3")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 3")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 3")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 3")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 3")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Вы знаете, для меня очень важно, чтобы ребенок с раннего детства видел, '
                         'что у него может быть все, как у его папы. '
                         'Чтобы не чувствовал, что ему что-то недоступно из-за возраста или по каким-то иным причинам. '
                         'Здоровые амбиции - это отлично, хах. Поэтому я смотрю модели именно BMW... '
                         'Да, цена не имеет значение, главное, чтобы цена - качество были соизмеримы. '
                         'Платить деньги за то, что того не стоит, я не собираюсь... '
                         'Мне абсолютно все равно, в какой фирме осуществить покупку, если вы лучшие на рынке РБ '
                         'и можете мне прямо сейчас привести аргументы, то мы оформим заказ)',
                         reply_markup=keyboard_vopros1)
    # ДЕНЬ3
    # Вопрос 3
    if call.data == "безопасность вопрос 3":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 3")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 3")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 3")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 3")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 3")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 3")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Вы знаете, для меня очень важно, чтобы ребенок с раннего детства видел, '
                         'что у него может быть все, как у его папы. '
                         'Чтобы не чувствовал, что ему что-то недоступно из-за возраста или по каким-то иным причинам. '
                         'Здоровые амбиции - это отлично, хах. Поэтому я смотрю модели именно BMW... '
                         'Да, цена не имеет значение, главное, чтобы цена - качество были соизмеримы. '
                         'Платить деньги за то, что того не стоит, я не собираюсь... '
                         'Мне абсолютно все равно, в какой фирме осуществить покупку, если вы лучшие на рынке РБ '
                         'и можете мне прямо сейчас привести аргументы, то мы оформим заказ)',
                         reply_markup=keyboard_vopros1)
    if call.data == "привязанность вопрос 3":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 3")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 3")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 3")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 3")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 3")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 3")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Вы знаете, для меня очень важно, чтобы ребенок с раннего детства видел, '
                         'что у него может быть все, как у его папы. '
                         'Чтобы не чувствовал, что ему что-то недоступно из-за возраста или по каким-то иным причинам. '
                         'Здоровые амбиции - это отлично, хах. Поэтому я смотрю модели именно BMW... '
                         'Да, цена не имеет значение, главное, чтобы цена - качество были соизмеримы. '
                         'Платить деньги за то, что того не стоит, я не собираюсь... '
                         'Мне абсолютно все равно, в какой фирме осуществить покупку, если вы лучшие на рынке РБ '
                         'и можете мне прямо сейчас привести аргументы, то мы оформим заказ)',
                         reply_markup=keyboard_vopros1)
    if call.data == "комфорт вопрос 3":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 3")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 3")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 3")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 3")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 3")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 3")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Вы знаете, для меня очень важно, чтобы ребенок с раннего детства видел, '
                         'что у него может быть все, как у его папы. '
                         'Чтобы не чувствовал, что ему что-то недоступно из-за возраста или по каким-то иным причинам. '
                         'Здоровые амбиции - это отлично, хах. Поэтому я смотрю модели именно BMW... '
                         'Да, цена не имеет значение, главное, чтобы цена - качество были соизмеримы. '
                         'Платить деньги за то, что того не стоит, я не собираюсь... '
                         'Мне абсолютно все равно, в какой фирме осуществить покупку, если вы лучшие на рынке РБ '
                         'и можете мне прямо сейчас привести аргументы, то мы оформим заказ)',
                         reply_markup=keyboard_vopros1)
    if call.data == "новизна вопрос 3":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 3")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 3")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 3")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 3")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 3")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 3")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Вы знаете, для меня очень важно, чтобы ребенок с раннего детства видел, '
                         'что у него может быть все, как у его папы. '
                         'Чтобы не чувствовал, что ему что-то недоступно из-за возраста или по каким-то иным причинам. '
                         'Здоровые амбиции - это отлично, хах. Поэтому я смотрю модели именно BMW... '
                         'Да, цена не имеет значение, главное, чтобы цена - качество были соизмеримы. '
                         'Платить деньги за то, что того не стоит, я не собираюсь... '
                         'Мне абсолютно все равно, в какой фирме осуществить покупку, если вы лучшие на рынке РБ '
                         'и можете мне прямо сейчас привести аргументы, то мы оформим заказ)',
                         reply_markup=keyboard_vopros1)
    if call.data == "экономии вопрос 3":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 3")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 3")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 3")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 3")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 3")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 3")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Вы знаете, для меня очень важно, чтобы ребенок с раннего детства видел, '
                         'что у него может быть все, как у его папы. '
                         'Чтобы не чувствовал, что ему что-то недоступно из-за возраста или по каким-то иным причинам. '
                         'Здоровые амбиции - это отлично, хах. Поэтому я смотрю модели именно BMW... '
                         'Да, цена не имеет значение, главное, чтобы цена - качество были соизмеримы. '
                         'Платить деньги за то, что того не стоит, я не собираюсь... '
                         'Мне абсолютно все равно, в какой фирме осуществить покупку, если вы лучшие на рынке РБ '
                         'и можете мне прямо сейчас привести аргументы, то мы оформим заказ)',
                         reply_markup=keyboard_vopros1)
    if call.data == "престиж вопрос 3":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKiEl_018rx58QeikvnQp0tqRohoDqgAAK0AAN7wH0TtKVMG7NclcYeBA')
        bot.send_message(call.message.chat.id, 'Ты умеешь читать мысли 😎')
        time.sleep(1)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 4")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 4")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 4")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 4")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 4")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 4")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Мне нужен такой тариф, чтобы мне было удобно. '
                         'Я очень часто зависаю в мессенджерах, т.к. моя работа связана с постоянным общением с '
                         'заказчиками. Плюс я часто езжу в командировки и соответственно использую те же мессенджеры '
                         'уже для общения с близкими. Я очень редко звоню, чаще звонят мне. '
                         'Я предпочитаю общение в переписке: так ничего не забудется и можно все лаконично и четко '
                         'изложить без лишних эмоций. А еще в дороге я смотрю фильмы. Что вы можете мне предложить?',
                         reply_markup=keyboard_vopros1)
    # ДЕНЬ3
    # Вопрос 4
    if call.data == "безопасность вопрос 4":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 4")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 4")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 4")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 4")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 4")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 4")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Мне нужен такой тариф, чтобы мне было удобно. '
                         'Я очень часто зависаю в мессенджерах, т.к. моя работа связана с постоянным общением с '
                         'заказчиками. Плюс я часто езжу в командировки и соответственно использую те же мессенджеры '
                         'уже для общения с близкими. Я очень редко звоню, чаще звонят мне. '
                         'Я предпочитаю общение в переписке: так ничего не забудется и можно все лаконично и четко '
                         'изложить без лишних эмоций. А еще в дороге я смотрю фильмы. Что вы можете мне предложить?',
                         reply_markup=keyboard_vopros1)
    if call.data == "привязанность вопрос 4":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 4")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 4")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 4")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 4")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 4")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 4")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Мне нужен такой тариф, чтобы мне было удобно. '
                         'Я очень часто зависаю в мессенджерах, т.к. моя работа связана с постоянным общением с '
                         'заказчиками. Плюс я часто езжу в командировки и соответственно использую те же мессенджеры '
                         'уже для общения с близкими. Я очень редко звоню, чаще звонят мне. '
                         'Я предпочитаю общение в переписке: так ничего не забудется и можно все лаконично и четко '
                         'изложить без лишних эмоций. А еще в дороге я смотрю фильмы. Что вы можете мне предложить?',
                         reply_markup=keyboard_vopros1)
    if call.data == "экономии вопрос 4":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 4")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 4")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 4")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 4")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 4")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 4")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Мне нужен такой тариф, чтобы мне было удобно. '
                         'Я очень часто зависаю в мессенджерах, т.к. моя работа связана с постоянным общением с '
                         'заказчиками. Плюс я часто езжу в командировки и соответственно использую те же мессенджеры '
                         'уже для общения с близкими. Я очень редко звоню, чаще звонят мне. '
                         'Я предпочитаю общение в переписке: так ничего не забудется и можно все лаконично и четко '
                         'изложить без лишних эмоций. А еще в дороге я смотрю фильмы. Что вы можете мне предложить?',
                         reply_markup=keyboard_vopros1)
    if call.data == "престиж вопрос 4":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 4")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 4")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 4")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 4")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 4")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 4")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Мне нужен такой тариф, чтобы мне было удобно. '
                         'Я очень часто зависаю в мессенджерах, т.к. моя работа связана с постоянным общением с '
                         'заказчиками. Плюс я часто езжу в командировки и соответственно использую те же мессенджеры '
                         'уже для общения с близкими. Я очень редко звоню, чаще звонят мне. '
                         'Я предпочитаю общение в переписке: так ничего не забудется и можно все лаконично и четко '
                         'изложить без лишних эмоций. А еще в дороге я смотрю фильмы. Что вы можете мне предложить?',
                         reply_markup=keyboard_vopros1)
    if call.data == "новизна вопрос 4":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 4")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 4")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 4")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 4")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 4")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 4")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Мне нужен такой тариф, чтобы мне было удобно. '
                         'Я очень часто зависаю в мессенджерах, т.к. моя работа связана с постоянным общением с '
                         'заказчиками. Плюс я часто езжу в командировки и соответственно использую те же мессенджеры '
                         'уже для общения с близкими. Я очень редко звоню, чаще звонят мне. '
                         'Я предпочитаю общение в переписке: так ничего не забудется и можно все лаконично и четко '
                         'изложить без лишних эмоций. А еще в дороге я смотрю фильмы. Что вы можете мне предложить?',
                         reply_markup=keyboard_vopros1)
    if call.data == "комфорт вопрос 4":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKiGF_02Uw7r2fDgZcn3AeRwMVxRWrsAAL1AAMw1J0R3NeLwV6aUvUeBA')
        bot.send_message(call.message.chat.id, 'Ты чуешь истинную потребность клиента за версту!')
        time.sleep(1)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 5")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 5")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 5")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 5")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 5")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 5")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Скажите, а у вас есть скидки? Или может быть какие-то подарки при покупке от определенной '
                         'суммы? ... Хм, вы так рассказываете, что мне прям хочется самому сесть в эту машинку и '
                         'проехать на ней по своему дачному участку. Жаль, что мне не 8 лет… А я могу пообщаться '
                         'именно с вами, когда наберу в следующий раз? Не хочу с кем-то другим вести беседы',
                         reply_markup=keyboard_vopros1)
    # ДЕНЬ3
    # Вопрос 5
    if call.data == "безопасность вопрос 5":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 5")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 5")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 5")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 5")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 5")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 5")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Скажите, а у вас есть скидки? Или может быть какие-то подарки при покупке от определенной '
                         'суммы? ... Хм, вы так рассказываете, что мне прям хочется самому сесть в эту машинку и '
                         'проехать на ней по своему дачному участку. Жаль, что мне не 8 лет… А я могу пообщаться '
                         'именно с вами, когда наберу в следующий раз? Не хочу с кем-то другим вести беседы',
                         reply_markup=keyboard_vopros1)
    if call.data == "экономии вопрос 5":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 5")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 5")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 5")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 5")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 5")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 5")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Скажите, а у вас есть скидки? Или может быть какие-то подарки при покупке от определенной '
                         'суммы? ... Хм, вы так рассказываете, что мне прям хочется самому сесть в эту машинку и '
                         'проехать на ней по своему дачному участку. Жаль, что мне не 8 лет… А я могу пообщаться '
                         'именно с вами, когда наберу в следующий раз? Не хочу с кем-то другим вести беседы',
                         reply_markup=keyboard_vopros1)
    if call.data == "комфорт вопрос 5":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 5")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 5")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 5")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 5")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 5")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 5")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Скажите, а у вас есть скидки? Или может быть какие-то подарки при покупке от определенной '
                         'суммы? ... Хм, вы так рассказываете, что мне прям хочется самому сесть в эту машинку и '
                         'проехать на ней по своему дачному участку. Жаль, что мне не 8 лет… А я могу пообщаться '
                         'именно с вами, когда наберу в следующий раз? Не хочу с кем-то другим вести беседы',
                         reply_markup=keyboard_vopros1)
    if call.data == "престиж вопрос 5":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 5")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 5")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 5")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 5")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 5")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 5")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Скажите, а у вас есть скидки? Или может быть какие-то подарки при покупке от определенной '
                         'суммы? ... Хм, вы так рассказываете, что мне прям хочется самому сесть в эту машинку и '
                         'проехать на ней по своему дачному участку. Жаль, что мне не 8 лет… А я могу пообщаться '
                         'именно с вами, когда наберу в следующий раз? Не хочу с кем-то другим вести беседы',
                         reply_markup=keyboard_vopros1)
    if call.data == "новизна вопрос 5":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 5")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 5")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 5")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 5")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 5")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 5")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'Скажите, а у вас есть скидки? Или может быть какие-то подарки при покупке от определенной '
                         'суммы? ... Хм, вы так рассказываете, что мне прям хочется самому сесть в эту машинку и '
                         'проехать на ней по своему дачному участку. Жаль, что мне не 8 лет… А я могу пообщаться '
                         'именно с вами, когда наберу в следующий раз? Не хочу с кем-то другим вести беседы',
                         reply_markup=keyboard_vopros1)
    if call.data == "привязанность вопрос 5":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKiHl_02g941a-tKmk4mzdlewNO1waqAALEAAMw1J0RyMW8vArrFUoeBA')
        bot.send_message(call.message.chat.id, 'Ты знаешь толк в определении того, что же именно движет клиентом')
        time.sleep(1)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 6")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 6")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 6")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 6")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 6")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 6")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id, 'Мы уже у вас покупали машинку для ребенка. '
                                               'Но она уже не актуальна, не в тренде. Знаю, что уже появились более '
                                               'мощные модели, с более полной комплектацией и интересными функциями. '
                                               'Что вы можете мне предложить?.. Мой ребенок постоянно мониторит, '
                                               'что появляется на рынке. Это будет уже 3-я машинка',
                         reply_markup=keyboard_vopros1)
    # ДЕНЬ3
    # Вопрос 6
    if call.data == "безопасность вопрос 6":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 6")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 6")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 6")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 6")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 6")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 6")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id, 'Мы уже у вас покупали машинку для ребенка. '
                                               'Но она уже не актуальна, не в тренде. Знаю, что уже появились более '
                                               'мощные модели, с более полной комплектацией и интересными функциями. '
                                               'Что вы можете мне предложить?.. Мой ребенок постоянно мониторит, '
                                               'что появляется на рынке. Это будет уже 3-я машинка',
                         reply_markup=keyboard_vopros1)
    if call.data == "привязанность вопрос 6":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 6")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 6")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 6")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 6")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 6")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 6")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id, 'Мы уже у вас покупали машинку для ребенка. '
                                               'Но она уже не актуальна, не в тренде. Знаю, что уже появились более '
                                               'мощные модели, с более полной комплектацией и интересными функциями. '
                                               'Что вы можете мне предложить?.. Мой ребенок постоянно мониторит, '
                                               'что появляется на рынке. Это будет уже 3-я машинка',
                         reply_markup=keyboard_vopros1)
    if call.data == "комфорт вопрос 6":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 6")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 6")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 6")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 6")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 6")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 6")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id, 'Мы уже у вас покупали машинку для ребенка. '
                                               'Но она уже не актуальна, не в тренде. Знаю, что уже появились более '
                                               'мощные модели, с более полной комплектацией и интересными функциями. '
                                               'Что вы можете мне предложить?.. Мой ребенок постоянно мониторит, '
                                               'что появляется на рынке. Это будет уже 3-я машинка',
                         reply_markup=keyboard_vopros1)
    if call.data == "престиж вопрос 6":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 6")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 6")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 6")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 6")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 6")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 6")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id, 'Мы уже у вас покупали машинку для ребенка. '
                                               'Но она уже не актуальна, не в тренде. Знаю, что уже появились более '
                                               'мощные модели, с более полной комплектацией и интересными функциями. '
                                               'Что вы можете мне предложить?.. Мой ребенок постоянно мониторит, '
                                               'что появляется на рынке. Это будет уже 3-я машинка',
                         reply_markup=keyboard_vopros1)
    if call.data == "экономии вопрос 6":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 6")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 6")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 6")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 6")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 6")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 6")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id, 'Мы уже у вас покупали машинку для ребенка. '
                                               'Но она уже не актуальна, не в тренде. Знаю, что уже появились более '
                                               'мощные модели, с более полной комплектацией и интересными функциями. '
                                               'Что вы можете мне предложить?.. Мой ребенок постоянно мониторит, '
                                               'что появляется на рынке. Это будет уже 3-я машинка',
                         reply_markup=keyboard_vopros1)
    if call.data == "новизна вопрос 6":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKiJF_02v4lq7VLUV00fQ5sj-w8uAXMAAIDAAP3F4ErOtLbAuMqTpceBA')
        bot.send_message(call.message.chat.id, 'Молодец! Так держать 👍 ')
        time.sleep(1)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 7")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 7")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 7")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 7")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 7")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 7")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А у вас точно все стерильно, я могу не беспокоиться о том, что может быть заражение крови '
                         'при сдаче анализов?',
                         reply_markup=keyboard_vopros1)
    # ДЕНЬ3
    # Вопрос 7
    if call.data == "привязанность вопрос 7":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 7")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 7")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 7")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 7")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 7")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 7")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А у вас точно все стерильно, я могу не беспокоиться о том, что может быть заражение крови '
                         'при сдаче анализов?',
                         reply_markup=keyboard_vopros1)
    if call.data == "комфорт вопрос 7":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 7")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 7")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 7")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 7")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 7")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 7")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А у вас точно все стерильно, я могу не беспокоиться о том, что может быть заражение крови '
                         'при сдаче анализов?',
                         reply_markup=keyboard_vopros1)
    if call.data == "престиж вопрос 7":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 7")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 7")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 7")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 7")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 7")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 7")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А у вас точно все стерильно, я могу не беспокоиться о том, что может быть заражение крови '
                         'при сдаче анализов?',
                         reply_markup=keyboard_vopros1)
    if call.data == "новизна вопрос 7":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 7")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 7")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 7")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 7")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 7")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 7")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А у вас точно все стерильно, я могу не беспокоиться о том, что может быть заражение крови '
                         'при сдаче анализов?',
                         reply_markup=keyboard_vopros1)
    if call.data == "экономии вопрос 7":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 7")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 7")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 7")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 7")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 7")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 7")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А у вас точно все стерильно, я могу не беспокоиться о том, что может быть заражение крови '
                         'при сдаче анализов?',
                         reply_markup=keyboard_vopros1)
    if call.data == "безопасность вопрос 7":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKiKl_029cP4MJJgTcJt2amMzOwTl7DAAILAAP3F4Er_st2rNLiKEkeBA')
        bot.send_message(call.message.chat.id, 'Ты телепат, считываешь мотивы клиента с первого раза!')
        time.sleep(1)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 8")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 8")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 8")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 8")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 8")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 8")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А у вас есть услуга доставки, я не хочу тратить свое время на какие-то поездки,'
                         ' хочу, чтобы вы мне все доставили сами в удобное для меня время',
                         reply_markup=keyboard_vopros1)
    # ДЕНЬ3
    # Вопрос 8
    if call.data == "безопасность вопрос 8":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 8")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 8")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 8")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 8")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 8")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 8")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А у вас есть услуга доставки, я не хочу тратить свое время на какие-то поездки,'
                         ' хочу, чтобы вы мне все доставили сами в удобное для меня время',
                         reply_markup=keyboard_vopros1)
    if call.data == "привязанность вопрос 8":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 8")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 8")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 8")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 8")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 8")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 8")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А у вас есть услуга доставки, я не хочу тратить свое время на какие-то поездки,'
                         ' хочу, чтобы вы мне все доставили сами в удобное для меня время',
                         reply_markup=keyboard_vopros1)
    if call.data == "экономии вопрос 8":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 8")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 8")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 8")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 8")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 8")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 8")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А у вас есть услуга доставки, я не хочу тратить свое время на какие-то поездки,'
                         ' хочу, чтобы вы мне все доставили сами в удобное для меня время',
                         reply_markup=keyboard_vopros1)
    if call.data == "престиж вопрос 8":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 8")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 8")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 8")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 8")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 8")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 8")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А у вас есть услуга доставки, я не хочу тратить свое время на какие-то поездки,'
                         ' хочу, чтобы вы мне все доставили сами в удобное для меня время',
                         reply_markup=keyboard_vopros1)
    if call.data == "новизна вопрос 8":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 8")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 8")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 8")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 8")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 8")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 8")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А у вас есть услуга доставки, я не хочу тратить свое время на какие-то поездки,'
                         ' хочу, чтобы вы мне все доставили сами в удобное для меня время',
                         reply_markup=keyboard_vopros1)
    if call.data == "комфорт вопрос 8":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKiLV_03ID9DkeSxMHvFo6DODwOg2SjAAINAAOWn4wONM9_DtpaNXUeBA')
        bot.send_message(call.message.chat.id, 'Ты умеешь читать мысли 😎')
        time.sleep(1)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 9")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 9")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 9")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 9")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 9")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 9")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А ваша служба доставки на каком месте в рейтинге по РФ? Какие преимущества у вас перед '
                         'вашими конкурентами?',
                         reply_markup=keyboard_vopros1)
    # ДЕНЬ3
    # Вопрос 9
    if call.data == "безопасность вопрос 9":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 9")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 9")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 9")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 9")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 9")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 9")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А ваша служба доставки на каком месте в рейтинге по РФ? Какие преимущества у вас перед '
                         'вашими конкурентами?',
                         reply_markup=keyboard_vopros1)
    if call.data == "привязанность вопрос 9":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 9")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 9")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 9")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 9")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 9")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 9")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А ваша служба доставки на каком месте в рейтинге по РФ? Какие преимущества у вас перед '
                         'вашими конкурентами?',
                         reply_markup=keyboard_vopros1)
    if call.data == "комфорт вопрос 9":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 9")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 9")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 9")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 9")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 9")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 9")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А ваша служба доставки на каком месте в рейтинге по РФ? Какие преимущества у вас перед '
                         'вашими конкурентами?',
                         reply_markup=keyboard_vopros1)
    if call.data == "новизна вопрос 9":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 9")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 9")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 9")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 9")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 9")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 9")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А ваша служба доставки на каком месте в рейтинге по РФ? Какие преимущества у вас перед '
                         'вашими конкурентами?',
                         reply_markup=keyboard_vopros1)
    if call.data == "экономии вопрос 9":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 9")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 9")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 9")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 9")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 9")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 9")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А ваша служба доставки на каком месте в рейтинге по РФ? Какие преимущества у вас перед '
                         'вашими конкурентами?',
                         reply_markup=keyboard_vopros1)
    if call.data == "престиж вопрос 9":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKiMF_03Q9Ok6zTO66jN9qtPXGlTzXtAAICAAOvxlEat-gMjnASweEeBA')
        bot.send_message(call.message.chat.id, 'Ты знаешь толк в определении того, что же именно движет клиентом')
        time.sleep(1)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 10")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 10")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 10")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 10")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 10")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 10")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А есть аналог такого же тарифа, но, может быть, с более длительными сроками доставки и, '
                         'следовательно, более выгодный по цене?',
                         reply_markup=keyboard_vopros1)
    # ДЕНЬ3
    # Вопрос 10
    if call.data == "безопасность вопрос 10":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 10")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 10")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 10")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 10")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 10")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 10")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А есть аналог такого же тарифа, но, может быть, с более длительными сроками доставки и, '
                         'следовательно, более выгодный по цене?',
                         reply_markup=keyboard_vopros1)
    if call.data == "привязанность вопрос 10":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 10")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 10")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 10")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 10")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 10")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 10")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А есть аналог такого же тарифа, но, может быть, с более длительными сроками доставки и, '
                         'следовательно, более выгодный по цене?',
                         reply_markup=keyboard_vopros1)
    if call.data == "комфорт вопрос 10":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 10")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 10")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 10")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 10")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 10")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 10")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А есть аналог такого же тарифа, но, может быть, с более длительными сроками доставки и, '
                         'следовательно, более выгодный по цене?',
                         reply_markup=keyboard_vopros1)
    if call.data == "престиж вопрос 10":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 10")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 10")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 10")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 10")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 10")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 10")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А есть аналог такого же тарифа, но, может быть, с более длительными сроками доставки и, '
                         'следовательно, более выгодный по цене?',
                         reply_markup=keyboard_vopros1)
    if call.data == "новизна вопрос 10":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\nПопробуй еще раз 🙂 Вот тебе подсказка:'
                                               '\n_Покупательские мотивы:_'
                                               '\n_❗ Безопасности: Ищет защищенность и гарантию, оценивает репутацию _'
                                               '_компании._'
                                               '\n'
                                               '\n_❗ Привязанности: Восприимчив к симпатии или ее отсутствии у _'
                                               '_продавца, к подарку или скидке, которые будут ему сделаны. _'
                                               '\n'
                                               '\n_❗ Комфорта: Удобство, которое приобретает клиент с покупкой _'
                                               '_товара._'
                                               '\n'
                                               '\n_❗ Престижа: Стремление клиента выделяться на общем фоне. Качество _'
                                               '_товара имеет большую роль. Приближение к более _'
                                               '_высокому уровню жизни. _'
                                               '\n'
                                               '\n_❗ Новизны: Хотят быть соблазненными каким-либо новым способом: _'
                                               '_новым продуктом, который удовлетворит их потребность в перемене. _'
                                               '\n'
                                               '\n_❗ Экономии: Не всегда имеет решительное преобладание. _'
                                               '_Часто служит _'
                                               '_прикрытием. Зачастую, цена – пустяк, в сравнении с услугами, _'
                                               '_которые может оказать товар._', parse_mode="Markdown")
        time.sleep(15)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_bezopasnost = types.InlineKeyboardButton(text="безопасность", callback_data="безопасность вопрос 10")
        keyboard_vopros1.add(btn_bezopasnost)
        btn_privyazannost = types.InlineKeyboardButton(text="привязанность", callback_data="привязанность вопрос 10")
        keyboard_vopros1.add(btn_privyazannost)
        btn_komfort = types.InlineKeyboardButton(text="комфорт", callback_data="комфорт вопрос 10")
        keyboard_vopros1.add(btn_komfort)
        btn_prestizh = types.InlineKeyboardButton(text="престиж", callback_data="престиж вопрос 10")
        keyboard_vopros1.add(btn_prestizh)
        btn_novizna = types.InlineKeyboardButton(text="новизна", callback_data="новизна вопрос 10")
        keyboard_vopros1.add(btn_novizna)
        btn_akonomii = types.InlineKeyboardButton(text="экономии", callback_data="экономии вопрос 10")
        keyboard_vopros1.add(btn_akonomii)
        bot.send_message(call.message.chat.id,
                         'А есть аналог такого же тарифа, но, может быть, с более длительными сроками доставки и, '
                         'следовательно, более выгодный по цене?',
                         reply_markup=keyboard_vopros1)
    if call.data == "экономии вопрос 10":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAK55mAJYVcRQ5cvmOJodTpF95NdrHvGAAIfAAOvxlEaXOcVuSobGHQeBA')
        bot.send_message(call.message.chat.id, 'Ты чуешь истинную потребность клиента за версту')
        time.sleep(3)
        bot.send_message(call.message.chat.id,
                         'Ну что ж, напоследок, уже по привычке, пару вопросов на логическое мышление 😉')
        time.sleep(2)
        keyboard_vopros11 = types.InlineKeyboardMarkup()
        btn_10 = types.InlineKeyboardButton(text="10", callback_data="10")
        keyboard_vopros11.add(btn_10)
        btn_25 = types.InlineKeyboardButton(text="25", callback_data="25")
        keyboard_vopros11.add(btn_25)
        btn_50 = types.InlineKeyboardButton(text="50", callback_data="50")
        keyboard_vopros11.add(btn_50)
        btn_70 = types.InlineKeyboardButton(text="70", callback_data="70")
        keyboard_vopros11.add(btn_70)
        btn_90 = types.InlineKeyboardButton(text="90", callback_data="90")
        keyboard_vopros11.add(btn_90)
        bot.send_message(call.message.chat.id, 'Разделите 30 на 1/2 и прибавьте 10. Сколько получится?',
                         reply_markup=keyboard_vopros11)
    # ДЕНЬ3
    # Вопрос 11
    if call.data == "10":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_30 : 0,5 = 60 + 10 = 70_', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros12 = types.InlineKeyboardMarkup()
        btn_20 = types.InlineKeyboardButton(text="Через 20 мин", callback_data="Через 20 мин")
        keyboard_vopros12.add(btn_20)
        btn_40 = types.InlineKeyboardButton(text="Через 40 мин", callback_data="Через 40 мин")
        keyboard_vopros12.add(btn_40)
        btn_60 = types.InlineKeyboardButton(text="Через 60 мин", callback_data="Через 60 мин")
        keyboard_vopros12.add(btn_60)
        btn_90 = types.InlineKeyboardButton(text="Через 90 мин", callback_data="Через 90 мин")
        keyboard_vopros12.add(btn_90)
        bot.send_message(call.message.chat.id,
                         'Доктор дал вам 3 таблетки. Вы должны принимать одну таблетку каждые полчаса. Через сколько '
                         'времени они у вас кончатся?',
                         reply_markup=keyboard_vopros12)
    if call.data == "25":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_30 : 0,5 = 60 + 10 = 70_', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros12 = types.InlineKeyboardMarkup()
        btn_20 = types.InlineKeyboardButton(text="Через 20 мин", callback_data="Через 20 мин")
        keyboard_vopros12.add(btn_20)
        btn_40 = types.InlineKeyboardButton(text="Через 40 мин", callback_data="Через 40 мин")
        keyboard_vopros12.add(btn_40)
        btn_60 = types.InlineKeyboardButton(text="Через 60 мин", callback_data="Через 60 мин")
        keyboard_vopros12.add(btn_60)
        btn_90 = types.InlineKeyboardButton(text="Через 90 мин", callback_data="Через 90 мин")
        keyboard_vopros12.add(btn_90)
        bot.send_message(call.message.chat.id,
                         'Доктор дал вам 3 таблетки. Вы должны принимать одну таблетку каждые полчаса. Через сколько '
                         'времени они у вас кончатся?',
                         reply_markup=keyboard_vopros12)
    if call.data == "50":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_30 : 0,5 = 60 + 10 = 70_', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros12 = types.InlineKeyboardMarkup()
        btn_20 = types.InlineKeyboardButton(text="Через 20 мин", callback_data="Через 20 мин")
        keyboard_vopros12.add(btn_20)
        btn_40 = types.InlineKeyboardButton(text="Через 40 мин", callback_data="Через 40 мин")
        keyboard_vopros12.add(btn_40)
        btn_60 = types.InlineKeyboardButton(text="Через 60 мин", callback_data="Через 60 мин")
        keyboard_vopros12.add(btn_60)
        btn_90 = types.InlineKeyboardButton(text="Через 90 мин", callback_data="Через 90 мин")
        keyboard_vopros12.add(btn_90)
        bot.send_message(call.message.chat.id,
                         'Доктор дал вам 3 таблетки. Вы должны принимать одну таблетку каждые полчаса. Через сколько '
                         'времени они у вас кончатся?',
                         reply_markup=keyboard_vopros12)
    if call.data == "90":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_30 : 0,5 = 60 + 10 = 70_', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros12 = types.InlineKeyboardMarkup()
        btn_20 = types.InlineKeyboardButton(text="Через 20 мин", callback_data="Через 20 мин")
        keyboard_vopros12.add(btn_20)
        btn_40 = types.InlineKeyboardButton(text="Через 40 мин", callback_data="Через 40 мин")
        keyboard_vopros12.add(btn_40)
        btn_60 = types.InlineKeyboardButton(text="Через 60 мин", callback_data="Через 60 мин")
        keyboard_vopros12.add(btn_60)
        btn_90 = types.InlineKeyboardButton(text="Через 90 мин", callback_data="Через 90 мин")
        keyboard_vopros12.add(btn_90)
        bot.send_message(call.message.chat.id,
                         'Доктор дал вам 3 таблетки. Вы должны принимать одну таблетку каждые полчаса. Через сколько '
                         'времени они у вас кончатся?',
                         reply_markup=keyboard_vopros12)
    if call.data == "70":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Верно!'
                                               '\n_30 : 0,5 = 60 + 10 = 70_', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros12 = types.InlineKeyboardMarkup()
        btn_20 = types.InlineKeyboardButton(text="Через 20 мин", callback_data="Через 20 мин")
        keyboard_vopros12.add(btn_20)
        btn_40 = types.InlineKeyboardButton(text="Через 40 мин", callback_data="Через 40 мин")
        keyboard_vopros12.add(btn_40)
        btn_60 = types.InlineKeyboardButton(text="Через 60 мин", callback_data="Через 60 мин")
        keyboard_vopros12.add(btn_60)
        btn_90 = types.InlineKeyboardButton(text="Через 90 мин", callback_data="Через 90 мин")
        keyboard_vopros12.add(btn_90)
        bot.send_message(call.message.chat.id,
                         'Доктор дал вам 3 таблетки. Вы должны принимать одну таблетку каждые полчаса. Через сколько '
                         'времени они у вас кончатся?',
                         reply_markup=keyboard_vopros12)
    # ДЕНЬ3
    # Вопрос 12
    if call.data == "Через 20 мин":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_Одну таблетку вы выпиваете сейчас, через полчаса другую и через _'
                                               '_полчаса третью...итого один час._', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros13 = types.InlineKeyboardMarkup()
        btn_ne_odnogo = types.InlineKeyboardButton(text="Ни одного", callback_data="Ни одного")
        keyboard_vopros13.add(btn_ne_odnogo)
        btn_coten = types.InlineKeyboardButton(text="Несколько сотен", callback_data="Несколько сотен")
        keyboard_vopros13.add(btn_coten)
        btn_tisyach = types.InlineKeyboardButton(text="Несколько тысяч", callback_data="Несколько тысяч")
        keyboard_vopros13.add(btn_tisyach)
        btn_d_tisyach = types.InlineKeyboardButton(text="Десятки тысяч", callback_data="Десятки тысяч")
        keyboard_vopros13.add(btn_d_tisyach)
        btn_million = types.InlineKeyboardButton(text="Около миллиона", callback_data="Около миллиона")
        keyboard_vopros13.add(btn_million)
        bot.send_message(call.message.chat.id,
                         'Сколько разных видов животных были спасены от потопа на ковчеге у Моисея '
                         '(если не знаете точно, отвечайте приблизительно)?',
                         reply_markup=keyboard_vopros13)
    if call.data == "Через 40 мин":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_Одну таблетку вы выпиваете сейчас, через полчаса другую и через _'
                                               '_полчаса третью...итого один час._', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros13 = types.InlineKeyboardMarkup()
        btn_ne_odnogo = types.InlineKeyboardButton(text="Ни одного", callback_data="Ни одного")
        keyboard_vopros13.add(btn_ne_odnogo)
        btn_coten = types.InlineKeyboardButton(text="Несколько сотен", callback_data="Несколько сотен")
        keyboard_vopros13.add(btn_coten)
        btn_tisyach = types.InlineKeyboardButton(text="Несколько тысяч", callback_data="Несколько тысяч")
        keyboard_vopros13.add(btn_tisyach)
        btn_d_tisyach = types.InlineKeyboardButton(text="Десятки тысяч", callback_data="Десятки тысяч")
        keyboard_vopros13.add(btn_d_tisyach)
        btn_million = types.InlineKeyboardButton(text="Около миллиона", callback_data="Около миллиона")
        keyboard_vopros13.add(btn_million)
        bot.send_message(call.message.chat.id,
                         'Сколько разных видов животных были спасены от потопа на ковчеге у Моисея '
                         '(если не знаете точно, отвечайте приблизительно)?',
                         reply_markup=keyboard_vopros13)
    if call.data == "Через 90 мин":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_Одну таблетку вы выпиваете сейчас, через полчаса другую и через _'
                                               '_полчаса третью...итого один час._', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros13 = types.InlineKeyboardMarkup()
        btn_ne_odnogo = types.InlineKeyboardButton(text="Ни одного", callback_data="Ни одного")
        keyboard_vopros13.add(btn_ne_odnogo)
        btn_coten = types.InlineKeyboardButton(text="Несколько сотен", callback_data="Несколько сотен")
        keyboard_vopros13.add(btn_coten)
        btn_tisyach = types.InlineKeyboardButton(text="Несколько тысяч", callback_data="Несколько тысяч")
        keyboard_vopros13.add(btn_tisyach)
        btn_d_tisyach = types.InlineKeyboardButton(text="Десятки тысяч", callback_data="Десятки тысяч")
        keyboard_vopros13.add(btn_d_tisyach)
        btn_million = types.InlineKeyboardButton(text="Около миллиона", callback_data="Около миллиона")
        keyboard_vopros13.add(btn_million)
        bot.send_message(call.message.chat.id,
                         'Сколько разных видов животных были спасены от потопа на ковчеге у Моисея '
                         '(если не знаете точно, отвечайте приблизительно)? ',
                         reply_markup=keyboard_vopros13)
    if call.data == "Через 60 мин":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Верно!'
                                               '\n_Одну таблетку вы выпиваете сейчас, через полчаса другую и через _'
                                               '_полчаса третью...итого один час._', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros13 = types.InlineKeyboardMarkup()
        btn_ne_odnogo = types.InlineKeyboardButton(text="Ни одного", callback_data="Ни одного")
        keyboard_vopros13.add(btn_ne_odnogo)
        btn_coten = types.InlineKeyboardButton(text="Несколько сотен", callback_data="Несколько сотен")
        keyboard_vopros13.add(btn_coten)
        btn_tisyach = types.InlineKeyboardButton(text="Несколько тысяч", callback_data="Несколько тысяч")
        keyboard_vopros13.add(btn_tisyach)
        btn_d_tisyach = types.InlineKeyboardButton(text="Десятки тысяч", callback_data="Десятки тысяч")
        keyboard_vopros13.add(btn_d_tisyach)
        btn_million = types.InlineKeyboardButton(text="Около миллиона", callback_data="Около миллиона")
        keyboard_vopros13.add(btn_million)
        bot.send_message(call.message.chat.id, 'Сколько разных видов животных были спасены от потопа '
                                               'на ковчеге у Моисея (если не знаете точно, отвечайте приблизительно)?',
                         reply_markup=keyboard_vopros13)
    # ДЕНЬ3
    # Вопрос 13 КОНЦОВКА
    if call.data == "Несколько сотен":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_У Моисея не было ковчега, соответственно он не спас _'
                                               '_ни одно животное...Ноев ковчег_', parse_mode="Markdown")
        time.sleep(3)
        bot.send_message(call.message.chat.id, '' + call.message.chat.first_name +
                         ', до набора новичка 🎁 тебе остался всего один шаг 💪')
        time.sleep(1)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAK53WAJXxgvMgVRIjwuwoNTGCG9Ekh2AAJvAwACz7vUDpIyjey9BupLHgQ',
                         reply_markup=const.markup_menu_poka_day3)

    if call.data == "Несколько тысяч":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_У Моисея не было ковчега, соответственно он не спас ни одно _'
                                               '_животное... Ноев ковчег_', parse_mode="Markdown")
        time.sleep(3)
        bot.send_message(call.message.chat.id, '' + call.message.chat.first_name +
                         ', до набора новичка 🎁 тебе остался всего один шаг 💪')
        time.sleep(1)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAK53WAJXxgvMgVRIjwuwoNTGCG9Ekh2AAJvAwACz7vUDpIyjey9BupLHgQ',
                         reply_markup=const.markup_menu_poka_day3)

    if call.data == "Десятки тысяч":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_У Моисея не было ковчега, соответственно он не спас ни одно _'
                                               '_животное... Ноев ковчег_', parse_mode="Markdown")
        time.sleep(3)
        bot.send_message(call.message.chat.id, '' + call.message.chat.first_name +
                         ', до набора новичка 🎁 тебе остался всего один шаг 💪')
        time.sleep(1)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAK53WAJXxgvMgVRIjwuwoNTGCG9Ekh2AAJvAwACz7vUDpIyjey9BupLHgQ',
                         reply_markup=const.markup_menu_poka_day3)

    if call.data == "Около миллиона":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_У Моисея не было ковчега, соответственно он не спас ни одно _'
                                               '_животное... Ноев ковчег_', parse_mode="Markdown")
        time.sleep(3)
        bot.send_message(call.message.chat.id, '' + call.message.chat.first_name +
                         ', до набора новичка 🎁 тебе остался всего один шаг 💪')
        time.sleep(1)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAK53WAJXxgvMgVRIjwuwoNTGCG9Ekh2AAJvAwACz7vUDpIyjey9BupLHgQ',
                         reply_markup=const.markup_menu_poka_day3)

    if call.data == "Ни одного":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Верно!'
                                               '\n_У Моисея не было ковчега, соответственно он не спас ни одно _'
                                               '_животное... Ноев ковчег_', parse_mode="Markdown")
        time.sleep(3)
        bot.send_message(call.message.chat.id,'' + call.message.chat.first_name +
                         ', до набора новичка 🎁 тебе остался всего один шаг 💪')
        time.sleep(1)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAK53WAJXxgvMgVRIjwuwoNTGCG9Ekh2AAJvAwACz7vUDpIyjey9BupLHgQ',
                         reply_markup=const.markup_menu_poka_day3)

    if call.data == "А, Б вопрос 1":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\nТы старался, это похвально. Не переживай, скоро начнется обучение, '
                                               'на котором все станет просто и понятно '
                                               '\nВерный ответ: В, Г')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б", callback_data="А, Б вопрос 2")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В", callback_data="А, В вопрос 2")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А", callback_data="А вопрос 2")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б", callback_data="Б вопрос 2")
        keyboard_vopros1.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="В", callback_data="В вопрос 2")
        keyboard_vopros1.add(btn_5)
        bot.send_message(call.message.chat.id, 'Когда клиент задает вопрос в самом начале диалога необходимо'
                                               '\nА) проигнорировать его вопрос и задать базовые уточняющие вопросы, '
                                               'которые позволяют понять суть обращения, после уже предоставить ответ '
                                               'на вопрос, если он останется актуальным '
                                               '\nБ) присоединиться в формате: '
                                               'вы обратились по адресу/я обязательно отвечу на все ваши вопросы/да я '
                                               'сейчас все вам расскажу, '
                                               'позвольте, я первоначально задам вам пару вопросов…'
                                               '\nВ) ответить сразу на вопрос обобщенно, не уточняя детали',
                         reply_markup=keyboard_vopros1)
    if call.data == "А, Г вопрос 1":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\nТы старался, это похвально. Не переживай, скоро начнется обучение, '
                                               'на котором все станет просто и понятно '
                                               '\nВерный ответ: В, Г')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б", callback_data="А, Б вопрос 2")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В", callback_data="А, В вопрос 2")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А", callback_data="А вопрос 2")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б", callback_data="Б вопрос 2")
        keyboard_vopros1.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="В", callback_data="В вопрос 2")
        keyboard_vopros1.add(btn_5)
        bot.send_message(call.message.chat.id, 'Когда клиент задает вопрос в самом начале диалога необходимо'
                                               '\nА) проигнорировать его вопрос и задать базовые уточняющие вопросы, '
                                               'которые позволяют понять суть обращения, после уже предоставить ответ '
                                               'на вопрос, если он останется актуальным '
                                               '\nБ) присоединиться в формате: '
                                               'вы обратились по адресу/я обязательно отвечу на все ваши вопросы/да я '
                                               'сейчас все вам расскажу, '
                                               'позвольте, я первоначально задам вам пару вопросов…'
                                               '\nВ) ответить сразу на вопрос обобщенно, не уточняя детали',
                         reply_markup=keyboard_vopros1)
    if call.data == "Б, В, Г вопрос 1":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\nТы старался, это похвально. Не переживай, скоро начнется обучение, '
                                               'на котором все станет просто и понятно '
                                               '\nВерный ответ: В, Г')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б", callback_data="А, Б вопрос 2")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В", callback_data="А, В вопрос 2")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А", callback_data="А вопрос 2")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б", callback_data="Б вопрос 2")
        keyboard_vopros1.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="В", callback_data="В вопрос 2")
        keyboard_vopros1.add(btn_5)
        bot.send_message(call.message.chat.id, 'Когда клиент задает вопрос в самом начале диалога необходимо'
                                               '\nА) проигнорировать его вопрос и задать базовые уточняющие вопросы, '
                                               'которые позволяют понять суть обращения, после уже предоставить ответ '
                                               'на вопрос, если он останется актуальным '
                                               '\nБ) присоединиться в формате: '
                                               'вы обратились по адресу/я обязательно отвечу на все ваши вопросы/да я '
                                               'сейчас все вам расскажу, '
                                               'позвольте, я первоначально задам вам пару вопросов…'
                                               '\nВ) ответить сразу на вопрос обобщенно, не уточняя детали',
                         reply_markup=keyboard_vopros1)
    if call.data == "В, Г вопрос 1":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKirV_1iPyj6eZEDCx1V7245tGEPpPxAAJ-AAOWn4wOcYMRnixctuUeBA')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Верно!'
                                               '\n_Изначально необходимо снять эмоциональный всплеск у клиента, _'
                                               '_дать ему возможность расслабиться и только потом переходить к тому, _'
                                               '_чтобы ему помочь. _'
                                               '_Пока человек находится в эмоциях, он не готов воспринимать _'
                                               '_информацию, _'
                                               '_анализировать ее и мыслить логически. _'
                                               '_Т.е. он не услышит вас, какое бы замечательное решение вы ему не _'
                                               '_предложили._', parse_mode="Markdown")
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б", callback_data="А, Б вопрос 2")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В", callback_data="А, В вопрос 2")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А", callback_data="А вопрос 2")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б", callback_data="Б вопрос 2")
        keyboard_vopros1.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="В", callback_data="В вопрос 2")
        keyboard_vopros1.add(btn_5)
        bot.send_message(call.message.chat.id, 'Когда клиент задает вопрос, в самом начале диалога необходимо:'
                                               '\nА) проигнорировать его вопрос и задать базовые уточняющие вопросы, '
                                               'которые позволяют понять суть обращения, после уже предоставить ответ '
                                               'на вопрос, если он останется актуальным '
                                               '\nБ) присоединиться в формате: '
                                               'вы обратились по адресу/я обязательно отвечу на все ваши вопросы/да я '
                                               'сейчас все вам расскажу, '
                                               'позвольте, я первоначально задам вам пару вопросов…'
                                               '\nВ) ответить сразу на вопрос обобщенно, не уточняя детали',
                         reply_markup=keyboard_vopros1)
    # ДЕНЬ4
    # Вопрос 2
    if call.data == "А, Б вопрос 2":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\nТы старался, это похвально. Не переживай, скоро начнется обучение, '
                                               'на котором все станет просто и понятно '
                                               '\nВерный ответ: Б')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б, В, Г", callback_data="А, Б, В, Г вопрос 3")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В, Г", callback_data="А, В, Г вопрос 3")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А, Б, Г", callback_data="А, Б, Г вопрос 3")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="А, Б, В", callback_data="А, Б, В вопрос 3")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id, 'С помощью каких инструментов клиент поймет, что вы его услышали?'
                                               '\nА) Правильно ли я вас поняла, что…'
                                               '\nБ) Вы сказали, что …, следовательно, наш товар/услуга позволит Вам…'
                                               '\nВ) ага, так, мг'
                                               '\nГ) перефразирование сказанного клиентом',
                         reply_markup=keyboard_vopros1)
    if call.data == "А, В вопрос 2":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\nТы старался, это похвально. Не переживай, скоро начнется обучение, '
                                               'на котором все станет просто и понятно '
                                               '\nВерный ответ: Б')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б, В, Г", callback_data="А, Б, В, Г вопрос 3")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В, Г", callback_data="А, В, Г вопрос 3")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А, Б, Г", callback_data="А, Б, Г вопрос 3")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="А, Б, В", callback_data="А, Б, В вопрос 3")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id, 'С помощью каких инструментов клиент поймет, что вы его услышали?'
                                               '\nА) Правильно ли я вас поняла, что…'
                                               '\nБ) Вы сказали, что …, следовательно, наш товар/услуга позволит Вам…'
                                               '\nВ) ага, так, мг'
                                               '\nГ) перефразирование сказанного клиентом',
                         reply_markup=keyboard_vopros1)
    if call.data == "А вопрос 2":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\nТы старался, это похвально. Не переживай, скоро начнется обучение, '
                                               'на котором все станет просто и понятно '
                                               '\nВерный ответ: Б')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б, В, Г", callback_data="А, Б, В, Г вопрос 3")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В, Г", callback_data="А, В, Г вопрос 3")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А, Б, Г", callback_data="А, Б, Г вопрос 3")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="А, Б, В", callback_data="А, Б, В вопрос 3")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id, 'С помощью каких инструментов клиент поймет, что вы его услышали?'
                                               '\nА) Правильно ли я вас поняла, что…'
                                               '\nБ) Вы сказали, что …, следовательно, наш товар/услуга позволит Вам…'
                                               '\nВ) ага, так, мг'
                                               '\nГ) перефразирование сказанного клиентом',
                         reply_markup=keyboard_vopros1)
    if call.data == "В вопрос 2":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\nТы старался, это похвально. Не переживай, скоро начнется обучение, '
                                               'на котором все станет просто и понятно '
                                               '\nВерный ответ: Б')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б, В, Г", callback_data="А, Б, В, Г вопрос 3")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В, Г", callback_data="А, В, Г вопрос 3")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А, Б, Г", callback_data="А, Б, Г вопрос 3")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="А, Б, В", callback_data="А, Б, В вопрос 3")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id, 'С помощью каких инструментов клиент поймет, что вы его услышали?'
                                               '\nА) Правильно ли я вас поняла, что…'
                                               '\nБ) Вы сказали, что …, следовательно, наш товар/услуга позволит Вам…'
                                               '\nВ) ага, так, мг'
                                               '\nГ) перефразирование сказанного клиентом',
                         reply_markup=keyboard_vopros1)
    if call.data == "Б вопрос 2":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKiql_1iNTyNAZydhqyDe3Fz7T09i3GAAIMAAOvxlEada4sUs9mal0eBA')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Верно!'
                                               '\n_Вопрос, на который нет однозначного ответа, _'
                                               '_т.к. нужно уточнить дополнительную информацию или_'
                                               '_(если это продажи) после которого необходимо переориентировать _'
                                               '_клиента на совместный выбор, _'
                                               '_не стоит оставлять без ответа. Однако для того, _'
                                               '_чтобы плавно перейти к уточнению или диалогу по покупке, _'
                                               '_нужно частично согласиться с клиентом, дав понять, что на его вопрос _'
                                               '_будет получен ответ, но чуть позже_', parse_mode="Markdown")
        time.sleep(7)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б, В, Г", callback_data="А, Б, В, Г вопрос 3")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В, Г", callback_data="А, В, Г вопрос 3")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А, Б, Г", callback_data="А, Б, Г вопрос 3")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="А, Б, В", callback_data="А, Б, В вопрос 3")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id, 'С помощью каких инструментов клиент поймет, что вы его услышали?'
                                               '\nА) Правильно ли я вас поняла, что…'
                                               '\nБ) Вы сказали, что …, следовательно, наш товар/услуга позволит Вам…'
                                               '\nВ) ага, так, мг'
                                               '\nГ) перефразирование сказанного клиентом',
                         reply_markup=keyboard_vopros1)
    # ДЕНЬ4
    # Вопрос 3
    if call.data == "А, В, Г вопрос 3":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\nТы старался, это похвально. Не переживай, скоро начнется обучение, '
                                               'на котором все станет просто и понятно '
                                               '\nВерный ответ: А, Б, В, Г')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="Все, кроме Б вопрос 4")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="Только А", callback_data="Только А вопрос 4")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="Все варианты верны вопрос 4")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б, Г", callback_data="Б, Г вопрос 4")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id,
                         'Какими навыками должен обладать оператор, чтобы быть клиентоориентированным?'
                         '\nА) желание помочь'
                         '\nБ) эмпатия'
                         '\nВ) настрой на поиск решения вопроса, а не препятствий'
                         '\nГ) нешаблонность общения, индивидуальный подход к каждому',
                         reply_markup=keyboard_vopros1)
    if call.data == "А, Б, Г вопрос 3":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\nТы старался, это похвально. Не переживай, скоро начнется обучение, '
                                               'на котором все станет просто и понятно '
                                               '\nВерный ответ: А, Б, В, Г')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="Все, кроме Б вопрос 4")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="Только А", callback_data="Только А вопрос 4")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="Все варианты верны вопрос 4")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б, Г", callback_data="Б, Г вопрос 4")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id,
                         'Какими навыками должен обладать оператор, чтобы быть клиентоориентированным?'
                         '\nА) желание помочь'
                         '\nБ) эмпатия'
                         '\nВ) настрой на поиск решения вопроса, а не препятствий'
                         '\nГ) нешаблонность общения, индивидуальный подход к каждому',
                         reply_markup=keyboard_vopros1)
    if call.data == "А, Б, В вопрос 3":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\nТы старался, это похвально. Не переживай, скоро начнется обучение, '
                                               'на котором все станет просто и понятно '
                                               '\nВерный ответ: А, Б, В, Г')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="Все, кроме Б вопрос 4")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="Только А", callback_data="Только А вопрос 4")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="Все варианты верны вопрос 4")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б, Г", callback_data="Б, Г вопрос 4")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id,
                         'Какими навыками должен обладать оператор, чтобы быть клиентоориентированным?'
                         '\nА) желание помочь'
                         '\nБ) эмпатия'
                         '\nВ) настрой на поиск решения вопроса, а не препятствий'
                         '\nГ) нешаблонность общения, индивидуальный подход к каждому',
                         reply_markup=keyboard_vopros1)
    if call.data == "А, Б, В, Г вопрос 3":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKipF_1iJkOYeGpyCJgq33N1iYZXWXMAALKBwAClvoSBYAPwokore4pHgQ')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Верно!')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="Все, кроме Б вопрос 4")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="Только А", callback_data="Только А вопрос 4")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="Все варианты верны вопрос 4")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б, Г", callback_data="Б, Г вопрос 4")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id,
                         'Какими навыками должен обладать оператор, чтобы быть клиентоориентированным?'
                         '\nА) желание помочь'
                         '\nБ) эмпатия'
                         '\nВ) настрой на поиск решения вопроса, а не препятствий'
                         '\nГ) нешаблонность общения, индивидуальный подход к каждому',
                         reply_markup=keyboard_vopros1)
    # ДЕНЬ4
    # Вопрос 4
    if call.data == "Все, кроме Б вопрос 4":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\n_Эмпатия - осознанное сопереживание текущему эмоциональному _'
                                               '_состоянию другого _'
                                               '_человека без потери ощущения происхождения этого переживания. _'
                                               '_Понимание эмоционального состояния другого человека и демонстрацию _'
                                               '_этого понимания_', parse_mode="Markdown")
        bot.send_photo(call.message.chat.id,
                       'https://drive.google.com/file/d/1ChZ8AjA7UnM-3L5I0GUCezB-m6dBIYs6/view?usp=sharing')
        time.sleep(3)
        bot.send_message(call.message.chat.id,
                         'Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет '
                         'просто и понятно '
                         '\nВерный ответ: Все варианты верны')
        time.sleep(10)
        keyboard_type = types.InlineKeyboardMarkup()
        btn_red = types.InlineKeyboardButton(text="Красный тип", callback_data="Красный тип. Описание")
        btn_blue = types.InlineKeyboardButton(text="Синий тип", callback_data="Синий тип. Описание")
        btn_yellow = types.InlineKeyboardButton(text="Желтый тип", callback_data="Желтый тип. Описание")
        btn_green = types.InlineKeyboardButton(text="Зеленый тип", callback_data="Зеленый тип. Описание")
        keyboard_type.add(btn_red, btn_blue)
        keyboard_type.add(btn_yellow, btn_green)
        btn_answer = types.InlineKeyboardButton(text="Перейти к ответам без прочтения",
                                                callback_data="Перейти к ответам без прочтения")
        keyboard_type.add(btn_answer)
        bot.send_message(call.message.chat.id, 'Есть одна из типологий клиентов DISK.'
                                               '\nОна поможет вам  понимать отличительные особенности клиентов и '
                                               'выбирать правильные стратегии общения с каждым из них:  '
                                               'быстро расположить клиента, избежать конфликтов с ним, а '
                                               'также понять закономерности его поведения.'
                                               '\nСогласно этой теории мы условно делим клиентов по следующим '
                                               'признакам: '
                                               '\n✅степень выраженности лидерских качеств: '
                                               '\n       ведомый/ведущий'
                                               '\n✅склонность полагаться на логику/эмоции'
                                               '\n'
                                               '\n‼*Ведущий/ведомый.*'
                                               '\n'
                                               '\n1⃣Ведущий тип поведения выражается активностью, решительностью в '
                                               'поведении. '
                                               'Он сам выбирает товары/услуги, точно знает, что именно он хочет '
                                               'купить/уточнить, '
                                               'и какие качества для него принципиальны. Эти люди демонстрируют '
                                               'выраженные '
                                               'лидерские качества, часто занимают руководящие позиции.'
                                               '\n'
                                               '\n2⃣Ведомый тип  поведения означает, что такому человеку необходима '
                                               'внешняя поддержка при принятии важных решений.'
                                               'Они часто приходят выбирать товары с родственниками или друзьями и '
                                               'активно с ними советуются. Если они пришли одни – они часто '
                                               'ориентируются '
                                               'на мнение продавца/консультанта, который должен помочь сделать выбор, '
                                               'поддержать принятое решение или решить вопрос.'
                                               '\n'
                                               '\n‼*Логика/эмоции.*'
                                               '\n'
                                               '\n1⃣Клиент, который более склонен к логичному поведению, '
                                               'будет в большей степени интересоваться фактическими характеристиками '
                                               'товара. '
                                               'Он часто занимает экспертную позицию в общении, демонстрирует хорошее '
                                               'знание '
                                               'товара/услуги и требует от продавца/консультанта того же самого'
                                               '\n'
                                               '\n2⃣На клиента - эмоцию в большей степени влияет именно '
                                               'эмоциональность '
                                               'и яркость подачи информации. Он в большей степени оценивает не сам '
                                               'товар/услугу, а то, как он преподнесен. В данном случае ораторские '
                                               'качества продавца/консультанта играют решающую роль.',
                         parse_mode="Markdown", reply_markup=keyboard_type)
    if call.data == "Только А вопрос 4":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\n_Эмпатия - осознанное сопереживание текущему эмоциональному _'
                                               '_состоянию другого _'
                                               '_человека без потери ощущения происхождения этого переживания. _'
                                               '_Понимание эмоционального состояния другого человека и демонстрацию _'
                                               '_этого понимания_', parse_mode="Markdown")
        bot.send_photo(call.message.chat.id,
                       'https://drive.google.com/file/d/1ChZ8AjA7UnM-3L5I0GUCezB-m6dBIYs6/view?usp=sharing')
        time.sleep(3)
        bot.send_message(call.message.chat.id,
                         'Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет '
                         'просто и понятно '
                         '\nВерный ответ: Все варианты верны')
        time.sleep(5)
        keyboard_type = types.InlineKeyboardMarkup()
        btn_red = types.InlineKeyboardButton(text="Красный тип", callback_data="Красный тип. Описание")
        btn_blue = types.InlineKeyboardButton(text="Синий тип", callback_data="Синий тип. Описание")
        btn_yellow = types.InlineKeyboardButton(text="Желтый тип", callback_data="Желтый тип. Описание")
        btn_green = types.InlineKeyboardButton(text="Зеленый тип", callback_data="Зеленый тип. Описание")
        keyboard_type.add(btn_red, btn_blue)
        keyboard_type.add(btn_yellow, btn_green)
        btn_answer = types.InlineKeyboardButton(text="Перейти к ответам без прочтения",
                                                callback_data="Перейти к ответам без прочтения")
        keyboard_type.add(btn_answer)
        bot.send_message(call.message.chat.id, 'Есть одна из типологий клиентов DISK.'
                                               '\nОна поможет вам  понимать отличительные особенности клиентов и '
                                               'выбирать правильные стратегии общения с каждым из них:  '
                                               'быстро расположить клиента, избежать конфликтов с ним, а '
                                               'также понять закономерности его поведения.'
                                               '\nСогласно этой теории мы условно делим клиентов по следующим '
                                               'признакам: '
                                               '\n✅степень выраженности лидерских качеств: '
                                               '\n       ведомый/ведущий'
                                               '\n✅склонность полагаться на логику/эмоции'
                                               '\n'
                                               '\n‼*Ведущий/ведомый.*'
                                               '\n'
                                               '\n1⃣Ведущий тип поведения выражается активностью, решительностью в '
                                               'поведении. '
                                               'Он сам выбирает товары/услуги, точно знает, что именно он хочет '
                                               'купить/уточнить, '
                                               'и какие качества для него принципиальны. Эти люди демонстрируют '
                                               'выраженные '
                                               'лидерские качества, часто занимают руководящие позиции.'
                                               '\n'
                                               '\n2⃣Ведомый тип  поведения означает, что такому человеку необходима '
                                               'внешняя поддержка при принятии важных решений.'
                                               'Они часто приходят выбирать товары с родственниками или друзьями и '
                                               'активно с ними советуются. Если они пришли одни – они часто '
                                               'ориентируются '
                                               'на мнение продавца/консультанта, который должен помочь сделать выбор, '
                                               'поддержать принятое решение или решить вопрос.'
                                               '\n'
                                               '\n‼*Логика/эмоции.*'
                                               '\n'
                                               '\n1⃣Клиент, который более склонен к логичному поведению, '
                                               'будет в большей степени интересоваться фактическими характеристиками '
                                               'товара. '
                                               'Он часто занимает экспертную позицию в общении, демонстрирует хорошее '
                                               'знание '
                                               'товара/услуги и требует от продавца/консультанта того же самого'
                                               '\n'
                                               '\n2⃣На клиента - эмоцию в большей степени влияет именно '
                                               'эмоциональность '
                                               'и яркость подачи информации. Он в большей степени оценивает не сам '
                                               'товар/услугу, а то, как он преподнесен. В данном случае ораторские '
                                               'качества продавца/консультанта играют решающую роль.',
                         parse_mode="Markdown", reply_markup=keyboard_type)
    if call.data == "Б, Г вопрос 4":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно! 🦉'
                                               '\n_Эмпатия - осознанное сопереживание текущему эмоциональному _'
                                               '_состоянию другого _'
                                               '_человека без потери ощущения происхождения этого переживания. _'
                                               '_Понимание эмоционального состояния другого человека и демонстрацию _'
                                               '_этого понимания_', parse_mode="Markdown")
        bot.send_photo(call.message.chat.id,
                       'https://drive.google.com/file/d/1ChZ8AjA7UnM-3L5I0GUCezB-m6dBIYs6/view?usp=sharing')
        time.sleep(3)
        bot.send_message(call.message.chat.id,
                         'Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет '
                         'просто и понятно '
                         '\nВерный ответ: Все варианты верны')
        time.sleep(5)
        keyboard_type = types.InlineKeyboardMarkup()
        btn_red = types.InlineKeyboardButton(text="Красный тип", callback_data="Красный тип. Описание")
        btn_blue = types.InlineKeyboardButton(text="Синий тип", callback_data="Синий тип. Описание")
        btn_yellow = types.InlineKeyboardButton(text="Желтый тип", callback_data="Желтый тип. Описание")
        btn_green = types.InlineKeyboardButton(text="Зеленый тип", callback_data="Зеленый тип. Описание")
        keyboard_type.add(btn_red, btn_blue)
        keyboard_type.add(btn_yellow, btn_green)
        btn_answer = types.InlineKeyboardButton(text="Перейти к ответам без прочтения",
                                                callback_data="Перейти к ответам без прочтения")
        keyboard_type.add(btn_answer)
        bot.send_message(call.message.chat.id, 'Есть одна из типологий клиентов DISK.'
                                               '\nОна поможет вам  понимать отличительные особенности клиентов и '
                                               'выбирать правильные стратегии общения с каждым из них:  '
                                               'быстро расположить клиента, избежать конфликтов с ним, а '
                                               'также понять закономерности его поведения.'
                                               '\nСогласно этой теории мы условно делим клиентов по следующим '
                                               'признакам: '
                                               '\n✅степень выраженности лидерских качеств: '
                                               '\n       ведомый/ведущий'
                                               '\n✅склонность полагаться на логику/эмоции'
                                               '\n'
                                               '\n‼*Ведущий/ведомый.*'
                                               '\n'
                                               '\n1⃣Ведущий тип поведения выражается активностью, решительностью в '
                                               'поведении. '
                                               'Он сам выбирает товары/услуги, точно знает, что именно он хочет '
                                               'купить/уточнить, '
                                               'и какие качества для него принципиальны. Эти люди демонстрируют '
                                               'выраженные '
                                               'лидерские качества, часто занимают руководящие позиции.'
                                               '\n'
                                               '\n2⃣Ведомый тип  поведения означает, что такому человеку необходима '
                                               'внешняя поддержка при принятии важных решений.'
                                               'Они часто приходят выбирать товары с родственниками или друзьями и '
                                               'активно с ними советуются. Если они пришли одни – они часто '
                                               'ориентируются '
                                               'на мнение продавца/консультанта, который должен помочь сделать выбор, '
                                               'поддержать принятое решение или решить вопрос.'
                                               '\n'
                                               '\n‼*Логика/эмоции.*'
                                               '\n'
                                               '\n1⃣Клиент, который более склонен к логичному поведению, '
                                               'будет в большей степени интересоваться фактическими характеристиками '
                                               'товара. '
                                               'Он часто занимает экспертную позицию в общении, демонстрирует хорошее '
                                               'знание '
                                               'товара/услуги и требует от продавца/консультанта того же самого'
                                               '\n'
                                               '\n2⃣На клиента - эмоцию в большей степени влияет именно '
                                               'эмоциональность '
                                               'и яркость подачи информации. Он в большей степени оценивает не сам '
                                               'товар/услугу, а то, как он преподнесен. В данном случае ораторские '
                                               'качества продавца/консультанта играют решающую роль.',
                         parse_mode="Markdown", reply_markup=keyboard_type)
    if call.data == "Все варианты верны вопрос 4":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAK6mGAKghw0DhcatrGd8yPyI-Yo4hRWAAJFAAOYv4ANNNnchGya6lseBA')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Верно! 🦉'
                                               '\n_Клиентоориентированность – это способность компании и сотрудников _'
                                               '_вовремя определять желания клиентов, чтобы удовлетворить их своей _'
                                               '_продукцией или услугой с максимальной выгодой. _'
                                               '\n_То есть с развитием культуры потребления, покупатели хотели не _'
                                               '_просто получить товар, но сделать это с максимальным комфортом._',
                         parse_mode="Markdown")
        time.sleep(10)
        keyboard_type = types.InlineKeyboardMarkup()
        btn_red = types.InlineKeyboardButton(text="Красный тип", callback_data="Красный тип. Описание")
        btn_blue = types.InlineKeyboardButton(text="Синий тип", callback_data="Синий тип. Описание")
        btn_yellow = types.InlineKeyboardButton(text="Желтый тип", callback_data="Желтый тип. Описание")
        btn_green = types.InlineKeyboardButton(text="Зеленый тип", callback_data="Зеленый тип. Описание")
        keyboard_type.add(btn_red, btn_blue)
        keyboard_type.add(btn_yellow, btn_green)
        btn_answer = types.InlineKeyboardButton(text="Перейти к ответам без прочтения",
                                                callback_data="Перейти к ответам без прочтения")
        keyboard_type.add(btn_answer)
        bot.send_message(call.message.chat.id, 'Есть одна из типологий клиентов DISK.'
                                               '\nОна поможет вам  понимать отличительные особенности клиентов и '
                                               'выбирать правильные стратегии общения с каждым из них:  '
                                               'быстро расположить клиента, избежать конфликтов с ним, а '
                                               'также понять закономерности его поведения.'
                                               '\nСогласно этой теории мы условно делим клиентов по следующим '
                                               'признакам: '
                                               '\n✅степень выраженности лидерских качеств: '
                                               '\n       ведомый/ведущий'
                                               '\n✅склонность полагаться на логику/эмоции'
                                               '\n'
                                               '\n‼*Ведущий/ведомый.*'
                                               '\n'
                                               '\n1⃣Ведущий тип поведения выражается активностью, решительностью в '
                                               'поведении. '
                                               'Он сам выбирает товары/услуги, точно знает, что именно он хочет '
                                               'купить/уточнить, '
                                               'и какие качества для него принципиальны. Эти люди демонстрируют '
                                               'выраженные '
                                               'лидерские качества, часто занимают руководящие позиции.'
                                               '\n'
                                               '\n2⃣Ведомый тип  поведения означает, что такому человеку необходима '
                                               'внешняя поддержка при принятии важных решений.'
                                               'Они часто приходят выбирать товары с родственниками или друзьями и '
                                               'активно с ними советуются. Если они пришли одни – они часто '
                                               'ориентируются '
                                               'на мнение продавца/консультанта, который должен помочь сделать выбор, '
                                               'поддержать принятое решение или решить вопрос.'
                                               '\n'
                                               '\n‼*Логика/эмоции.*'
                                               '\n'
                                               '\n1⃣Клиент, который более склонен к логичному поведению, '
                                               'будет в большей степени интересоваться фактическими характеристиками '
                                               'товара. '
                                               'Он часто занимает экспертную позицию в общении, демонстрирует хорошее '
                                               'знание '
                                               'товара/услуги и требует от продавца/консультанта того же самого'
                                               '\n'
                                               '\n2⃣На клиента - эмоцию в большей степени влияет именно '
                                               'эмоциональность '
                                               'и яркость подачи информации. Он в большей степени оценивает не сам '
                                               'товар/услугу, а то, как он преподнесен. В данном случае ораторские '
                                               'качества продавца/консультанта играют решающую роль.',
                         parse_mode="Markdown", reply_markup=keyboard_type)
    if call.data == "Красный тип. Описание":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_type = types.InlineKeyboardMarkup()
        btn_blue = types.InlineKeyboardButton(text="Синий тип", callback_data="Синий тип. Описание")
        btn_yellow = types.InlineKeyboardButton(text="Желтый тип", callback_data="Желтый тип. Описание")
        btn_green = types.InlineKeyboardButton(text="Зеленый тип", callback_data="Зеленый тип. Описание")
        keyboard_type.add(btn_blue)
        keyboard_type.add(btn_yellow)
        keyboard_type.add(btn_green)
        btn_answer = types.InlineKeyboardButton(text="Перейти к ответам без прочтения",
                                                callback_data="Перейти к ответам без прочтения")
        keyboard_type.add(btn_answer)
        bot.send_message(call.message.chat.id, 'Красный тип (ведущий/эмоциональный)'
                                               '\n'
                                               '\nЯвный лидер, который характеризуется уверенным поведением и '
                                               'ориентацией на достижение цели. '
                                               'Главное для него – получить желаемое любой ценой. '
                                               'Они предпринимают решительные действия для того, '
                                               'чтобы добиться желаемого результата. '
                                               'При этом красные принимают решения самостоятельно, и на него слабо '
                                               'влияет мнение окружающих. '
                                               'Это очень энергичные люди, которые часто занимают руководящие '
                                               'должности. '
                                               '\nПри этом они не всегда логичны, могут быть импульсивны, иногда '
                                               'непоследовательны. '
                                               'Они часто опираются не на факты, а на эмоции и субъективные '
                                               'впечатления. '
                                               '\nЧто можно ожидать от клиентов красного типа:'
                                               '\nЧасто «перехватывают» инициативу в общении с '
                                               'продавцом/консультантом '
                                               '\nБольше обращают внимание на степень уверенности '
                                               'продавца/консультана '
                                               ' и манеру подачи товара/услуги, нежели на технические подробности'
                                               '\nИногда высказывают возражения, '
                                               'чтобы просто проверить уверенность продавца\консультанта в '
                                               'товаре/услуге'
                                               '\nМогут очень напористо требовать дополнительные скидки и бонусы'
                                               '\nБыстро принимают решения'
                                               '\nУпрямы, их тяжело переубедить в чем-либо'
                                               '\n'
                                               '\nЗадача продавца/консультанта: уверенная, убедительная, '
                                               'эмоционально окрашенная презентация ', reply_markup=keyboard_type)
    if call.data == "Синий тип. Описание":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_type = types.InlineKeyboardMarkup()
        btn_red = types.InlineKeyboardButton(text="Красный тип", callback_data="Красный тип. Описание")
        btn_yellow = types.InlineKeyboardButton(text="Желтый тип", callback_data="Желтый тип. Описание")
        btn_green = types.InlineKeyboardButton(text="Зеленый тип", callback_data="Зеленый тип. Описание")
        keyboard_type.add(btn_red)
        keyboard_type.add(btn_yellow)
        keyboard_type.add(btn_green)
        btn_answer = types.InlineKeyboardButton(text="Перейти к ответам без прочтения",
                                                callback_data="Перейти к ответам без прочтения")
        keyboard_type.add(btn_answer)
        bot.send_message(call.message.chat.id, 'Синий тип (ведущий/логичный)'
                                               '\nЭтот тип отличается в первую очередь своей логичностью и '
                                               'рациональностью. '
                                               'Они вдумчивые, практичные, стремятся заранее просчитать последствия '
                                               'своих решений. '
                                               'Они также являются ведущим типом, то есть при принятии решений они '
                                               'опираются не на мнение окружающих, а на итоги своих умозаключений. '
                                               'Они ведут себя достаточно сдержанно, предпочитают спокойную '
                                               'обстановку в общении без чрезмерных эмоций.'
                                               '\nЧто можно ожидать от клиентов синего типа:'
                                               '\nСтремятся просчитать выгоду от покупки/услуги'
                                               '\nОбращают внимание на фактические характеристики товара/услуги и их '
                                               'преимущества, а не на эмоциональность презентации '
                                               '\nЧасто берут паузу для того, чтобы сравнить товар/услугу с '
                                               'аналогичными товарами конкурентов '
                                               '\nИзбегают общения с чрезмерно напористыми продавцами/консультантами'
                                               '\n'
                                               '\nЗадача продавца/консультанта: идеальное знание характеристик '
                                               'товара, '
                                               'умение проводить аргументированную сравнительную характеристику и '
                                               'описывать выгоды от приобретения. ', reply_markup=keyboard_type)
    if call.data == "Желтый тип. Описание":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_type = types.InlineKeyboardMarkup()
        btn_red = types.InlineKeyboardButton(text="Красный тип", callback_data="Красный тип. Описание")
        btn_blue = types.InlineKeyboardButton(text="Синий тип", callback_data="Синий тип. Описание")
        btn_green = types.InlineKeyboardButton(text="Зеленый тип", callback_data="Зеленый тип. Описание")
        keyboard_type.add(btn_red)
        keyboard_type.add(btn_blue)
        keyboard_type.add(btn_green)
        btn_answer = types.InlineKeyboardButton(text="Перейти к ответам без прочтения",
                                                callback_data="Перейти к ответам без прочтения")
        keyboard_type.add(btn_answer)
        bot.send_message(call.message.chat.id, 'Желтый тип (ведомый/эмоциональный)'
                                               '\nЭто очень открытые, живые, эмоциональные люди, которые любят '
                                               'общение с окружающими. '
                                               'Они любят быть в центре внимания, и всеми силами стараются это '
                                               'внимание привлечь. '
                                               'Они любят все новое, интересное и уникальное. При этом их внимание '
                                               'неустойчиво, '
                                               ' то есть их интерес может быстро возникнуть и также быстро угаснуть.'
                                               '\nЭтот тип в силу неустойчивости своего внимания и ориентации на '
                                               'окружающих '
                                               'относится к ведомым, то есть окружающие достаточно сильно влияют на '
                                               'их мнение. '
                                               'Они могут быстро изменить свое мнение в результате общения, '
                                               'могут быстро '
                                               'загореться новой идеей, которую им интересно преподнесли.'
                                               '\nЧто ожидать от клиентов желтого типа:'
                                               '\nМогут быть чрезмерно общительными'
                                               '\nМогут быстро терять интерес к товару/услуге'
                                               '\nМогут быть непоследовательны'
                                               '\n'
                                               '\nЗадача продавца/консультанта: презентация с упором на уникальность '
                                               'товара, '
                                               'активная помощь в выборе наиболее подходящего варианта.',
                         reply_markup=keyboard_type)
    if call.data == "Зеленый тип. Описание":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        keyboard_type = types.InlineKeyboardMarkup()
        btn_red = types.InlineKeyboardButton(text="Красный тип", callback_data="Красный тип. Описание")
        btn_blue = types.InlineKeyboardButton(text="Синий тип", callback_data="Синий тип. Описание")
        btn_yellow = types.InlineKeyboardButton(text="Желтый тип", callback_data="Желтый тип. Описание")
        keyboard_type.add(btn_red)
        keyboard_type.add(btn_blue)
        keyboard_type.add(btn_yellow)
        btn_answer = types.InlineKeyboardButton(text="Перейти к ответам без прочтения",
                                                callback_data="Перейти к ответам без прочтения")
        keyboard_type.add(btn_answer)
        bot.send_message(call.message.chat.id, 'Зеленый тип (ведомый/логичный)'
                                               '\nДанный тип отличается тем, что они достаточно консервативны, '
                                               'они стремятся максимальное количество раз перепроверить свое решение '
                                               'и избежать возможных ошибок.  Они относятся к ведомому типу потому, '
                                               'что они придают большое значение общественному мнению, советам друзей '
                                               'и родственников. Перед тем, как принять решение, они стремятся '
                                               'посоветоваться со всеми компетентными в данном вопросе знакомыми и '
                                               'только после этого сделать выбор. '
                                               '\nКроме того, зеленый тип очень ценит искренность и душевность '
                                               'общения, '
                                               'а также стремится создать максимально комфортные условия для '
                                               'окружающих. '
                                               '\nЧто ожидать от клиентов зеленого типа:'
                                               '\nПри выборе часто опирается на мнение окружающих'
                                               '\nНуждаются в поддержке выбора'
                                               '\nСтараются не принимать поспешных решений'
                                               '\n'
                                               '\nЗадача продавца/консультанта: теплое и доброжелательное общение, '
                                               'презентация с акцентом на добротность товара/услуги, помощь и '
                                               'поддержка при выборе',
                         reply_markup=keyboard_type)
    # ДЕНЬ4
    # Вопрос 5
    if call.data == "Перейти к ответам без прочтения":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'В следующих вопросах нужно определить к какому типу относится клент.')
        time.sleep(2)
        keyboard_vopros5 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный вопрос 5")
        keyboard_vopros5.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий вопрос 5")
        keyboard_vopros5.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый вопрос 5")
        keyboard_vopros5.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый вопрос 5")
        keyboard_vopros5.add(btn_4)
        bot.send_message(call.message.chat.id, 'Сообщает, что уже пересмотрел не одно видео, полазил по всем сайтам, '
                                               'представленным в РБ, уточнил у нескольких друзей, которые уже успели '
                                               'приобрести '
                                               'своим детям электромобили, все нюансы эксплуатации и на что необходимо '
                                               'обратить особое внимание. Приводит информацию с других сайтов, '
                                               'просит сравнить с нашим предложением. При завершении диалога '
                                               'озвучивает, '
                                               'что ждет звонка от еще одного друга, вот он точно в этом плане '
                                               'эксперт, '
                                               '3 машинки купил уже своему ребенку, а после примет решение',
                         reply_markup=keyboard_vopros5)
    # ДЕНЬ4
    # Вопрос 6
    if call.data == "красный вопрос 5":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Верный ответ: *Зеленый тип* 🦉'
                                               '\n_Они относятся к ведомому типу потому, что они придают большое _'
                                               '_значение общественному мнению, советам друзей и родственников. _'
                                               '_Перед тем, как принять решение, они стремятся посоветоваться со _'
                                               '_всеми компетентными в данном вопросе знакомыми и только после _'
                                               '_этого сделать выбор._', parse_mode="Markdown")
        time.sleep(7)
        keyboard_vopros6 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный вопрос 6")
        keyboard_vopros6.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий вопрос 6")
        keyboard_vopros6.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый вопрос 6")
        keyboard_vopros6.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый вопрос 6")
        keyboard_vopros6.add(btn_4)
        bot.send_message(call.message.chat.id, 'Следующий вопрос:'
                                               '\nХочет сдать анализы на аллергены, с врачом не консультировался, '
                                               'прочитал в сети несколько статей, сделал выводы, что ему это '
                                               'необходимо. '
                                               'Настаивает на полной панели, не дает оператору объяснить, '
                                               'чем они отличаются друг от друга. Говорит, что ему положена скидка, '
                                               'ведь он же планирует сделать целый комплекс анализов. '
                                               'Спрашивает, насколько вы уверены в достоверности анализов именно '
                                               'вашей лаборатории. Где можно ознакомиться с подтверждающей это '
                                               'информацией. '
                                               'А пользовались ли вы сами услугами лаборатории? На ответ нет, звучит: '
                                               'хм, видимо не так уж и хороши. Удивлен, когда узнает, что врач '
                                               'медицинского офиса не расшифрует ему результаты. Настаивает, '
                                               'чтобы для него было исключение. После очень быстро переходит на '
                                               'уточнение '
                                               'адреса ближайшего офиса и прощается',
                         reply_markup=keyboard_vopros6)
    if call.data == "синий вопрос 5":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Верный ответ: *Зеленый тип* 🦉'
                                               '\n_Они относятся к ведомому типу потому, что они придают большое _'
                                               '_значение общественному мнению, советам друзей и родственников. _'
                                               '_Перед тем, как принять решение, они стремятся посоветоваться со _'
                                               '_всеми компетентными в данном вопросе знакомыми и только после _'
                                               '_этого сделать выбор._', parse_mode="Markdown")
        time.sleep(7)
        keyboard_vopros6 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный вопрос 6")
        keyboard_vopros6.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий вопрос 6")
        keyboard_vopros6.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый вопрос 6")
        keyboard_vopros6.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый вопрос 6")
        keyboard_vopros6.add(btn_4)
        bot.send_message(call.message.chat.id, 'Следующий вопрос:'
                                               '\nХочет сдать анализы на аллергены, с врачом не консультировался, '
                                               'прочитал в сети несколько статей, сделал выводы, что ему это '
                                               'необходимо. '
                                               'Настаивает на полной панели, не дает оператору объяснить, '
                                               'чем они отличаются друг от друга. Говорит, что ему положена скидка, '
                                               'ведь он же планирует сделать целый комплекс анализов. '
                                               'Спрашивает, насколько вы уверены в достоверности анализов именно '
                                               'вашей лаборатории. Где можно ознакомиться с подтверждающей это '
                                               'информацией. '
                                               'А пользовались ли вы сами услугами лаборатории? На ответ нет, звучит: '
                                               'хм, видимо не так уж и хороши. Удивлен, когда узнает, что врач '
                                               'медицинского офиса не расшифрует ему результаты. Настаивает, '
                                               'чтобы для него было исключение. После очень быстро переходит на '
                                               'уточнение '
                                               'адреса ближайшего офиса и прощается',
                         reply_markup=keyboard_vopros6)
    if call.data == "желтый вопрос 5":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Верный ответ: *Зеленый тип* 🦉'
                                               '\n_Они относятся к ведомому типу потому, что они придают большое _'
                                               '_значение общественному мнению, советам друзей и родственников. _'
                                               '_Перед тем, как принять решение, они стремятся посоветоваться со _'
                                               '_всеми компетентными в данном вопросе знакомыми и только после _'
                                               '_этого сделать выбор._', parse_mode="Markdown")
        time.sleep(7)
        keyboard_vopros6 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный вопрос 6")
        keyboard_vopros6.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий вопрос 6")
        keyboard_vopros6.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый вопрос 6")
        keyboard_vopros6.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый6")
        keyboard_vopros6.add(btn_4)
        bot.send_message(call.message.chat.id, 'Следующий вопрос:'
                                               '\nХочет сдать анализы на аллергены, с врачом не консультировался, '
                                               'прочитал в сети несколько статей, сделал выводы, что ему это '
                                               'необходимо. '
                                               'Настаивает на полной панели, не дает оператору объяснить, '
                                               'чем они отличаются друг от друга. Говорит, что ему положена скидка, '
                                               'ведь он же планирует сделать целый комплекс анализов. '
                                               'Спрашивает, насколько вы уверены в достоверности анализов именно '
                                               'вашей лаборатории. Где можно ознакомиться с подтверждающей это '
                                               'информацией. '
                                               'А пользовались ли вы сами услугами лаборатории? На ответ нет, звучит: '
                                               'хм, видимо не так уж и хороши. Удивлен, когда узнает, что врач '
                                               'медицинского офиса не расшифрует ему результаты. Настаивает, '
                                               'чтобы для него было исключение. После очень быстро переходит на '
                                               'уточнение '
                                               'адреса ближайшего офиса и прощается',
                         reply_markup=keyboard_vopros6)
    if call.data == "зеленый вопрос 5":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id,
                         'CAACAgIAAxkBAAKim1_1iD0jYgod3SHkT_HGjKZ__QQsAAKKAQACECECEHDFOWrqWWPTHgQ')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Молодец!')
        time.sleep(2)
        keyboard_vopros6 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный вопрос 6")
        keyboard_vopros6.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий вопрос 6")
        keyboard_vopros6.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый вопрос 6")
        keyboard_vopros6.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый вопрос 6")
        keyboard_vopros6.add(btn_4)
        bot.send_message(call.message.chat.id, 'Хочет сдать анализы на аллергены, с врачом не консультировался, '
                                               'прочитал в сети несколько статей, сделал выводы, что ему это '
                                               'необходимо. '
                                               'Настаивает на полной панели, не дает оператору объяснить, '
                                               'чем они отличаются друг от друга. Говорит, что ему положена скидка, '
                                               'ведь он же планирует сделать целый комплекс анализов. '
                                               'Спрашивает, насколько вы уверены в достоверности анализов именно '
                                               'вашей лаборатории. Где можно ознакомиться с подтверждающей это '
                                               'информацией. '
                                               'А пользовались ли вы сами услугами лаборатории? На ответ нет, звучит: '
                                               'хм, видимо не так уж и хороши. Удивлен, когда узнает, что врач '
                                               'медицинского офиса не расшифрует ему результаты. Настаивает, '
                                               'чтобы для него было исключение. После очень быстро переходит на '
                                               'уточнение '
                                               'адреса ближайшего офиса и прощается',
                         reply_markup=keyboard_vopros6)
    # ДЕНЬ4
    # Вопрос 7
    if call.data == "зеленый вопрос 6":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Верный ответ: *Красный тип* 🦉'
                                               '\n_Они явный лидер, которые характеризуются уверенным поведением _'
                                               '_и ориентацией на достижение цели._'
                                               '_ Главное для них – получить желаемое любой ценой._',
                         parse_mode="Markdown")
        time.sleep(7)
        keyboard_vopros7 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный вопрос 7")
        keyboard_vopros7.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий вопрос 7")
        keyboard_vopros7.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый вопрос 7")
        keyboard_vopros7.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый вопрос 7")
        keyboard_vopros7.add(btn_4)
        bot.send_message(call.message.chat.id, 'При исходящем звонке говорит, как же вам повезло, '
                                               'что вы попали именно на нее. Ведь она так любит поболтать. '
                                               'Параллельно сообщает коллегам, что видите, мобильный оператор '
                                               'звонит именно мне предложить новые условия пользования, а не кому-то '
                                               'из вас. '
                                               'Начинает расспрашивать про новинку в тарифах, есть ли такая услуга и '
                                               'у нас. '
                                               'С удовольствием бы подключила себе. Когда слышит, что такой нет, '
                                               'но есть другая, '
                                               'которая дает те же преимущества, то слушает очень внимательно, '
                                               'но не более минуты, после отвлекается на разговоры по работе шепотом, '
                                               'при этом не кладя трубку. После того, как вы напоминаете о том. '
                                               'Что это уникальное предложение лишь для нее, задает пару '
                                               'вопросов и соглашается на изменение перечня услуг в ее тарифном плане',
                         reply_markup=keyboard_vopros7)
    if call.data == "синий вопрос 6":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Верный ответ: *Красный тип* 🦉'
                                               '\n_Они явный лидер, которые характеризуются уверенным поведением _'
                                               '_и ориентацией на достижение цели._'
                                               '_ Главное для них – получить желаемое любой ценой._',
                         parse_mode="Markdown")
        time.sleep(7)
        keyboard_vopros7 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный вопрос 7")
        keyboard_vopros7.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий вопрос 7")
        keyboard_vopros7.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый вопрос 7")
        keyboard_vopros7.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый вопрос 7")
        keyboard_vopros7.add(btn_4)
        bot.send_message(call.message.chat.id, 'При исходящем звонке говорит, как же вам повезло, '
                                               'что вы попали именно на нее. Ведь она так любит поболтать. '
                                               'Параллельно сообщает коллегам, что видите, мобильный оператор '
                                               'звонит именно мне предложить новые условия пользования, а не кому-то '
                                               'из вас. '
                                               'Начинает расспрашивать про новинку в тарифах, есть ли такая услуга и '
                                               'у нас. '
                                               'С удовольствием бы подключила себе. Когда слышит, что такой нет, '
                                               'но есть другая, '
                                               'которая дает те же преимущества, то слушает очень внимательно, '
                                               'но не более минуты, после отвлекается на разговоры по работе шепотом, '
                                               'при этом не кладя трубку. После того, как вы напоминаете о том. '
                                               'Что это уникальное предложение лишь для нее, задает пару '
                                               'вопросов и соглашается на изменение перечня услуг в ее тарифном плане',
                         reply_markup=keyboard_vopros7)
    if call.data == "желтый вопрос 6":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Верный ответ: *Красный тип* 🦉'
                                               '\n_Они явный лидер, которые характеризуются уверенным поведением _'
                                               '_и ориентацией на достижение цели._'
                                               '_ Главное для них – получить желаемое любой ценой._',
                         parse_mode="Markdown")
        time.sleep(7)
        keyboard_vopros7 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный вопрос 7")
        keyboard_vopros7.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий вопрос 7")
        keyboard_vopros7.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый вопрос 7")
        keyboard_vopros7.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый вопрос 7")
        keyboard_vopros7.add(btn_4)
        bot.send_message(call.message.chat.id, 'При исходящем звонке говорит, как же вам повезло, '
                                               'что вы попали именно на нее. Ведь она так любит поболтать. '
                                               'Параллельно сообщает коллегам, что видите, мобильный оператор '
                                               'звонит именно мне предложить новые условия пользования, а не кому-то '
                                               'из вас. '
                                               'Начинает расспрашивать про новинку в тарифах, есть ли такая услуга и '
                                               'у нас. '
                                               'С удовольствием бы подключила себе. Когда слышит, что такой нет, '
                                               'но есть другая, '
                                               'которая дает те же преимущества, то слушает очень внимательно, '
                                               'но не более минуты, после отвлекается на разговоры по работе шепотом, '
                                               'при этом не кладя трубку. После того, как вы напоминаете о том. '
                                               'Что это уникальное предложение лишь для нее, задает пару '
                                               'вопросов и соглашается на изменение перечня услуг в ее тарифном плане',
                         reply_markup=keyboard_vopros7)
    if call.data == "красный вопрос 6":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id, 'CAACAgEAAxkBAAKimF_1iAw1UDknn8P73j3ZHQo3lHwkAAIiAAM4DoIR3jA0x7O3d2QeBA')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Молодец!')
        time.sleep(2)
        keyboard_vopros7 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный вопрос 7")
        keyboard_vopros7.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий вопрос 7")
        keyboard_vopros7.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый вопрос 7")
        keyboard_vopros7.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый вопрос 7")
        keyboard_vopros7.add(btn_4)
        bot.send_message(call.message.chat.id, 'При исходящем звонке говорит, как же вам повезло, '
                                               'что вы попали именно на нее. Ведь она так любит поболтать. '
                                               'Параллельно сообщает коллегам, что видите, мобильный оператор '
                                               'звонит именно мне предложить новые условия пользования, а не кому-то '
                                               'из вас. '
                                               'Начинает расспрашивать про новинку в тарифах, есть ли такая услуга и '
                                               'у нас. '
                                               'С удовольствием бы подключила себе. Когда слышит, что такой нет, '
                                               'но есть другая, '
                                               'которая дает те же преимущества, то слушает очень внимательно, '
                                               'но не более минуты, после отвлекается на разговоры по работе шепотом, '
                                               'при этом не кладя трубку. После того, как вы напоминаете о том. '
                                               'Что это уникальное предложение лишь для нее, задает пару '
                                               'вопросов и соглашается на изменение перечня услуг в ее тарифном плане',
                         reply_markup=keyboard_vopros7)
    # ДЕНЬ4
    # Вопрос 8
    if call.data == "зеленый вопрос 7":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Верный ответ: *Желтый тип* 🦉'
                                               '\n_Они любят быть в центре внимания, и всеми силами стараются это _'
                                               '_внимание привлечь. Они любят все новое, интересное и уникальное. _'
                                               '_При этом их внимание неустойчиво._', parse_mode="Markdown")
        time.sleep(7)
        keyboard_vopros8 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный вопрос 8")
        keyboard_vopros8.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий вопрос 8")
        keyboard_vopros8.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый вопрос 8")
        keyboard_vopros8.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый вопрос 8")
        keyboard_vopros8.add(btn_4)
        bot.send_message(call.message.chat.id, 'В чат обращается клиент, чья посылка ему еще не пришла, '
                                               'срок озвученный изначально специалистом при заполнении заявки '
                                               'истекает сегодня. '
                                               'Он спрашивает, где находится посылка, какова вероятность того, '
                                               'что ему доставят ее сегодня домой, уточняет может ли он сам забрать с '
                                               'пункта выдачи, несмотря на то, что выбирал услугу доставки курьером, '
                                               'будет ли возврат разницы между заказанными услугами, как долго может '
                                               'быть задержка в приезде курьера, учитывая, что посылка уже в его '
                                               'городе. '
                                               'Прописывает свои выводы на основе услышанных ответов, понимает, '
                                               'что товар ему нужен до выходных, а уверенности в доставке до указанных '
                                               'сроков нет. Следовательно, учитывая, что доплата за курьера '
                                               'незначительная, '
                                               'принимает решение приехать самому забрать посылку сегодня. '
                                               'Но предлагает подумать о скидке для него в следующий раз'
                                               ' с учетом сложившейся ситуации, т.к. задержи произошли из-за компании',
                         reply_markup=keyboard_vopros8)
    if call.data == "синий вопрос 7":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Верный ответ: *Желтый тип* 🦉'
                                               '\n_Они любят быть в центре внимания, и всеми силами стараются это _'
                                               '_внимание привлечь. Они любят все новое, интересное и уникальное. _'
                                               '_При этом их внимание неустойчиво._', parse_mode="Markdown")
        time.sleep(7)
        keyboard_vopros8 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный вопрос 8")
        keyboard_vopros8.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий вопрос 8")
        keyboard_vopros8.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый вопрос 8")
        keyboard_vopros8.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый вопрос 8")
        keyboard_vopros8.add(btn_4)
        bot.send_message(call.message.chat.id, 'В чат обращается клиент, чья посылка ему еще не пришла, '
                                               'срок озвученный изначально специалистом при заполнении заявки '
                                               'истекает сегодня. '
                                               'Он спрашивает, где находится посылка, какова вероятность того, '
                                               'что ему доставят ее сегодня домой, уточняет может ли он сам забрать с '
                                               'пункта выдачи, несмотря на то, что выбирал услугу доставки курьером, '
                                               'будет ли возврат разницы между заказанными услугами, как долго может '
                                               'быть задержка в приезде курьера, учитывая, что посылка уже в его '
                                               'городе. '
                                               'Прописывает свои выводы на основе услышанных ответов, понимает, '
                                               'что товар ему нужен до выходных, а уверенности в доставке до указанных '
                                               'сроков нет. Следовательно, учитывая, что доплата за курьера '
                                               'незначительная, '
                                               'принимает решение приехать самому забрать посылку сегодня. '
                                               'Но предлагает подумать о скидке для него в следующий раз'
                                               ' с учетом сложившейся ситуации, т.к. задержи произошли из-за компании',
                         reply_markup=keyboard_vopros8)
    if call.data == "красный вопрос 7":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Верный ответ: *Желтый тип* 🦉'
                                               '\n_Они любят быть в центре внимания, и всеми силами стараются это _'
                                               '_внимание привлечь. Они любят все новое, интересное и уникальное. _'
                                               '_При этом их внимание неустойчиво._', parse_mode="Markdown")
        time.sleep(7)
        keyboard_vopros8 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный вопрос 8")
        keyboard_vopros8.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий вопрос 8")
        keyboard_vopros8.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый вопрос 8")
        keyboard_vopros8.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый вопрос 8")
        keyboard_vopros8.add(btn_4)
        bot.send_message(call.message.chat.id, 'В чат обращается клиент, чья посылка ему еще не пришла, '
                                               'срок озвученный изначально специалистом при заполнении заявки '
                                               'истекает сегодня. '
                                               'Он спрашивает, где находится посылка, какова вероятность того, '
                                               'что ему доставят ее сегодня домой, уточняет может ли он сам забрать с '
                                               'пункта выдачи, несмотря на то, что выбирал услугу доставки курьером, '
                                               'будет ли возврат разницы между заказанными услугами, как долго может '
                                               'быть задержка в приезде курьера, учитывая, что посылка уже в его '
                                               'городе. '
                                               'Прописывает свои выводы на основе услышанных ответов, понимает, '
                                               'что товар ему нужен до выходных, а уверенности в доставке до указанных '
                                               'сроков нет. Следовательно, учитывая, что доплата за курьера '
                                               'незначительная, '
                                               'принимает решение приехать самому забрать посылку сегодня. '
                                               'Но предлагает подумать о скидке для него в следующий раз'
                                               ' с учетом сложившейся ситуации, т.к. задержи произошли из-за компании',
                         reply_markup=keyboard_vopros8)
    if call.data == "желтый вопрос 7":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAKilV_1h-5NMqKm_T81lUs9hGtQRTHEAAIGAAOvxlEans7u-Fup_foeBA')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Молодец!')
        time.sleep(2)
        keyboard_vopros8 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный вопрос 8")
        keyboard_vopros8.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий вопрос 8")
        keyboard_vopros8.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый вопрос 8")
        keyboard_vopros8.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый вопрос 8")
        keyboard_vopros8.add(btn_4)
        bot.send_message(call.message.chat.id, 'В чат обращается клиент, чья посылка ему еще не пришла, '
                                               'срок озвученный изначально специалистом при заполнении заявки '
                                               'истекает сегодня. '
                                               'Он спрашивает, где находится посылка, какова вероятность того, '
                                               'что ему доставят ее сегодня домой, уточняет может ли он сам забрать с '
                                               'пункта выдачи, несмотря на то, что выбирал услугу доставки курьером, '
                                               'будет ли возврат разницы между заказанными услугами, как долго может '
                                               'быть задержка в приезде курьера, учитывая, что посылка уже в его '
                                               'городе. '
                                               'Прописывает свои выводы на основе услышанных ответов, понимает, '
                                               'что товар ему нужен до выходных, а уверенности в доставке до указанных '
                                               'сроков нет. Следовательно, учитывая, что доплата за курьера '
                                               'незначительная, '
                                               'принимает решение приехать самому забрать посылку сегодня. '
                                               'Но предлагает подумать о скидке для него в следующий раз'
                                               ' с учетом сложившейся ситуации, т.к. задержи произошли из-за компании',
                         reply_markup=keyboard_vopros8)
    # ДЕНЬ4
    # Вопрос 9
    if call.data == "зеленый вопрос 8":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Верный ответ: *Синий тип* 🦉'
                                               '\n_Они вдумчивые, практичные, стремятся заранее просчитать _'
                                               '_последствия своих решений. Они также являются ведущим типом, _'
                                               '_то есть при принятии решений они опираются не на мнение_'
                                               '_ окружающих, а на итоги своих умозаключений._', parse_mode="Markdown")
        time.sleep(7)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Посмотреть видео",
                                                url="https://drive.google.com/file/d/1IBiABfqv"
                                                    "i6YnswWn2Z40YUWQeT_YhWb_/view?usp=sharing")
        keyboard.add(url_button)
        bot.send_message(call.message.chat.id, 'Хм, ну что ж, теперь ты умеешь определять с каким клиентом как '
                                               'себя лучше вести, к старту обучения в проект ты уже готов)'
                                               '\nОдин из наших наставников подготовил видео-разбор звонка. Думаю, '
                                               'тебе будет полезно его посмотреть  😎', reply_markup=keyboard)
        time.sleep(10)
        bot.send_message(call.message.chat.id, 'Напоследок по традиции несколько вопросов на логику.')
        time.sleep(2)
        keyboard_vopros9 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="1", callback_data="1 коза")
        keyboard_vopros9.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="5", callback_data="5 коз")
        keyboard_vopros9.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="7", callback_data="7 коз")
        keyboard_vopros9.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="8", callback_data="8 коз")
        keyboard_vopros9.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="9", callback_data="9 коз")
        keyboard_vopros9.add(btn_5)
        bot.send_message(call.message.chat.id,
                         'У фермера было 17 коз, из них все кроме 9 погибли от чумы. Сколько у него их осталось?',
                         reply_markup=keyboard_vopros9)
    if call.data == "желтый вопрос 8":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Верный ответ: *Синий тип* 🦉'
                                               '\n_Они вдумчивые, практичные, стремятся заранее просчитать _'
                                               '_последствия своих решений. Они также являются ведущим типом, _'
                                               '_то есть при принятии решений они опираются не на мнение_'
                                               '_ окружающих, а на итоги своих умозаключений._', parse_mode="Markdown")
        time.sleep(7)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Посмотреть видео",
                                                url="https://drive.google.com/file/d/1IBiABfqv"
                                                    "i6YnswWn2Z40YUWQeT_YhWb_/view?usp=sharing")
        keyboard.add(url_button)
        bot.send_message(call.message.chat.id, 'Хм, ну что ж, теперь ты умеешь определять с каким клиентом как '
                                               'себя лучше вести, к старту обучения в проект ты уже готов)'
                                               '\nОдин из наших наставников подготовил видео-разбор звонка. Думаю, '
                                               'тебе будет полезно его посмотреть  😎', reply_markup=keyboard)
        time.sleep(10)
        bot.send_message(call.message.chat.id, 'Напоследок по традиции несколько вопросов на логику.')
        time.sleep(2)
        keyboard_vopros9 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="1", callback_data="1 коза")
        keyboard_vopros9.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="5", callback_data="5 коз")
        keyboard_vopros9.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="7", callback_data="7 коз")
        keyboard_vopros9.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="8", callback_data="8 коз")
        keyboard_vopros9.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="9", callback_data="9 коз")
        keyboard_vopros9.add(btn_5)
        bot.send_message(call.message.chat.id,
                         'У фермера было 17 коз, из них все кроме 9 погибли от чумы. Сколько у него их осталось?',
                         reply_markup=keyboard_vopros9)
    if call.data == "красный вопрос 8":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Верный ответ: *Синий тип* 🦉'
                                               '\n_Они вдумчивые, практичные, стремятся заранее просчитать _'
                                               '_последствия своих решений. Они также являются ведущим типом, _'
                                               '_то есть при принятии решений они опираются не на мнение_'
                                               '_ окружающих, а на итоги своих умозаключений._', parse_mode="Markdown")
        time.sleep(7)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Посмотреть видео",
                                                url="https://drive.google.com/file/d/1IBiABf"
                                                    "qvi6YnswWn2Z40YUWQeT_YhWb_/view?usp=sharing")
        keyboard.add(url_button)
        bot.send_message(call.message.chat.id, 'Хм, ну что ж, теперь ты умеешь определять с каким клиентом как '
                                               'себя лучше вести, к старту обучения в проект ты уже готов)'
                                               '\nОдин из наших наставников подготовил видео-разбор звонка. Думаю, '
                                               'тебе будет полезно его посмотреть  😎', reply_markup=keyboard)
        time.sleep(10)
        bot.send_message(call.message.chat.id, 'Напоследок по традиции несколько вопросов на логику.')
        time.sleep(2)
        keyboard_vopros9 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="1", callback_data="1 коза")
        keyboard_vopros9.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="5", callback_data="5 коз")
        keyboard_vopros9.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="7", callback_data="7 коз")
        keyboard_vopros9.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="8", callback_data="8 коз")
        keyboard_vopros9.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="9", callback_data="9 коз")
        keyboard_vopros9.add(btn_5)
        bot.send_message(call.message.chat.id,
                         'У фермера было 17 коз, из них все кроме 9 погибли от чумы. Сколько у него их осталось?',
                         reply_markup=keyboard_vopros9)
    if call.data == "синий вопрос 8":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAKikl_1h8BSPRlysksnVmLmtm7sQA_OAAITAAPANk8TqrOH9384yqUeBA')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Молодец!')
        time.sleep(2)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Посмотреть видео",
                                                url="https://drive.google.com/file/d/1IBi"
                                                    "ABfqvi6YnswWn2Z40YUWQeT_YhWb_/view?usp=sharing")
        keyboard.add(url_button)
        bot.send_message(call.message.chat.id, 'Хм, ну что ж, теперь ты умеешь определять с каким клиентом как '
                                               'себя лучше вести, к старту обучения в проект ты уже готов)'
                                               '\nОдин из наших наставников подготовил видео-разбор звонка. Думаю, '
                                               'тебе будет полезно его посмотреть  😎', reply_markup=keyboard)
        time.sleep(10)
        bot.send_message(call.message.chat.id, 'Напоследок по традиции несколько вопросов на логику.')
        time.sleep(2)
        keyboard_vopros9 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="1", callback_data="1 коза")
        keyboard_vopros9.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="5", callback_data="5 коз")
        keyboard_vopros9.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="7", callback_data="7 коз")
        keyboard_vopros9.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="8", callback_data="8 коз")
        keyboard_vopros9.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="9", callback_data="9 коз")
        keyboard_vopros9.add(btn_5)
        bot.send_message(call.message.chat.id,
                         'У фермера было 17 коз, из них все кроме 9 погибли от чумы. Сколько у него их осталось?',
                         reply_markup=keyboard_vopros9)
    # ДЕНЬ4
    # Вопрос 10
    if call.data == "1 коза":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_9, так как погибли все, кроме девяти_', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros10 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="9 лет", callback_data="9 лет")
        keyboard_vopros10.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="2 года", callback_data="2 года")
        keyboard_vopros10.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="1 год", callback_data="1 год")
        keyboard_vopros10.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="6 месяцев", callback_data="6 месяцев")
        keyboard_vopros10.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="11 лет", callback_data="11 лет")
        keyboard_vopros10.add(btn_5)
        bot.send_message(call.message.chat.id,
                         'Двум братьям вместе 11 лет. Один из них на 10 лет старше другого. Сколько лет младшему?',
                         reply_markup=keyboard_vopros10)
    if call.data == "5 коз":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_9, так как погибли все, кроме девяти_', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros10 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="9 лет", callback_data="9 лет")
        keyboard_vopros10.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="2 года", callback_data="2 года")
        keyboard_vopros10.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="1 год", callback_data="1 год")
        keyboard_vopros10.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="6 месяцев", callback_data="6 месяцев")
        keyboard_vopros10.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="11 лет", callback_data="11 лет")
        keyboard_vopros10.add(btn_5)
        bot.send_message(call.message.chat.id,
                         'Двум братьям вместе 11 лет. Один из них на 10 лет старше другого. Сколько лет младшему?',
                         reply_markup=keyboard_vopros10)
    if call.data == "7 коз":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_9, так как погибли все, кроме девяти_', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros10 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="9 лет", callback_data="9 лет")
        keyboard_vopros10.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="2 года", callback_data="2 года")
        keyboard_vopros10.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="1 год", callback_data="1 год")
        keyboard_vopros10.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="6 месяцев", callback_data="6 месяцев")
        keyboard_vopros10.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="11 лет", callback_data="11 лет")
        keyboard_vopros10.add(btn_5)
        bot.send_message(call.message.chat.id,
                         'Двум братьям вместе 11 лет. Один из них на 10 лет старше другого. Сколько лет младшему?',
                         reply_markup=keyboard_vopros10)
    if call.data == "8 коз":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_9, так как погибли все, кроме девяти_', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros10 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="9 лет", callback_data="9 лет")
        keyboard_vopros10.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="2 года", callback_data="2 года")
        keyboard_vopros10.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="1 год", callback_data="1 год")
        keyboard_vopros10.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="6 месяцев", callback_data="6 месяцев")
        keyboard_vopros10.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="11 лет", callback_data="11 лет")
        keyboard_vopros10.add(btn_5)
        bot.send_message(call.message.chat.id,
                         'Двум братьям вместе 11 лет. Один из них на 10 лет старше другого. Сколько лет младшему?',
                         reply_markup=keyboard_vopros10)
    if call.data == "9 коз":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAKij1_1h4mG2tEXFq-OWM3-AueQBArjAALZAANWnb0K0ZJm0tJjB6geBA')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Верно!'
                                               '\n_9, так как погибли все, кроме девяти_', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros10 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="9 лет", callback_data="9 лет")
        keyboard_vopros10.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="2 года", callback_data="2 года")
        keyboard_vopros10.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="1 год", callback_data="1 год")
        keyboard_vopros10.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="6 месяцев", callback_data="6 месяцев")
        keyboard_vopros10.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="11 лет", callback_data="11 лет")
        keyboard_vopros10.add(btn_5)
        bot.send_message(call.message.chat.id,
                         'Двум братьям вместе 11 лет. Один из них на 10 лет старше другого. Сколько лет младшему?',
                         reply_markup=keyboard_vopros10)
    # ДЕНЬ4
    # Вопрос 11
    if call.data == "9 лет":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_6 месяцев. Его брату 10 с половиной лет. _'
                                               '_Если бы младшему брату был один год, то старшему было бы _'
                                               '_одиннадцать, _'
                                               '_соответственно вместе им было бы 12 лет_', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros11 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="В США", callback_data="В США")
        keyboard_vopros11.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="В Мексике", callback_data="В Мексике")
        keyboard_vopros11.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="На границе", callback_data="На границе")
        keyboard_vopros11.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="В зависимости от национальности",
                                           callback_data="В зависимости от национальности")
        keyboard_vopros11.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="Нигде", callback_data="Нигде")
        keyboard_vopros11.add(btn_5)
        bot.send_message(call.message.chat.id,
                         'Самолет, летевший из США в Мексику, разбился ровно на границе между этими двумя странами. '
                         'Где похоронят выживших?',
                         reply_markup=keyboard_vopros11)
    if call.data == "2 года":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_6 месяцев. Его брату 10 с половиной лет. _'
                                               '_Если бы младшему брату был один год, то старшему было бы _'
                                               '_одиннадцать, _'
                                               '_соответственно вместе им было бы 12 лет_', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros11 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="В США", callback_data="В США")
        keyboard_vopros11.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="В Мексике", callback_data="В Мексике")
        keyboard_vopros11.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="На границе", callback_data="На границе")
        keyboard_vopros11.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="В зависимости от национальности",
                                           callback_data="В зависимости от национальности")
        keyboard_vopros11.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="Нигде", callback_data="Нигде")
        keyboard_vopros11.add(btn_5)
        bot.send_message(call.message.chat.id,
                         'Самолет, летевший из США в Мексику, разбился ровно на границе между этими двумя странами. '
                         'Где похоронят выживших?',
                         reply_markup=keyboard_vopros11)
    if call.data == "1 год":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_6 месяцев. Его брату 10 с половиной лет. _'
                                               '_Если бы младшему брату был один год, то старшему было бы _'
                                               '_одиннадцать, _'
                                               '_соответственно вместе им было бы 12 лет_', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros11 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="В США", callback_data="В США")
        keyboard_vopros11.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="В Мексике", callback_data="В Мексике")
        keyboard_vopros11.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="На границе", callback_data="На границе")
        keyboard_vopros11.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="В зависимости от национальности",
                                           callback_data="В зависимости от национальности")
        keyboard_vopros11.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="Нигде", callback_data="Нигде")
        keyboard_vopros11.add(btn_5)
        bot.send_message(call.message.chat.id,
                         'Самолет, летевший из США в Мексику, разбился ровно на границе между этими двумя странами. '
                         'Где похоронят выживших?',
                         reply_markup=keyboard_vopros11)
    if call.data == "11 лет":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_6 месяцев. Его брату 10 с половиной лет. _'
                                               '_Если бы младшему брату был один год, то старшему было бы _'
                                               '_одиннадцать, _'
                                               '_соответственно вместе им было бы 12 лет_', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros11 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="В США", callback_data="В США")
        keyboard_vopros11.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="В Мексике", callback_data="В Мексике")
        keyboard_vopros11.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="На границе", callback_data="На границе")
        keyboard_vopros11.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="В зависимости от национальности",
                                           callback_data="В зависимости от национальности")
        keyboard_vopros11.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="Нигде", callback_data="Нигде")
        keyboard_vopros11.add(btn_5)
        bot.send_message(call.message.chat.id,
                         'Самолет, летевший из США в Мексику, разбился ровно на границе между этими двумя странами. '
                         'Где похоронят выживших?',
                         reply_markup=keyboard_vopros11)
    if call.data == "6 месяцев":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAKijF_1hzq0J-CPHimxxZwJxnqyRwWWAAISAAP3F4Erq1mdGtkjKYUeBA')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Верно!'
                                               '\n_6 месяцев. Его брату 10 с половиной лет. _'
                                               '_Если бы младшему брату был один год, то старшему было бы _'
                                               '_одиннадцать, _'
                                               '_соответственно вместе им было бы 12 лет_', parse_mode="Markdown")
        time.sleep(1)
        keyboard_vopros11 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="В США", callback_data="В США")
        keyboard_vopros11.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="В Мексике", callback_data="В Мексике")
        keyboard_vopros11.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="На границе", callback_data="На границе")
        keyboard_vopros11.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="В зависимости от национальности",
                                           callback_data="В зависимости от национальности")
        keyboard_vopros11.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="Нигде", callback_data="Нигде")
        keyboard_vopros11.add(btn_5)
        bot.send_message(call.message.chat.id,
                         'Самолет, летевший из США в Мексику, разбился ровно на границе между этими двумя странами. '
                         'Где похоронят выживших?',
                         reply_markup=keyboard_vopros11)
    # ДЕНЬ4
    # КОНЕЦ
    if call.data == "В США":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_Нигде. Выживших не хоронят, их откачивают!_', parse_mode="Markdown")
        time.sleep(3)
        bot.send_message(call.message.chat.id, '' + call.message.chat.first_name +
                         ', спасибо тебе за продуктивную работу ☺'
                         '\nЖдем тебя в нашем Учебном центре 🤗')
        time.sleep(1)
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAK54GAJYLJm_hI8LcRvkakQEh0w7xw6AA'
                                               'JfAwACz7vUDh2-xX5QXp1vHgQ')
    if call.data == "В Мексике":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_Нигде. Выживших не хоронят, их откачивают!_', parse_mode="Markdown")
        time.sleep(3)
        bot.send_message(call.message.chat.id, '' + call.message.chat.first_name +
                         ', спасибо тебе за продуктивную работу ☺'
                         '\nЖдем тебя в нашем Учебном центре 🤗')
        time.sleep(1)
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAK54GAJYLJm_hI8LcRvkakQEh0w7xw6AAJfA'
                                               'wACz7vUDh2-xX5QXp1vHgQ')
    if call.data == "На границе":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_Нигде. Выживших не хоронят, их откачивают!_', parse_mode="Markdown")
        time.sleep(3)
        bot.send_message(call.message.chat.id, '' + call.message.chat.first_name +
                         ', спасибо тебе за продуктивную работу ☺'
                         '\nЖдем тебя в нашем Учебном центре 🤗')
        time.sleep(1)
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAK54GAJYLJm_hI8LcRvkakQEh0w7xw6AAJfAwACz7vU'
                                               'Dh2-xX5QXp1vHgQ')
    if call.data == "В зависимости от национальности":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n_Нигде. Выживших не хоронят, их откачивают!_', parse_mode="Markdown")
        time.sleep(3)
        bot.send_message(call.message.chat.id, '' + call.message.chat.first_name +
                         ', спасибо тебе за продуктивную работу ☺'
                         '\nЖдем тебя в нашем Учебном центре 🤗')
        time.sleep(1)
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAK54GAJYLJm_hI8LcRvkakQEh0w7xw6AAJfAwACz7'
                                               'vUDh2-xX5QXp1vHgQ')
    if call.data == "Нигде":
        tg_analytic.statistics(call.message.chat.first_name, call.data)
        bot.send_message(call.message.chat.id, 'Верно!'
                                               '\n_Выживших не хоронят, их откачивают!_', parse_mode="Markdown")
        time.sleep(3)
        bot.send_message(call.message.chat.id, '' + call.message.chat.first_name +
                         ', спасибо тебе за продуктивную работу ☺'
                         '\nЖдем тебя в нашем Учебном центре 🤗')
        time.sleep(1)
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAK54GAJYLJm_hI8LcRvkakQEh0w7xw6AAJfAwACz7vU'
                                               'Dh2-xX5QXp1vHgQ')


bot.polling(none_stop=True)
