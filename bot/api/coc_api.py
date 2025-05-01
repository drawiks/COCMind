
import requests

from config import COC_API_TOKEN

from loguru import logger

BASE_URL = "https://api.clashofclans.com/v1"

HEADERS = {
    "Authorization": f"Bearer {COC_API_TOKEN}"
}

def get_player_info(player_tag: str):
    url = f"{BASE_URL}/players/%23{player_tag.lstrip('#')}"
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"{response.status_code}: {response.text}")
            return None
    except requests.RequestException as e:
        logger.error(e)
        return None
