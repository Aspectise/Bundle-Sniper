import aiohttp
import asyncio
import os
from src import cprint
import json
from functions import checker, display, checker2
import traceback
import time
with open("settings.json", "r") as file:settings = json.load(file)
class Sniper:
    def __init__(self) -> None:
        self.cookie = settings["Cookie"]
        self.user_id, self.username = asyncio.run(self.check_cookie())
        self.webhook_url = settings["Webhook"]
        seen = set()
        self.bundles = list((key, value) for key, value in settings.get('Bundles', {}).items() if not (key in seen or seen.add(key)))

        self.wait_checker = settings.get("Wait_Time").get("Checker_1")
        self.wait_checker2 = settings.get("Wait_Time").get("Checker_2")

        self.buys = 0
        self.checks = 0
        self.last_bought = None
        self.buying = False
        self.runtime = time.time()
        asyncio.run(self.run())

    async def check_cookie(self):
        async with aiohttp.ClientSession(cookies={".ROBLOSECURITY": self.cookie}) as session:
            async with session.get("https://users.roblox.com/v1/users/authenticated", ssl=False) as response:
                if response.status == 200:
                    data = await response.json()
                    user_id = data.get("id")
                    name = data.get("name")
                    return user_id, name
                else:
                    cprint.error("You have an invalid buy cookie in config.json")
                    os.system("pause")
                    os._exit(0)

    async def webhook(self, data):
        if self.webhook_url:
            item_thumb = await self.get_thumb(data['id'])
            payload = {"embeds": [{"title": f"New item purchased with Death Sniper", "description": f"**Successfully Purchased `{data['name']}`**\n**Price: `{data['name']}`**", "url": f"https://www.roblox.com/bundles/{id}", "color": 9109504, "footer": {"text": f"discord.gg/deathsniper","icon_url": "https://cdn-icons-png.flaticon.com/512/521/521269.png"}, "thumbnail": {"url": item_thumb}}]}
            async with aiohttp.ClientSession() as session:
                async with session.post(self.webhook_url, json=payload) as response:
                    if response.status != 204:
                        cprint.error(f"Failed to send webhook notification {response.status}.")
    async def get_thumb(self, id):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://thumbnails.roblox.com/v1/bundles/thumbnails?bundleIds={id}&size=420x420&format=Png&isCircular=false", ssl=False) as response:
                if response.status == 200:
                    data = await response.json()
                    data = data.get("data")[0]
                    return data.get("imageUrl")
                else:
                    return None

    async def run(self):
        while True:
            try:
                tasks = [asyncio.create_task(display.info(self)), asyncio.create_task(checker.start(self)), asyncio.create_task(checker2.start(self))]
                await asyncio.gather(*tasks)
            except Exception as e:
                traceback.print_exc()
                cprint.error(e)

if __name__ == "__main__":
    Sniper()