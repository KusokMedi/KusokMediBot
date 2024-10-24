import telebot as t
from PIL.ImageMath import lambda_eval
from telebot import types
from time import sleep
import requests
import json
import random as r

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = t.TeleBot("Your_Token")
print("Bot successfully started!")

jokes1 = ["""— Вчера долго пыталась объяснить бабуле, что работаю программистом.
— Удалось?
— Короче, сошлись на том, что чиню телевизоры и развожу мышей.""", """— Почему ваши дети всё время ссорятся?
— Конфликт версий, — отвечает программист.""", """Программисту нужно попасть на двенадцатый этаж.
Он заходит в лифт, нажимает кнопку «1», затем «2» и долго ещё безуспешно ищет глазами клавишу Enter…""",
          """Один монитор — обычный программист,два монитора — продвинутый программист, три монитора — системный программист, четыре монитора — охранник.""",
          """Беседуют два программиста.
— Чем программист отличается от обычного смертного?
— А тем, что в состоянии ответить на вопрос, в котором уже заключён ответ.
— Это как же?
— Ну, например, ответь на вопрос: сколько будет 2х2=4?
— ТRUЕ!""",
          """Школьный учитель спрашивает учеников о профессии родителей.
— Тим, чем твоя мама занимается на работе?
Тим встаёт и гордо говорит:
— Она доктор.
— Замечательно, ну как насчёт тебя, Эмми?
Девочка стеснительно произносит:
— Мой папа разносит почту.
— Спасибо, Эмми, — говорит учитель. — Ну, а твои родители что делают, Билл?
Билл гордо встаёт и объявляет:
— Мой папа играет музыку в борделе!
Обалдевший учитель решил направиться к Биллу домой.
— В каких условиях вы растите ребёнка? — спрашивает он у отца.
Тот отвечает:
— Вообще-то я программист и специализируюсь на TCP/IP коммуникационном протоколе в системе UNIX. Ну как объяснить это семилетнему пацану?""",
          """Встретил в поле Иван Царевич Змея Горыныча об одной голове.
Достал он свой меч-кладенец и срубил голову, но на её месте появилось две. Срубил две — выросло четыре, срубил четыре — выросло восемь.
Так рубил Иван Царевич головы, пока не снёс Змею 65536 голов, и сдох Змей Горыныч, ибо был он 16-ти разрядный.""",
          """Однажды новичок спросил мастера: «Я оптимизировал 10 строк кода на Python в одну строку за счёт осмысления списка, и новый код получился очень элегантным. Почему мой pull request отклонили?».

Мастер ответил: «Это я его отклонил»

Увидев удивление новичка, мастер добавил: «Я написал эти 10 строк кода месяц назад».

Новичок покраснел, но всё равно не хотел отказываться от своего PR, поэтому возразил: «Но прямо рядом с функцией, которую я изменил, находится аналогичная функция с гораздо более сложными однострочниками. Почему их объединили?»

«О, тот код я написал 10 лет назад», — ответил мастер.""",
          """Однажды новичок спросил мастера: «Каждый день я пишу много кода, выполняя множество требований, но почему мой уровень программирования не повышается?»

Мастер ответил: «Дай посмотреть, что ты пишешь».

Новичок показал компьютер. Мастер указал на обычную строку кода присвоения переменных и сказал: «Когда ты поймёшь, что перед этим нужно пять строк комментариев, тогда и вырастешь». С этими словами мастер ушёл.""",
          """Между интернетом и жизнью гораздо больше общего, чем может показаться на первый взгляд: в обоих случаях непонятно, что мы здесь делаем и ради чего, но уходить уже как-то не слишком хочется…""",
          """Давеча узнала страшное — 30% от всех посылаемых дикпиков не настоящие! В смысле не принадлежат отправителю, а тырены с интернета. Не то, чтобы меня это сильно волновало, мне и не присылали никогда, но хотелось верить, что в мире фальшивого блеска, лжи и пропаганды осталось что-то честное и искреннее и вот. Последняя скрепа рухнула…""",
          """Роскомнадзор не смог отчитаться об успешной блокировке Рунета из-за отсутствия интернета.""",
          """Если в очередном обновлении  Java будет создана  функция очищения  программного мусора,
основная  часть приложений Java будут удалять себя сразу после установки.""",
          """Баг — это еще не записанная  фича.""", """Компьютер — это настоящее  зло, но  если его выключить,
появляются  два новых зла: телевизор и холодильник. """,
          """Всегда мало времени, чтобы разработать проект, но его всегда хватает, чтобы сделать в 2 раза больше багов."""]
facts1 = ["""Ада Лавлейс, дочь знаменитого поэта Лорда Байрона, часто считается первым программистом в истории. Она работала с Чарльзом Бэббиджем над его "Аналитической машиной" и написала первую в мире программу для неё, хотя машина так и не была построена.""",
          """"Hello, World!" Это традиционное сообщение, которое программисты используют для тестирования программы или системы. Этот пример впервые был использован в книге "Программирование на языке С" в 1978 году.""", """На сегодняшний день существует более 700 различных языков программирования, хотя большинство из них уже устарели или используются очень редко. Некоторые из наиболее популярных в настоящее время: Python, JavaScript, Java, C# и Rust.""",
          """Перед наступлением 2000 года мир испытывал тревогу из-за проблемы, связанной с тем, что многие компьютерные системы представляли год только двумя цифрами. Это означало, что 2000 год мог бы быть интерпретирован как 1900 год, что могло привести к ошибкам в системах. Многие компании тратили миллиарды долларов на исправление этой проблемы.""",
          """В 2012 году был зарегистрирован отчет об ошибке с длиной в 2,15 миллиона символов в проекте под названием Linux Kernel, который стал известен как самый длинный отчет об ошибке в истории.""",
          """Многие программисты вставляют скрытые сообщения или функции в программы или веб-сайты в качестве шутки или трибьюта. Эти скрытые элементы часто называют "пасхальными яйцами".""",
          """Операционная система Windows 3.1 состояла из около 3 миллионов строк кода. В сравнении с ней, современные операционные системы, такие как Linux Kernel, содержат более 27 миллионов строк кода.""",
          """Термины, такие как "24/7" (24 часа в сутки, 7 дней в неделю) и "365" (каждый день года), стали популярными благодаря IT-индустрии и необходимости постоянной поддержки и доступности серверов и сервисов. В современном мире многие системы и сервисы должны работать без простоев, что ставит перед программистами и инженерами сложные задачи по обеспечению непрерывности работы.""",
          """99 багов в коде - этот анекдот или фраза стала популярной среди программистов. Она гласит: "99 багов в коде, возьми один, почини... 127 багов в коде". Это шутливый способ подчеркнуть, что исправление одной проблемы в программе может породить другие.""",
          """Python, созданный в конце 1980-х годов Гвидо ван Россумом, стал одним из самых популярных языков программирования в мире. Его часто рекомендуют новичкам из-за простоты синтаксиса, а также из-за многочисленных применений в веб-разработке, науке о данных, искусственном интеллекте и многом другом.""",
          """Ожидается, что к 2030 году будет более 45 миллионов вакансий в сфере программирования по всему миру, что подчеркивает огромное влияние IT-сферы на глобальную экономику."""]

# EXAMPLE
# @bot.message_handler(commands=["command1", "command2"])
# def commandname(message):
#     bot.send_message(message.chat.id, f"")

# Start script
@bot.message_handler(commands=["start", "restart"])
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.first_name}!")
    sleep(1)
    bot.send_message(message.chat.id, f"""Кратко обо мне,
Я обычый бот созданный Матвеем (@KusokMedi) 09.28.2024,
Я был выпущен в открытый доступ XX.XX.XXXX и продолжаю обнавлятся.

Текущщая версия бота 1.3

Написать по поводу багов/предложений -> @KusokMedi
""")
    sleep(0.5)
    bot.send_message(message.chat.id, f"Чтобы узнать всё о боте пиши /help")


# Help script
@bot.message_handler(commands=["help"])
# Help list
# start - Старт бота▶️
# restart - Перезапуск 🔄
# help - Меню помощи 🆘
# socialmedia - Мои социальные сети 📱
# photogalery - Галлерея 🌄
# weather - Погода ⛅️
# random - Бросить кубик 🎲
# joke - Рандомная шутка 😂
# fact - Рандмный факт 🤔
# meme - Мемасик 🤪

# Help Script
def help(message):
    bot.send_message(message.chat.id, """<b>Меню помощи:</b>

    1. /start - Старт бота ▶️
    2. /restart - Перезапуск 🔄
    3. /socialmedia - Мои социальные сети 📱
    4. /weather - Погода ⛅️
    5. /random - Бросить кубик 🎲
    6. /joke - Рандомная шутка 😂
    7. /fact - Рандмный факт 🤔
    8. /meme - Мемасик 🤪""", parse_mode="html")


# Socialmedia scrpit
@bot.message_handler(commands=["social", "socialmedia"])
def commandname(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Мой Telegram канал", url="t.me/KusokMedi")
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton("Мой YouTube", url="bit.ly/KusokMediYT")
    btn3 = types.InlineKeyboardButton("Мой Discord", url="bit.ly/KusokMediDiscord")
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, """<b>Мои социальные сети:</b>""", parse_mode="html", reply_markup=markup)


# Gallery script
# @bot.message_handler(commands=["photogallery"])
# def photogallery(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton("Котик 😺")
#     btn2 = types.KeyboardButton("Собачка 🐶")
#     markup.row(btn1, btn2)
#     bot.send_message(message.chat.id, "Выбери фото", reply_markup=markup)
#     bot.register_next_step_handler(message, vybor_foto)
#
# def vybor_foto(message):
#     if message.text == "Котик 😺":
#         file1 = open("C:\\Users\\Matvejs Upesleja\\Desktop\\python progects\\KusokMediBot\\files\\cutecat.jpg", "rb")
#         bot.send_photo(message.chat.id, file1)
#         bot.send_message(message.chat.id, "Красивый, неправда ли?", reply_markup=types.ReplyKeyboardRemove())
#     elif message.text == "Собачка 🐶":
#         file2 = open("C:\\Users\\Matvejs Upesleja\\Desktop\\python progects\\KusokMediBot\\files\\dog.jpeg", "rb")
#         bot.send_photo(message.chat.id, file2)
#         bot.send_message(message.chat.id, "Миленький, неправда ли?", reply_markup=types.ReplyKeyboardRemove())
#     else:
#         bot.send_message(message.chat.id, "Error, Надо нажать на кнопки! Повтори -> /photogallery", reply_markup=types.ReplyKeyboardRemove())
# weather
@bot.message_handler(commands=["weather", "w"])
def weather(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("*тыкни сюда*", url="t.me/KusokMediWeatherBot")
    markup.row(btn1)
    bot.send_message(message.chat.id, """<b>Погода:</b>""", parse_mode="html", reply_markup=markup)


# random
@bot.message_handler(commands=['random'])
def dice1(message):
    bot.send_message(message.chat.id, "Твой кубик:")
    bot.send_dice(message.chat.id)

# Jokes script
@bot.message_handler(commands=['joke'])
def joke(message):
    global jokes1
    randomjokei = r.choice(jokes1)
    bot.send_message(message.chat.id, f"Рандомная шутка:\n{randomjokei}")
# Facts
@bot.message_handler(commands=['fact', "facts"])
def joke(message):
    global facts1
    randomfactsi = r.choice(facts1)
    bot.send_message(message.chat.id, f"Рандомный факт:\n{randomfactsi}")
# Memes
@bot.message_handler(commands=['meme'])
def send_mem(message):
    randommemeid = randint(0,9)
    if randommemeid == 0:
        with open('C:\\Users\\Matvejs Upesleja\\Desktop\\Prog memes\\meme1.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
    elif randommemeid == 1:
        with open('C:\\Users\\Matvejs Upesleja\\Desktop\\Prog memes\\meme2.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
    elif randommemeid == 2:
        with open('C:\\Users\\Matvejs Upesleja\\Desktop\\Prog memes\\meme3.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
    elif randommemeid == 3:
        with open('C:\\Users\\Matvejs Upesleja\\Desktop\\Prog memes\\meme4.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
    elif randommemeid == 4:
        with open('C:\\Users\\Matvejs Upesleja\\Desktop\\Prog memes\\meme5.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
    elif randommemeid == 5:
        with open('C:\\Users\\Matvejs Upesleja\\Desktop\\Prog memes\\meme6.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
    elif randommemeid == 6:
        with open('C:\\Users\\Matvejs Upesleja\\Desktop\\Prog memes\\meme7.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
    elif randommemeid == 7:
        with open('C:\\Users\\Matvejs Upesleja\\Desktop\\Prog memes\\meme8.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
    elif randommemeid == 8:
        with open('C:\\Users\\Matvejs Upesleja\\Desktop\\Prog memes\\meme9.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
    elif randommemeid == 9:
        with open('C:\\Users\\Matvejs Upesleja\\Desktop\\Prog memes\\meme10.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
    else:
        bot.send_message(message.chat.id, "Ета ошибка невозможна\n0_0\nКАААКК?!")
# shop
# @bot.message_handler(commands=["shop"])
# def shop(message):
#     file1 = open("C:\\Users\\Matvejs Upesleja\\Desktop\\python progects\\KusokMediBot\\files\\shop.png", "rb")
#     bot.send_photo(message.chat.id, file1)
#     markup = InlineKeyboardMarkup()
#     btn1 = InlineKeyboardButton("Нажми сюда чтобы открыть магазин 🙃")
#     bot.send_message(message.chat.id, "<b>Мой магазин!</b>", parse_mode="html", reply_markup=markup)
bot.polling(none_stop=True)
