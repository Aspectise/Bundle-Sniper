import aiohttp
import asyncio
import traceback
from src import cprint
from functions import purchase

async def start(self):
    async with aiohttp.ClientSession(cookies={".ROBLOSECURITY": self.cookie}) as session:
        while True:
            try:
                if not self.bundles:
                    return
                
                bundle_ids = ','.join(id for id, price in self.bundles)
                async with session.get(f"https://catalog.roblox.com/v1/bundles/details?bundleIds[]={bundle_ids}", ssl=False) as response:
                    self.checks += len(self.bundles)
                    if response.status == 200:
                        data = await response.json()
                        for items in data:
                            if items.get("collectibleItemDetail") and items.get("collectibleItemDetail").get("saleStatus") == "OnSale":
                                bundle_id = items.get("id")
                                bundle_price = items.get("collectibleItemDetail").get("price")
                                bundle_oprice = get_price(self, bundle_id)
                                if bundle_price <= bundle_oprice and not self.buying:
                                    cprint.info("Detected bundle!")
                                    bundle_name = items.get("name")
                                    bundle_pid = items.get("product").get("id")
                                    bundle_cpid = items.get("collectibleItemDetail").get("collectibleProductId")
                                    bundle_cid = items.get("collectibleItemDetail").get("collectibleItemId")
                                    creator_id = items.get("creator").get("id")
                                    creator_type = items.get("creator").get("type")
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
                                        cprint.info(f"Buying {bundle_name}...")
                                        self.buying = True
                                        await purchase.start(self, session, pdata)
                    elif response.status == 429:
                        cprint.error("Rate limit")
                        await asyncio.sleep(10)
            except Exception as e:
                traceback.print_exc()
                cprint.error(e)
            finally:
                await asyncio.sleep(self.wait_checker)

def get_price(self, bundle_id):
    for id, price in self.bundles:
        if int(id) == int(bundle_id):
            return price
    return None