import telebot
from telebot import types

# Вставьте ваш токен бота сюда
TOKEN = '6059362707:AAHV__YmJin22J1YL_IeVNAZvo4ddYn3ir0'

bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Отправь мне команду /addme, чтобы я смог добавить тебя в группу.")

# Обработчик команды /addme
@bot.message_handler(commands=['addme'])
def addme(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    # Здесь нужно указать chat_id группы, в которую вы хотите добавить пользователей
    group_chat_id = -1001971370189

    # Проверяем, является ли текущий чат группой
    if message.chat.type == 'private':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Добавить меня', url=f'https://t.me/+gL4Tf4anZE41N2U6'))
        bot.send_message(chat_id, 'Чтобы добавить себя в группу, нажми на кнопку ниже:', reply_markup=markup)
    else:
        bot.send_message(chat_id, 'Ты уже находишься в группе.')


bot.polling()
