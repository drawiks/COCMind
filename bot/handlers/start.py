
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from .profile import handle_profile

def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start_message(message):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        profile_button = KeyboardButton("📋 Профиль")
        upload_button = KeyboardButton("🏰 Загрузить базу")
        settings_button = KeyboardButton("⚙️ Настройки")
        markup.add(profile_button, upload_button, settings_button)

        bot.send_message(
            message.chat.id,
            "👋 Привет! Я *COCMind* — твой помощник в Clash of Clans!\n\nВыбери действие ниже 👇",
            reply_markup=markup,
            parse_mode="Markdown"
        )

    @bot.message_handler(func=lambda message: message.text == "📋 Профиль")
    def open_profile(message):
        handle_profile(bot, message)

    @bot.message_handler(func=lambda message: message.text == "🏰 Загрузить базу")
    def upload_base(message):
        bot.send_message(message.chat.id, "📷 Пришли скриншот своей базы!")

    @bot.message_handler(func=lambda message: message.text == "⚙️ Настройки")
    def settings(message):
        bot.send_message(message.chat.id, "⚙️ Настройки будут доступны скоро!")
