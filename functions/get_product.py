async def get(session, item):
    async with session.post("https://apis.roblox.com/marketplace-items/v1/items/details", json={"itemIds": [item]}) as response:
        if response.status == 200:
            data = await response.json()
            data = data[0]
            return data.get("collectibleProductId")
        else:
            return None