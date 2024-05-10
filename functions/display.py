from rgbprint import Color, gradient_print
import datetime
import time
import asyncio
import os

async def info(self):
    banner = '''
                                        ██▄   ▄███▄   ██     ▄▄▄▄▀ ▄  █ 
                                        █  █  █▀   ▀  █ █ ▀▀▀ █   █   █ 
                                        █   █ ██▄▄    █▄▄█    █   ██▀▀█ 
                                        █  █  █▄   ▄▀ █  █   █    █   █ 
                                        ███▀  ▀███▀      █  ▀        █  
                                                        █           ▀   
                                                       ▀                                                              
        
'''
    while True:
        if self.buying:
            return
        os.system('cls' if os.name == 'nt' else 'clear')
        gradient_print(banner, start_color=Color(0x999999), end_color=Color(0xCCCCCC))
        print(f'''
        {Color(0xCCCCCC)}                                        > Bundle Sniper <

        {Color(0x999999)}                                  > Usernames   : {Color(0xCCCCCC)}{self.username}
        {Color(0x999999)}                                  > Bundles     : {Color(0xCCCCCC)}{len(self.bundles)}
        {Color(0x999999)}                                  > Run Time    : {Color(0xCCCCCC)}{str(datetime.timedelta(seconds=(round(time.time() - self.runtime, 0))))}
        {Color(0x999999)}                                  > Buys        : {Color(0xCCCCCC)}{self.buys}
        {Color(0x999999)}                                  > Last Bought : {Color(0xCCCCCC)}{self.last_bought}

        {Color(0x999999)}                                      > Checks  : {Color(0xCCCCCC)}{self.checks}
        ''')
        await asyncio.sleep(2)
