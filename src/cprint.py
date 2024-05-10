from rgbprint import Color

def info(text):
    print(f"{Color(127, 127, 127)}INFO{Color(255, 255, 255)} | {text}")

def bought(text):
    print(f"{Color(0, 255, 0)}BOUGHT{Color(255, 255, 255)} | {text}")

def error(text):
    print(f"{Color(255, 0, 0)}ERROR{Color(255, 255, 255)} | {text}")
