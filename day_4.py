import telebot
import const
from telebot import types
import time

TOKEN = '1261241070:AAGxM_bK_Mk19Eit0rFF8WHk84fpwVPGfFA' # полученный у @BotFather
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def day4_start_message(message):
    bot.send_message(message.chat.id,
                         'Привет! Сегодня наше захватывающее путешествие подходит к концу, '
                         'но именно поэтому я подготовил для тебя самые интересные задания. Поехали!')
    time.sleep(2)
    keyboard_vopros1 = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(text="А, Б", callback_data="А, Б")
    keyboard_vopros1.add(btn_1)
    btn_2 = types.InlineKeyboardButton(text="В, Г", callback_data="В, Г")
    keyboard_vopros1.add(btn_2)
    btn_3 = types.InlineKeyboardButton(text="А, Г", callback_data="А, Г")
    keyboard_vopros1.add(btn_3)
    btn_4 = types.InlineKeyboardButton(text="Б, В, Г", callback_data="Б, В, Г")
    keyboard_vopros1.add(btn_4)
    bot.send_message(message.chat.id, 'Какие инструменты необходимо использовать, '
                                      'когда клиент демонстрирует негативную эмоцию (агрессию, раздражение, разочарование, недоверие и т.д.)'
                                      '\n А) сделать вид, что не заметил и продолжать задавать уточняющие вопросы'
                                      '\n Б) озвучить эмоцию и попросить клиента реагировать спокойнее'
                                      '\n В) понимание: суть метода показать, что клиент имеет право на эмоцию, это нормально, особенно когда его ожидания не оправданы'
                                      '\n Г) сожаление: если клиенту доставлен дискомфорт',
                     reply_markup=keyboard_vopros1)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
# Вопрос 1: Какие инструменты необходимо использовать, когда клиент демонстрирует негативную эмоцию (агрессию, раздражение, разочарование, недоверие и т.д.)
    if call.data == "А, Б":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет просто и понятно'
                                               '\n Верный ответ: В, Г')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б", callback_data="А, Б")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В", callback_data="А, В")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А", callback_data="А")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б", callback_data="Б")
        keyboard_vopros1.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="В", callback_data="В")
        keyboard_vopros1.add(btn_5)
        bot.send_message(call.message.chat.id, 'Когда клиент задает вопрос в самом начале диалога необходимо'
                                          '\n А) проигнорировать его вопрос и задать базовые уточняющие вопросы, '
                                               'которые позволяют понять суть обращения, после уже предоставить ответ на вопрос, если он останется актуальным'
                                          '\n Б) присоединиться в формате: '
                                               'вы обратились по адресу/я обязательно отвечу на все ваши вопросы/да я сейчас все вам расскажу, '
                                               'позвольте я первоначально задам вам пару вопросов…'
                                          '\n В) ответить сразу на вопрос обобщенно, не уточняя детали',
                         reply_markup=keyboard_vopros1)
    if call.data == "А, Г":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет просто и понятно'
                                               '\n Верный ответ: В, Г')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б", callback_data="А, Б")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В", callback_data="А, В")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А", callback_data="А")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б", callback_data="Б")
        keyboard_vopros1.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="В", callback_data="В")
        keyboard_vopros1.add(btn_5)
        bot.send_message(call.message.chat.id, 'Когда клиент задает вопрос в самом начале диалога необходимо'
                                          '\n А) проигнорировать его вопрос и задать базовые уточняющие вопросы, '
                                               'которые позволяют понять суть обращения, после уже предоставить ответ на вопрос, если он останется актуальным'
                                          '\n Б) присоединиться в формате: '
                                               'вы обратились по адресу/я обязательно отвечу на все ваши вопросы/да я сейчас все вам расскажу, '
                                               'позвольте я первоначально задам вам пару вопросов…'
                                          '\n В) ответить сразу на вопрос обобщенно, не уточняя детали',
                         reply_markup=keyboard_vopros1)
    if call.data == "Б, В, Г":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет просто и понятно'
                                               '\n Верный ответ: В, Г')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б", callback_data="А, Б")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В", callback_data="А, В")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А", callback_data="А")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б", callback_data="Б")
        keyboard_vopros1.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="В", callback_data="В")
        keyboard_vopros1.add(btn_5)
        bot.send_message(call.message.chat.id, 'Когда клиент задает вопрос в самом начале диалога необходимо'
                                          '\n А) проигнорировать его вопрос и задать базовые уточняющие вопросы, '
                                               'которые позволяют понять суть обращения, после уже предоставить ответ на вопрос, если он останется актуальным'
                                          '\n Б) присоединиться в формате: '
                                               'вы обратились по адресу/я обязательно отвечу на все ваши вопросы/да я сейчас все вам расскажу, '
                                               'позвольте я первоначально задам вам пару вопросов…'
                                          '\n В) ответить сразу на вопрос обобщенно, не уточняя детали',
                         reply_markup=keyboard_vopros1)
    if call.data == "В, Г":
        bot.send_message(call.message.chat.id, 'Верно!'
                                               '\n Изначально необходимо снять эмоциональный всплеск у клиента, '
                                               'дать ему возможность расслабится и только потом переходить к тому, чтобы ему помочь. '
                                               'Пока человек находиться в эмоциях он не готов воспринимать информацию, '
                                               'анализировать ее и мыслить логически. '
                                               'Т.е. он не услышит вас, какое бы замечательное решение вы ему не предложили')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б", callback_data="А, Б")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В", callback_data="А, В")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А", callback_data="А")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б", callback_data="Б")
        keyboard_vopros1.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="В", callback_data="В")
        keyboard_vopros1.add(btn_5)
        bot.send_message(call.message.chat.id, 'Когда клиент задает вопрос в самом начале диалога необходимо'
                                          '\n А) проигнорировать его вопрос и задать базовые уточняющие вопросы, '
                                               'которые позволяют понять суть обращения, после уже предоставить ответ на вопрос, если он останется актуальным'
                                          '\n Б) присоединиться в формате: '
                                               'вы обратились по адресу/я обязательно отвечу на все ваши вопросы/да я сейчас все вам расскажу, '
                                               'позвольте я первоначально задам вам пару вопросов…'
                                          '\n В) ответить сразу на вопрос обобщенно, не уточняя детали',
                         reply_markup=keyboard_vopros1)
# Вопрос 2:	Когда клиент задает вопрос в самом начале диалога необходимо
    if call.data == "А, Б":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет просто и понятно'
                                               '\n Верный ответ: Б')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б, В, Г", callback_data="А, Б, В, Г")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В, Г", callback_data="А, В, Г")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А, Б, Г", callback_data="А, Б, Г")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="А, Б, В", callback_data="А, Б, В")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id, 'С помощью каких инструментов клиент поймет, что вы его услышали'
                                          '\n А) Правильно ли я вас поняла, что…'
                                          '\n Б) Вы сказали, что …, следовательно, наш товар/услуга позволит Вам…'
                                          '\n В) ага, так, мг'
                                          '\n Г) перефразирование сказанного клиентом',
                         reply_markup=keyboard_vopros1)
    if call.data == "А, В":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет просто и понятно'
                                               '\n Верный ответ: Б')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б, В, Г", callback_data="А, Б, В, Г")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В, Г", callback_data="А, В, Г")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А, Б, Г", callback_data="А, Б, Г")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="А, Б, В", callback_data="А, Б, В")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id, 'С помощью каких инструментов клиент поймет, что вы его услышали'
                                          '\n А) Правильно ли я вас поняла, что…'
                                          '\n Б) Вы сказали, что …, следовательно, наш товар/услуга позволит Вам…'
                                          '\n В) ага, так, мг'
                                          '\n Г) перефразирование сказанного клиентом',
                         reply_markup=keyboard_vopros1)
    if call.data == "А":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет просто и понятно'
                                               '\n Верный ответ: Б')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б, В, Г", callback_data="А, Б, В, Г")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В, Г", callback_data="А, В, Г")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А, Б, Г", callback_data="А, Б, Г")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="А, Б, В", callback_data="А, Б, В")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id, 'С помощью каких инструментов клиент поймет, что вы его услышали'
                                          '\n А) Правильно ли я вас поняла, что…'
                                          '\n Б) Вы сказали, что …, следовательно, наш товар/услуга позволит Вам…'
                                          '\n В) ага, так, мг'
                                          '\n Г) перефразирование сказанного клиентом',
                         reply_markup=keyboard_vopros1)
    if call.data == "В":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет просто и понятно'
                                               '\n Верный ответ: Б')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б, В, Г", callback_data="А, Б, В, Г")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В, Г", callback_data="А, В, Г")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А, Б, Г", callback_data="А, Б, Г")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="А, Б, В", callback_data="А, Б, В")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id, 'С помощью каких инструментов клиент поймет, что вы его услышали'
                                          '\n А) Правильно ли я вас поняла, что…'
                                          '\n Б) Вы сказали, что …, следовательно, наш товар/услуга позволит Вам…'
                                          '\n В) ага, так, мг'
                                          '\n Г) перефразирование сказанного клиентом',
                         reply_markup=keyboard_vopros1)
    if call.data == "Б":
        bot.send_message(call.message.chat.id, 'Верно!'
                                               '\n Вопрос, на который нет однозначного ответа, '
                                               'т.к. нужно уточнить дополнительную информацию или'
                                               ' (если это продажи) после которого необходимо переориентировать клиента на совместный выбор, '
                                               'не стоит оставлять без ответа. Однако для того, '
                                               'чтобы плавно перейти к уточнению или диалогу по покупке, '
                                               'нужно частично согласиться с клиентом, дав понять, что на его вопрос будет получен ответ, но чуть позже')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="А, Б, В, Г", callback_data="А, Б, В, Г")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="А, В, Г", callback_data="А, В, Г")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="А, Б, Г", callback_data="А, Б, Г")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="А, Б, В", callback_data="А, Б, В")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id, 'С помощью каких инструментов клиент поймет, что вы его услышали'
                                          '\n А) Правильно ли я вас поняла, что…'
                                          '\n Б) Вы сказали, что …, следовательно, наш товар/услуга позволит Вам…'
                                          '\n В) ага, так, мг'
                                          '\n Г) перефразирование сказанного клиентом',
                         reply_markup=keyboard_vopros1)
# Вопрос 3:	С помощью каких инструментов клиент поймет, что вы его услышали
    if call.data == "А, В, Г":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет просто и понятно'
                                               '\n Верный ответ: А, Б, В, Г')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="Все, кроме Б")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="Только А", callback_data="Только А")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="Все варианты верны")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б, Г", callback_data="Б, Г")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id, 'Какими навыками должен обладать оператор, чтобы быть клиентоориентированным'
                                          '\n А) желание помочь'
                                          '\n Б) эмпатия'
                                          '\n В) настрой на поиск решения вопроса, а не препятствий'
                                          '\n Г) нешаблонность общения, индивидуальный подход к каждому',
                         reply_markup=keyboard_vopros1)
    if call.data == "А, Б, Г":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет просто и понятно'
                                               '\n Верный ответ: А, Б, В, Г')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="Все, кроме Б")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="Только А", callback_data="Только А")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="Все варианты верны")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б, Г", callback_data="Б, Г")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id, 'Какими навыками должен обладать оператор, чтобы быть клиентоориентированным'
                                          '\n А) желание помочь'
                                          '\n Б) эмпатия'
                                          '\n В) настрой на поиск решения вопроса, а не препятствий'
                                          '\n Г) нешаблонность общения, индивидуальный подход к каждому',
                         reply_markup=keyboard_vopros1)
    if call.data == "А, Б, В":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет просто и понятно'
                                               '\n Верный ответ: А, Б, В, Г')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="Все, кроме Б")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="Только А", callback_data="Только А")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="Все варианты верны")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б, Г", callback_data="Б, Г")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id, 'Какими навыками должен обладать оператор, чтобы быть клиентоориентированным'
                                          '\n А) желание помочь'
                                          '\n Б) эмпатия'
                                          '\n В) настрой на поиск решения вопроса, а не препятствий'
                                          '\n Г) нешаблонность общения, индивидуальный подход к каждому',
                         reply_markup=keyboard_vopros1)
    if call.data == "А, Б, В, Г":
        bot.send_message(call.message.chat.id, 'Dерно!')
        time.sleep(3)
        keyboard_vopros1 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="Все, кроме Б", callback_data="Все, кроме Б")
        keyboard_vopros1.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="Только А", callback_data="Только А")
        keyboard_vopros1.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="Все варианты верны", callback_data="Все варианты верны")
        keyboard_vopros1.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="Б, Г", callback_data="Б, Г")
        keyboard_vopros1.add(btn_4)
        bot.send_message(call.message.chat.id, 'Какими навыками должен обладать оператор, чтобы быть клиентоориентированным'
                                          '\n А) желание помочь'
                                          '\n Б) эмпатия'
                                          '\n В) настрой на поиск решения вопроса, а не препятствий'
                                          '\n Г) нешаблонность общения, индивидуальный подход к каждому',
                         reply_markup=keyboard_vopros1)
# Вопрос 4:	Какими навыками должен обладать оператор, чтобы быть клиентоориентированным
    if call.data == "Все, кроме Б":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n Эмпатия - осознанное сопереживание текущему эмоциональному состоянию другого '
                                               'человека без потери ощущения происхождения этого переживания. '
                                               'Понимание эмоционального состояния другого человека и демонстрацию этого понимания')
        bot.send_photo(call.message.chat.id, 'https://drive.google.com/file/d/1ChZ8AjA7UnM-3L5I0GUCezB-m6dBIYs6/view?usp=sharing')
        time.sleep(3)
        bot.send_message(call.message.chat.id, 'Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет просто и понятно'
                                               '\n Верный ответ: Все варианты верны')
    if call.data == "Только А":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n Эмпатия - осознанное сопереживание текущему эмоциональному состоянию другого '
                                               'человека без потери ощущения происхождения этого переживания. '
                                               'Понимание эмоционального состояния другого человека и демонстрацию этого понимания')
        bot.send_photo(call.message.chat.id, 'https://drive.google.com/file/d/1ChZ8AjA7UnM-3L5I0GUCezB-m6dBIYs6/view?usp=sharing')
        time.sleep(3)
        bot.send_message(call.message.chat.id, 'Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет просто и понятно'
                                               '\n Верный ответ: Все варианты верны')
    if call.data == "Б, Г":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n Эмпатия - осознанное сопереживание текущему эмоциональному состоянию другого '
                                               'человека без потери ощущения происхождения этого переживания. '
                                               'Понимание эмоционального состояния другого человека и демонстрацию этого понимания')
        bot.send_photo(call.message.chat.id, 'https://drive.google.com/file/d/1ChZ8AjA7UnM-3L5I0GUCezB-m6dBIYs6/view?usp=sharing')
        time.sleep(3)
        bot.send_message(call.message.chat.id, 'Ты старался, это похвально. Не переживай, скоро начнется обучение, на котором все станет просто и понятно'
                                               '\n Верный ответ: Все варианты верны')
    if call.data == "Все варианты верны":
        bot.send_message(call.message.chat.id, 'Верно!')
        time.sleep(3)
        keyboard_type = types.InlineKeyboardMarkup()
        btn_type = types.InlineKeyboardButton(text="Описание типов DISC", callback_data="type")
        keyboard_type.add(btn_type)
        bot.send_message(call.message.chat.id, 'Есть одна из типологий клиентов DISK. '
                                               'Она поможет вам быстро понимать отличительные особенности клиентов и выбирать '
                                               'правильные стратегии общения с каждым из них. Это поможет вам быстро расположить клиента, '
                                               'избежать конфликтов с ним, а также понять закономерности его поведения.'
                                               '\n Согласно этой теории, мы условно делим клиентов по следующим признакам:'
                                               '\n степень выраженности лидерских качеств: ведомый/ведущий'
                                               '\n склонность полагаться на логику/эмоции'
                                               '\n'
                                               '\n Ведущий/ведомый.'
                                               '\n Ведущий тип поведения выражается активность, решительностью в поведении. '
                                               'Он сам выбирает товары/услуги, точно знает, что именно он хочет купить/уточнить, '
                                               'и какие качества для него принципиальны. Эти люди демонстрируют выраженные '
                                               'лидерские качества, часто занимают руководящие позиции'
                                               '\n Тип поведения, который характеризуется термином «ведомый» означает, '
                                               'что такому человеку необходима внешняя поддержка при принятии важных решений. '
                                               'Они часто приходят выбирать товары с родственниками или друзьями и '
                                               'активно с ними советуются. Если они пришли одни – они часто ориентируются '
                                               'на мнение продавца/консультанта, который должен помочь сделать выбор, '
                                               'поддержать принятое решение или решить вопрос.'
                                               '\n'
                                               '\n Логика/эмоции.'
                                               '\n Клиент, который более склонен к логичному поведению, '
                                               'будет в большей степени интересоваться фактическими характеристиками товара. '
                                               'Он часто занимает экспертную позицию в общении, демонстрирует хорошее знание '
                                               'товара/услуги и требует от продавца/консультанта того же самого'
                                               '\n На клиента - эмоцию в большей степени влияет именно эмоциональность '
                                               'и яркость подачи информации. Он в большей степени оценивает не сам '
                                               'товар/услугу, а то, как он преподнесен. В данном случае ораторские '
                                               'качества продавца/консультанта играют решающую роль.',
                         reply_markup=keyboard_type)
    if call.data == "type":
        bot.send_message(call.message.chat.id, 'Красный тип (ведущий/эмоциональный)'
                                               '\n'
                                               '\n Явный лидер, который характеризуется уверенным поведением и ориентацией на достижение цели. '
                                               'Главное для него – получить желаемое любой ценой. '
                                               'Они предпринимают решительные действия для того, '
                                               'чтобы добиться желаемого результата. '
                                               'При этом красные принимают решения самостоятельно, и на него слабо влияет мнение окружающих.  '
                                               'Это очень энергичные люди, которые часто занимают руководящие должности.'
                                               '\n При этом они не всегда логичны, могут быть импульсивны, иногда непоследовательны. '
                                               'Они часто опираются не на факты, а на эмоции и субъективные впечатления.'
                                               '\n Что можно ожидать от клиентов красного типа:'
                                               '\n Часто «перехватывают» инициативу в общении с продавцом/консультантом'
                                               '\n Больше обращают внимание на степень уверенности продавца/консультанта'
                                               ' и манеру подачи товара/услуги, нежели на технические подробности'
                                               '\n Иногда высказывают возражения, '
                                               'чтобы просто проверить уверенность продавца\консультанта в товаре/услуге'
                                               '\n Могут очень напористо требовать дополнительные скидки и бонусы'
                                               '\n Быстро принимают решения'
                                               '\n Упрямы, их тяжело переубедить в чем-либо'
                                               '\n'
                                               '\n Задача продавца/консультанта: уверенная, убедительная, эмоционально окрашенная презентация'
                                               '\n'
                                               '\n Синий тип (ведущий/логичный)'
                                               '\n Этот тип отличается в первую очередь своей логичностью и рациональностью. '
                                               'Они вдумчивые, практичные, стремятся заранее просчитать последствия своих решений. '
                                               'Они также являются ведущим типом, то есть при принятии решений они '
                                               'опираются не на мнение окружающих, а на итоги своих умозаключений. '
                                               'Они ведут себя достаточно сдержанно, предпочитают спокойную '
                                               'обстановку в общении без чрезмерных эмоций.'
                                               '\n Что можно ожидать от клиентов синего типа:'
                                               '\n Стремятся просчитать выгоду от покупки/услуги'
                                               '\n Обращают внимание на фактические характеристики товара/услуги и их преимущества, а не на эмоциональность презентации'
                                               '\n Часто берут паузу для того, чтобы сравнить товар/услугу с аналогичными товарами конкурентов'
                                               '\n Избегают общения с чрезмерно напористыми продавцами/консультантами'
                                               '\n'
                                               '\n Задача продавца/консультанта: идеальное знание характеристик товара, '
                                               'умение проводить аргументированную сравнительную характеристику и описывать выгоды от приобретения.'
                                               '\n'
                                               '\n Желтый тип (ведомый/эмоциональный)'
                                               '\n Это очень открытые, живые, эмоциональные люди, которые любят общение с окружающими. '
                                               'Они любят быть в центре внимания, и всеми силами стараются это внимание привлечь. '
                                               'Они любят все новое, интересное и уникальное. При этом их внимание неустойчиво,'
                                               ' то есть их интерес может быстро возникнуть и также быстро угаснуть.'
                                               '\n Этот тип в силу неустойчивости своего внимания и ориентации на окружающих '
                                               'относится к ведомым, то есть окружающие достаточно сильно влияют на их мнение. '
                                               'Они могут быстро изменить свое мнение в результате общения, могут быстро '
                                               'загореться новой идеей, которую им интересно преподнесли.'
                                               '\n Что ожидать от клиентов желтого типа:'
                                               '\n Могут быть чрезмерно общительными'
                                               '\n Могут быстро терять интерес к товару/услуге'
                                               '\n Могут быть непоследовательны'
                                               '\n'
                                               '\n Задача продавца/консультанта: презентация с упором на уникальность товара, '
                                               'активная помощь в выборе наиболее подходящего варианта.'
                                               '\n'
                                               '\n Зеленый тип (ведомый/логичный)'
                                               '\n Данный тип отличается тем, что они достаточно консервативны, '
                                               'они стремятся максимальное количество раз перепроверить свое решение '
                                               'и избежать возможных ошибок.  Они относятся к ведомому типу потому, '
                                               'что они придают большое значение общественному мнению, советам друзей '
                                               'и родственников. Перед тем, как принять решение, они стремятся '
                                               'посоветоваться со всеми компетентными в данном вопросе знакомыми и только после этого сделать выбор.'
                                               '\n Кроме того, зеленый тип очень ценит искренность и душевность общения, '
                                               'а также стремится создать максимально комфортные условия для окружающих.'
                                               '\n Что ожидать от клиентов зеленого типа:'
                                               '\n При выборе часто опирается на мнение окружающих'
                                               '\n Нуждаются в поддержке выбора'
                                               '\n Стараются не принимать поспешных решений'
                                               '\n'
                                               '\n Задача продавца/консультанта: теплое и доброжелательное общение, '
                                               'презентация с акцентом на добротность товара/услуги, помощь и поддержка при выборе')
# Вопрос 5
        time.sleep(10)
        bot.send_message(call.message.chat.id, 'В следующих вопросах нужно определить к какому типу относится клент.')
        time.sleep(3)
        keyboard_vopros5 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный5")
        keyboard_vopros5.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий5")
        keyboard_vopros5.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый5")
        keyboard_vopros5.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый5")
        keyboard_vopros5.add(btn_4)
        bot.send_message(call.message.chat.id, 'Сообщает, что уже пересмотрел не одно видео, полазил по всем сайтам, '
                                               'представленным в РБ, уточнил у нескольких друзей, которые уже успели приобрести '
                                               'своим детям электромобили, все нюансы эксплуатации и на что необходимо '
                                               'обратить особое внимание. Приводит информацию с других сайтов, '
                                               'просит сравнить с нашим предложением. При завершении диалога озвучивает, '
                                               'что ждет звонка от еще одного друга, вот он точно в этом плане эксперт, '
                                               '3 машинки купил уже своему ребенку, а после примет решение',
                         reply_markup=keyboard_vopros5)
# Вопрос 6
    if call.data == "красный5":
        bot.send_message(call.message.chat.id, 'Не верно! Попробуй еще раз')
    if call.data == "синий5":
         bot.send_message(call.message.chat.id, 'Не верно! Попробуй еще раз')
    if call.data == "желтый5":
        bot.send_message(call.message.chat.id, 'Не верно! Попробуй еще раз')
    if call.data == "зеленый5":
        bot.send_message(call.message.chat.id, 'Молодец!')
        time.sleep(3)
        keyboard_vopros6 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный6")
        keyboard_vopros6.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий6")
        keyboard_vopros6.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый6")
        keyboard_vopros6.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый6")
        keyboard_vopros6.add(btn_4)
        bot.send_message(call.message.chat.id, 'Хочет сдать анализы на аллергены, с врачом не консультировался, '
                                               'прочитал в сети несколько статей, сделал выводы, что ему это необходимо. '
                                               'Настаивает на полной панели, не дает оператору объяснить, '
                                               'чем они отличаются друг от друга. Говорит, что ему положена скидка, '
                                               'ведь он же планирует сделать целый комплекс анализов. '
                                               'Спрашивает, насколько вы уверены в достоверности анализов именно '
                                               'вашей лаборатории. Где можно ознакомиться с подтверждающей это информацией. '
                                               'А пользовались ли вы сами услугами лаборатории? На ответ нет, звучит: '
                                               'хм, видимо не так уж и хороши. Удивлен, когда узнает, что врач '
                                               'медицинского офиса не расшифрует ему результаты. Настаивает, '
                                               'чтобы для него было исключение. После очень быстро переходит на уточнение '
                                               'адреса ближайшего офиса и прощается',
                 reply_markup=keyboard_vopros6)
# Вопрос 7
    if call.data == "зеленый6":
        bot.send_message(call.message.chat.id, 'Не верно! Попробуй еще раз')
    if call.data == "синий6":
         bot.send_message(call.message.chat.id, 'Не верно! Попробуй еще раз')
    if call.data == "желтый6":
        bot.send_message(call.message.chat.id, 'Не верно! Попробуй еще раз')
    if call.data == "красный6":
        bot.send_message(call.message.chat.id, 'Молодец!')
        time.sleep(3)
        keyboard_vopros7 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный7")
        keyboard_vopros7.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий7")
        keyboard_vopros7.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый7")
        keyboard_vopros7.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый7")
        keyboard_vopros7.add(btn_4)
        bot.send_message(call.message.chat.id, 'При исходящем звонке говорит, как же вам повезло, '
                                               'что вы попали именно на нее. Ведь она так любит поболтать. '
                                               'Параллельно сообщает коллегам, что видите, мобильный оператор '
                                               'звонит именно мне предложить новые условия пользования, а не кому-то из вас.'
                                               ' Начинает расспрашивать про новинку в тарифах, есть ли такая услуга и у нас. '
                                               'С удовольствием бы подключила себе. Когда слышит, что такой нет, но есть другая, '
                                               'которая дает те же преимущества, то слушает очень внимательно, '
                                               'но не более минуты, после отвлекается на разговоры по работе шепотом, '
                                               'при этом не кладя трубку. После того, как вы напоминаете о том. '
                                               'Что это уникальное предложение лишь для нее, задает пару '
                                               'вопросов и соглашается на изменение перечня услуг в ее тарифном плане',
                 reply_markup=keyboard_vopros7)
# Вопрос 8
    if call.data == "зеленый7":
        bot.send_message(call.message.chat.id, 'Не верно! Попробуй еще раз')
    if call.data == "синий7":
         bot.send_message(call.message.chat.id, 'Не верно! Попробуй еще раз')
    if call.data == "красный7":
        bot.send_message(call.message.chat.id, 'Не верно! Попробуй еще раз')
    if call.data == "желтый7":
        bot.send_message(call.message.chat.id, 'Молодец!')
        time.sleep(3)
        keyboard_vopros8 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="красный", callback_data="красный8")
        keyboard_vopros8.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="синий", callback_data="синий8")
        keyboard_vopros8.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="желтый", callback_data="желтый8")
        keyboard_vopros8.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="зеленый", callback_data="зеленый8")
        keyboard_vopros8.add(btn_4)
        bot.send_message(call.message.chat.id, 'В чат обращается клиент, чья посылка ему еще не пришла, '
                                               'срок озвученный изначально специалистом при заполнении заявки истекает сегодня. '
                                               'Он спрашивает, где находится посылка, какова вероятность того, '
                                               'что ему доставят ее сегодня домой, уточняет может ли он сам забрать с '
                                               'пункта выдачи, несмотря на то, что выбирал услугу доставки курьером, '
                                               'будет ли возврат разницы между заказанными услугами, как долго может '
                                               'быть задержка в приезде курьера, учитывая, что посылка уже в его городе. '
                                               'Прописывает свои выводы на основе услышанных ответов, понимает, '
                                               'что товар ему нужен до выходных, а уверенности в доставке до указанных '
                                               'сроков нет. Следовательно, учитывая, что доплата за курьера незначительная, '
                                               'принимает решение приехать самому забрать посылку сегодня. '
                                               'Но предлагает подумать о скидке для него в следующий раз'
                                               ' с учетом сложившейся ситуации, т.к. задержи произошли из-за компании',
                 reply_markup=keyboard_vopros8)
# Вопрос 9
    if call.data == "зеленый8":
        bot.send_message(call.message.chat.id, 'Не верно! Попробуй еще раз')
    if call.data == "желтый8":
         bot.send_message(call.message.chat.id, 'Не верно! Попробуй еще раз')
    if call.data == "красный8":
        bot.send_message(call.message.chat.id, 'Не верно! Попробуй еще раз')
    if call.data == "синий8":
        bot.send_message(call.message.chat.id, 'Молодец!')
        bot.send_message(call.message.chat.id, 'Хм, ну что ж, теперь ты умеешь определять с каким клиентом как '
                                               'себя лучше вести, к старту обучения в проект ты уже готов) Удачи! '
                                               'Напоследок по традиции несколько вопросов на логику.')
        time.sleep(3)
        keyboard_vopros9 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="1", callback_data="1")
        keyboard_vopros9.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="5", callback_data="5")
        keyboard_vopros9.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="7", callback_data="7")
        keyboard_vopros9.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="8", callback_data="8")
        keyboard_vopros9.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="9", callback_data="9")
        keyboard_vopros9.add(btn_5)
        bot.send_message(call.message.chat.id, 'У фермера было 17 коз, из них все кроме 9 погибли от чумы. Сколько у него их осталось?',
                         reply_markup=keyboard_vopros9)
# Вопрос 10
    if call.data == "1":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n9, так как погибли все, кроме девяти')
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
        bot.send_message(call.message.chat.id, 'Двум братьям вместе 11 лет. Один из них на 10 лет старше другого. Сколько лет младшему?',
                         reply_markup=keyboard_vopros10)
    if call.data == "5":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n9, так как погибли все, кроме девяти')
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
    if call.data == "7":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n9, так как погибли все, кроме девяти')
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
    if call.data == "8":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                               '\n9, так как погибли все, кроме девяти')
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
    if call.data == "9":
        bot.send_message(call.message.chat.id, 'Верно!'
                                               '\n9, так как погибли все, кроме девяти')
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
# Вопрос 11
    if call.data == "9 лет":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                                   '\n6 месяцев. Его брату 10 с половиной лет. '
                                               'Если бы младшему брату был один год, то старшему было бы одиннадцать, '
                                               'соответственно вместе им было бы 12 лет')
        time.sleep(1)
        keyboard_vopros11 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="В США", callback_data="В США")
        keyboard_vopros11.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="В Мексике", callback_data="В Мексике")
        keyboard_vopros11.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="На границе", callback_data="На границе")
        keyboard_vopros11.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="В зависимости от национальности", callback_data="В зависимости от национальности")
        keyboard_vopros11.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="Нигде", callback_data="Нигде")
        keyboard_vopros11.add(btn_5)
        bot.send_message(call.message.chat.id,
                             'Самолет, летевший из США в Мексику, разбился ровно на границе между этими двумя странами. '
                             'Где похоронят выживших?',
                             reply_markup=keyboard_vopros11)
    if call.data == "2 года":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                                   '\n6 месяцев. Его брату 10 с половиной лет. '
                                               'Если бы младшему брату был один год, то старшему было бы одиннадцать, '
                                               'соответственно вместе им было бы 12 лет')
        time.sleep(1)
        keyboard_vopros11 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="В США", callback_data="В США")
        keyboard_vopros11.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="В Мексике", callback_data="В Мексике")
        keyboard_vopros11.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="На границе", callback_data="На границе")
        keyboard_vopros11.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="В зависимости от национальности", callback_data="В зависимости от национальности")
        keyboard_vopros11.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="Нигде", callback_data="Нигде")
        keyboard_vopros11.add(btn_5)
        bot.send_message(call.message.chat.id,
                             'Самолет, летевший из США в Мексику, разбился ровно на границе между этими двумя странами. '
                             'Где похоронят выживших?',
                             reply_markup=keyboard_vopros11)
    if call.data == "1 год":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                                   '\n6 месяцев. Его брату 10 с половиной лет. '
                                               'Если бы младшему брату был один год, то старшему было бы одиннадцать, '
                                               'соответственно вместе им было бы 12 лет')
        time.sleep(1)
        keyboard_vopros11 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="В США", callback_data="В США")
        keyboard_vopros11.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="В Мексике", callback_data="В Мексике")
        keyboard_vopros11.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="На границе", callback_data="На границе")
        keyboard_vopros11.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="В зависимости от национальности", callback_data="В зависимости от национальности")
        keyboard_vopros11.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="Нигде", callback_data="Нигде")
        keyboard_vopros11.add(btn_5)
        bot.send_message(call.message.chat.id,
                             'Самолет, летевший из США в Мексику, разбился ровно на границе между этими двумя странами. '
                             'Где похоронят выживших?',
                             reply_markup=keyboard_vopros11)
    if call.data == "11 лет":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                                   '\n6 месяцев. Его брату 10 с половиной лет. '
                                               'Если бы младшему брату был один год, то старшему было бы одиннадцать, '
                                               'соответственно вместе им было бы 12 лет')
        time.sleep(1)
        keyboard_vopros11 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="В США", callback_data="В США")
        keyboard_vopros11.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="В Мексике", callback_data="В Мексике")
        keyboard_vopros11.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="На границе", callback_data="На границе")
        keyboard_vopros11.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="В зависимости от национальности", callback_data="В зависимости от национальности")
        keyboard_vopros11.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="Нигде", callback_data="Нигде")
        keyboard_vopros11.add(btn_5)
        bot.send_message(call.message.chat.id,
                             'Самолет, летевший из США в Мексику, разбился ровно на границе между этими двумя странами. '
                             'Где похоронят выживших?',
                             reply_markup=keyboard_vopros11)
    if call.data == "6 месяцев":
        bot.send_message(call.message.chat.id, 'Верно!'
                                                   '\n6 месяцев. Его брату 10 с половиной лет. '
                                               'Если бы младшему брату был один год, то старшему было бы одиннадцать, '
                                               'соответственно вместе им было бы 12 лет')
        time.sleep(1)
        keyboard_vopros11 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="В США", callback_data="В США")
        keyboard_vopros11.add(btn_1)
        btn_2 = types.InlineKeyboardButton(text="В Мексике", callback_data="В Мексике")
        keyboard_vopros11.add(btn_2)
        btn_3 = types.InlineKeyboardButton(text="На границе", callback_data="На границе")
        keyboard_vopros11.add(btn_3)
        btn_4 = types.InlineKeyboardButton(text="В зависимости от национальности", callback_data="В зависимости от национальности")
        keyboard_vopros11.add(btn_4)
        btn_5 = types.InlineKeyboardButton(text="Нигде", callback_data="Нигде")
        keyboard_vopros11.add(btn_5)
        bot.send_message(call.message.chat.id,
                             'Самолет, летевший из США в Мексику, разбился ровно на границе между этими двумя странами. '
                             'Где похоронят выживших?',
                             reply_markup=keyboard_vopros11)
# Конец
    if call.data == "В США":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                                   '\nНигде. Выживших не хоронят, их откачивают!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Хорошего тебе дня и успехов!')
    if call.data == "В Мексике":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                                   '\nНигде. Выживших не хоронят, их откачивают!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Хорошего тебе дня и успехов!')
    if call.data == "На границе":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                                   '\nНигде. Выживших не хоронят, их откачивают!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Хорошего тебе дня и успехов!')
    if call.data == "В зависимости от национальности":
        bot.send_message(call.message.chat.id, 'Не верно!'
                                                   '\nНигде. Выживших не хоронят, их откачивают!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Хорошего тебе дня и успехов!')
    if call.data == "Нигде":
        bot.send_message(call.message.chat.id, 'Верно!'
                                                   '\nВыживших не хоронят, их откачивают!')
        time.sleep(2)
        bot.send_message(call.message.chat.id, 'Хорошего тебе дня и успехов!')




bot.polling()