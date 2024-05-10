import aiohttp
import asyncio
import traceback
from src import cprint
from functions import purchase, get_product

async def start(self):
    async with aiohttp.ClientSession(cookies={".ROBLOSECURITY": self.cookie}) as session:
        while True:
            try:
                if not self.bundles:
                    return
                for id, price in self.bundles:
                    async with session.get(f"https://catalog.roblox.com/v1/catalog/items/{id}/details?itemType=Bundle", ssl=False) as response:
                        self.checks += 1
                        if response.status == 200:
                            data = await response.json()
                            if data.get("isPurchasable"):
                                bundle_id = data.get("id")
                                bundle_price = data.get("price")
                                if bundle_price <= price and not self.buying:
                                    cprint.info("Detected bundle!")
                                    bundle_name = data.get("name")
                                    bundle_pid = data.get("productId")
                                    bundle_cid = data.get("collectibleItemId")
                                    bundle_cpid = await get_product.get(session, bundle_cid)
                                    creator_id = data.get("expectedSellerId")
                                    creator_type = data.get("creatorType")
                                    pdata = {
                                        "name": bundle_name,
                                        "id": bundle_id,
                                        "pid": bundle_pid,
                                        "cid": bundle_cid,
                                        "cpid": bundle_cpid,
                                        "price": bundle_price,
                                        "creatorId": creator_id,
                                        "creatorType": creator_type
                                    }
                                    if not self.buying:
                                        self.buying = True
                                        cprint.info(f"Buying {bundle_name}...")
                                        await purchase.start(self, session, pdata)
                        elif response.status == 429:
                            await asyncio.sleep(10)
            except Exception as e:
                traceback.print_exc()
                cprint.error(e)
            finally:
                await asyncio.sleep(self.wait_checker2)
