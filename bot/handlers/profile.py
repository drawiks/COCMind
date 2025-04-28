
from bot.api.coc_api import get_player_info

from database.db import save_player, get_player

import asyncio

def handle_profile(bot, message):
    user_id = message.from_user.id
    player_data = asyncio.run(get_player(user_id))

    if player_data and player_data[0]:  # player_tag существует
        player_tag = player_data[0]
        asyncio.run(show_profile(bot, message, player_tag))
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

    player_info = asyncio.run(get_player_info(player_tag))

    if not player_info:
        bot.send_message(message.chat.id, "❗ Ошибка получения профиля. Проверь свой тег!")
        return

    name = player_info['name']
    town_hall_level = player_info['townHallLevel']
    exp_level = player_info['expLevel']

    asyncio.run(save_player(user_id, player_tag, name, town_hall_level, exp_level))

    asyncio.run(show_profile(bot, message, player_tag))

async def show_profile(bot, message, player_tag):
    player_info = await get_player_info(player_tag)

    if not player_info:
        bot.send_message(message.chat.id, "❗ Ошибка получения профиля. Проверь свой тег!")
        return

    text = f"""🏰 *Профиль игрока:*

👤 Имя: {player_info['name']}
🏷 Тег: {player_info['tag']}
🎯 Уровень: {player_info['expLevel']}
🏛 Ратуша: {player_info['townHallLevel']}
👥 Клан: {player_info['clan']['name'] if 'clan' in player_info else 'Без клана'}

🏆 Трофеи: {player_info['trophies']}
⚔️ Победы в атаке: {player_info['attackWins']}
🛡 Победы в защите: {player_info['defenseWins']}
"""

    bot.send_message(message.chat.id, text, parse_mode="Markdown")
