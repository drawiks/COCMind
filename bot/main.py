
import telebot
from .handlers import start

from config import BOT_TOKEN

from loguru import logger

class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot(BOT_TOKEN, parse_mode="Markdown")
        self.setup_handlers(self.bot)
        
        logger.info("бот запущен")
        
        self.bot.infinity_polling()

    def setup_handlers(self, bot):
        start.register_handlers(bot)