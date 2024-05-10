# Bundle-Sniper
## Setup
- Open settings.json file and put your cookie in there
- Put your bundle ids in settings file under `Bundles` in this format `"bundle id": max price to snipe at`, exp: `"359150": 100`
- (Optional) Put a discord webhook url if you want to get a notification when you snipe a bundle
- Save the settings file and open main.py
- If main.py is instantly closing, open a command prompt and type `pip install -r requirements.txt`

## Settings
```json
{
    "Cookie": "", Your roblox cookie to snipe bundles with

    "Webhook": "", Optional, discord webhook to get notified when you snipe a bundle

    "Wait_Time": {
        "Checker_1": 3, Wait time of checker 1 (if you dont know what your doing dont touch these)
        "Checker_2": 2 Wait time of checker 2 (if you dont know what your doing dont touch these)
    },

    "Bundles": {
        "359150": 1 Bundles ids with max price
    }
}
```

## ⭐
If you like this repo please star it 😊

## Support
If you want help or want to report a bug join the [Discord](https://discord.gg/deathsniper)
