
from bot.api.coc_api import get_player_info

from database.database import Database

def handle_profile(bot, message):
    user_id = message.from_user.id
    db = Database()
    
    user_tag = db.get_tag(user_id)

    if user_tag:
        show_profile(bot, message, user_tag)
    else:
        msg = bot.send_message(
            message.chat.id,
            "🔍 У тебя ещё нет привязанного тега! Пришли свой тег игрока (например: `#ABCD1234`)",
            parse_mode="Markdown"
        )
        bot.register_next_step_handler(msg, lambda msg: save_tag_and_show_profile(bot, msg))

def save_tag_and_show_profile(bot, message):
    user_id = message.from_user.id
    player_tag = message.text.strip()
    
    db = Database()
    
    player_info = get_player_info(player_tag)

    if not player_info:
        bot.send_message(message.chat.id, "❗ Ошибка получения профиля. Проверь свой тег!")
        return

    db.add_user(user_id, player_tag)
    show_profile(bot, message, player_tag)

def show_profile(bot, message, tag):
    player_info = get_player_info(tag)

    if not player_info:
        bot.send_message(message.chat.id, "❗ Ошибка получения профиля. Проверь свой тег!")
        return

    text = f"""🏰 *Профиль игрока:*

👑 Ник: {player_info['name']}
🏷 Тег: {player_info['tag']}
💎 Уровень: {player_info['expLevel']}

🛡 Клан: {player_info['clan']['name'] if 'clan' in player_info else 'Без клана'}
🎖 Роль в клане: {player_info.get('role', '—')}

📤 Пожертвовано войск: {player_info.get('donations', '—')}
📥 Получено войск: {player_info.get('donationsReceived', '—')}

🏡 *Родная деревня*

🎯 Лига: {player_info['league']['name'] if 'league' in player_info else '—'}
🥇 Лучшие трофеи: {player_info.get('bestTrophies', '—')}
🏆 Трофеи: {player_info.get('trophies', '—')}

🏛 Ратуша: {player_info['townHallLevel']}

🏗 *Деревня строителя*

🥇 Лучшие трофеи: {player_info.get('bestBuilderBaseTrophies', '—')}
🏆 Трофеи: {player_info.get('builderBaseTrophies', '—')}

🏛 Дом строителя: {player_info.get('builderHallLevel', '—')}

"""
    bot.send_message(message.chat.id, text, parse_mode="Markdown")
