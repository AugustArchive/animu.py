import aiohttp
from . import utils

class CFClient:
    def __init__(self, user_agent='animu.py/Production/v0.1.0'):
        self.user_agent = user_agent

    async def get_animu():
        async with aiohttp.ClientSession() as cs:
            async with cs.get(utils.ANIME_URL) as resp:
                json = await resp.json()
                return json

    async def get_hentai():
        async with aiohttp.ClientSession() as cs:
            async with cs.get(utils.HENTAI_URL) as resp:
                json = await resp.json()
                return json
