
import aiohttp

from config import COC_API_TOKEN

from loguru import logger

BASE_URL = "https://api.clashofclans.com/v1"

HEADERS = {
    "Authorization": f"Bearer {COC_API_TOKEN}"
}

async def get_player_info(player_tag: str):
    url = f"{BASE_URL}/players/%23{player_tag.lstrip('#')}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS) as response:
            if response.status == 200:
                return await response.json()
            else:
                logger.error(response.status)
                return None
