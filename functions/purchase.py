from src import cprint, csrf
import uuid
import traceback
import asyncio

async def start(self, session, pdata):
    try:
        xcsrf = csrf.get(self.cookie)
        session.headers.update({"X-Csrf-Token": xcsrf})
        payload = {
        "collectibleItemId": pdata["cid"],
        "expectedCurrency": 1,
        "expectedPrice": pdata["price"],
        "expectedPurchaserId": self.user_id,
        "expectedPurchaserType": "User",
        "expectedSellerId": pdata["creatorId"],
        "expectedSellerType": pdata["creatorType"],
        "idempotencyKey": str(uuid.uuid4()),
        "collectibleProductId": pdata["cpid"]
    }   
        async with session.post(f"https://apis.roblox.com/marketplace-sales/v1/item/{pdata['cid']}/purchase-item", json=payload, ssl=False) as response:
            if response.status == 200:
                data = await response.json()
                if data.get("purchased"):
                    remove_id(self, pdata["id"])
                    cprint.bought(f"Successfully bought {pdata['name']} for {pdata['price']}!")
                    self.buys += 1
                    self.last_bought = pdata["name"]
                    self.webhook(pdata)
                else:
                    cprint.error(f"Failed to buy bundle: {data}")
            else:
                data = await response.text()
                if "AlreadyOwned" in data:
                    cprint.error(f"{pdata['name']} already owned.")
                    remove_id(self, pdata["id"])
                    return
                else:
                    cprint.error(f"Failed to buy bundle: {data}")
    except Exception as e:
        cprint.error(e)
    finally:
        self.buying = False


def remove_id(self, id):
    index = next((index for index, bundle in enumerate(self.bundles) if int(bundle[0]) == id), None)
    if index is not None:
        del self.bundles[index]