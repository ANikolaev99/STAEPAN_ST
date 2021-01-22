from telebot import types


markup_menu_start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_yes = types.KeyboardButton('Да')
btn_no = types.KeyboardButton('Нет')
markup_menu_start.add(btn_yes, btn_no)

markup_menu_rabota = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_yes_r = types.KeyboardButton('Работал')
btn_no_r = types.KeyboardButton('Не работал')
markup_menu_rabota.add(btn_yes_r, btn_no_r)

markup_menu_ST = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_gotov = types.KeyboardButton('Готов')
btn_ne_gotov = types.KeyboardButton('Не готов')
markup_menu_ST.add(btn_gotov, btn_ne_gotov)

markup_menu_day2_start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_day2_gotov = types.KeyboardButton('Да, поехали')
btn_day2_ne_gotov = types.KeyboardButton('Нет, не совсем')
markup_menu_day2_start.add(btn_day2_gotov, btn_day2_ne_gotov)

markup_menu_day3_start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_day3_znay = types.KeyboardButton('Да, конечно, знаю')
btn_day3_ne_znay = types.KeyboardButton('Не уверен')
markup_menu_day3_start.add(btn_day3_znay, btn_day3_ne_znay)

markup_menu_poka_day1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_poka_1 = types.KeyboardButton('Перейти на второй уровень')
markup_menu_poka_day1.add(btn_poka_1)

markup_menu_poka_day2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_poka_2 = types.KeyboardButton('Перейти на третий уровень')
markup_menu_poka_day2.add(btn_poka_2)

markup_menu_poka_day3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_poka_3 = types.KeyboardButton('Перейти на четвертый уровень')
markup_menu_poka_day3.add(btn_poka_3)
