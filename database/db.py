
import aiosqlite

import os

DB_PATH = os.path.join(os.path.dirname(__file__), "cocmind.db")

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS players (
                user_id INTEGER PRIMARY KEY,
                player_tag TEXT NOT NULL,
                name TEXT,
                town_hall_level INTEGER,
                exp_level INTEGER
            )
        """)
        await db.commit()

async def save_player(user_id: int, player_tag: str, name: str, town_hall_level: int, exp_level: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT OR REPLACE INTO players (user_id, player_tag, name, town_hall_level, exp_level)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, player_tag, name, town_hall_level, exp_level))
        await db.commit()

async def get_player(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("""
            SELECT player_tag, name, town_hall_level, exp_level
            FROM players
            WHERE user_id = ?
        """, (user_id,))
        return await cursor.fetchone()
