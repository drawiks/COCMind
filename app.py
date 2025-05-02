
from bot.main import Bot
from database.database import Database

if __name__ == "__main__":
    db = Database()
    db._init_db()
    bot = Bot()