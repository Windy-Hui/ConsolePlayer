# -*- code: utf-8 -*-

# 引入内部库
import os
import ctypes
import sys
import time

# 引入外部库
try:
    from PIL import ImageGrab, Image
except ModuleNotFoundError:
    print("缺少运行所需要的库")
    time.sleep(5)
    sys.exit()


def GetConsoleXY():
    """获取控制台尺寸"""
    return (os.get_terminal_size().columns // 2, os.get_terminal_size().lines) 

def GetScreenShotFullWindow():
    """全屏截图"""
    return ImageGrab.grab()

def ChangeScreenshotSize(size, screen):
    """改变图像分辨率"""
    NewXY = size
    return screen.resize(NewXY)

def ConsoleClear():
    """清空控制台"""
    c = ctypes.windll.LoadLibrary(".\\ConsoleClear.dll")
    c.ConsoleClear()

def rgb(red, green, blue, string):
    """获取RGB颜色并返回相应颜色的字符"""
    return f'\x1b[38;2;{red};{green};{blue}m{string}'


def run():
    while 1:
        time.sleep(0.02)
        image = ChangeScreenshotSize(GetConsoleXY(), GetScreenShotFullWindow())
        width, height = image.size
        ConsoleClear()
        for y in range(1,height-1):
            for x in range(1,width):
                R, G, B = image.getpixel((x,y))
                sys.stdout.write(rgb(R, G, B,"██"))
            sys.stdout.write("\n")

if __name__ == '__main__':
    run()
