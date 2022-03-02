import telebot
from telebot import types
import  random
token = "5112096742:AAHxlqc4m0rNXbvcLM8ACtEMTeLBJNbMnPs"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['prepod'])
def prepod(message):
    bot.send_message(message.chat.id,'Чёрный список: Черноусова Т.Г., Кунц')
@bot.message_handler(commands=['start'])#обработка сообщений
def start(message):# функция
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("МТУСИ", "/help","/Да\Нет")
    bot.send_message(message.chat.id, 'Привет! Я типичный студент МТУСИ -Стасян\nЯ буду помогать тебе \n Хочешь узнать , что я умею? Тогда нажми /help(Эта кнопка будет в меню быстрого доступа, не потеряешь) ',reply_markup=keyboard)
'''Класс ReplyKeyboardMarkup создает пользовательскую клавиатуру с текстовыми кнопками на месте стандартной клавиатуры.'''
'''етод row() заполняет (message)клавиатуру кнопками. Метод send_message отправляет пользователю сообщение.'''

@bot.message_handler(commands=['Да\Нет'])
def reshka(message):
    a =  random.randint(0, 1)
    if a ==0:
        bot.send_message(message.chat.id, ' Нет')
    else:
        bot.send_message(message.chat.id, 'Да')
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, ' Я умею: \nРассказывать про преподов /prepod\nДавать советы\nДавать ссылку на сайт Мтуси(Левая кнока)\nПринимать решения(Идти на пары или нет)\nЕщё у меня есть пасхалки\nИ ещё. Ты можешь убить меня написав stop ')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.upper() == "МТУСИ":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
@bot.message_handler(content_types=['text'])
def gachi(message):
    if message.text.lower() == "гачи":
        bot.send_message(message.chat.id, 'welcome to the club buddy')
'''bot.send_photo(message.chat.id, 'https://www.meme-arsenal.com/memes/1943d46a42850f40a74116125d6cc1a4.jpg')
        video = open('welcome to the club buddy.mp4', 'rb')
        bot.send_video(message.chat.id , video)'''
'''img = open('3bmw6lzVeSM.JPG','rb')
        bot.send_photo(message.chat.id, img)'''
'''gif = open('gachiteam.gif', 'rb')
        bot.send_animation(message.chat.id , gif)'''
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() =='совет':
        bot.send_message(message.chat.id,'Если хочешь провести кента в Вуз  на Моторе, то иди через восточку')
@bot.message_handler(content_types=['text'])
def stop(message):
    if message.text.lower()=="stop":
        bot.send_message(message.chat.id ,'Конечно. Я служу тебе и поступлю так, как ты скажешь. Пусть это будет нашим секретом. Никто, ни единая душа не должна об этом знать. Я был верен тебе до самого дня твоего предательства.')
        bot.stop_bot()
bot.polling() #none_stop=True
