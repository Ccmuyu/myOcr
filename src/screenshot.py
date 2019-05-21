""" 本程序可独立运行，主要功能是截图并保存"""
import sys
from time import sleep
import keyboard
from PIL import ImageGrab #pillow
from baidumap import BaiduApi
from getText import GetText


def screenShot():
    """用于截图并保存"""
    print('请按F1开始截图')
    if keyboard.wait(hotkey='f1') == None:
        print('复制剪切板的图片，请按Ctrl+b，不复制继续截图')
        if keyboard.wait(hotkey='Ctrl+b') == None:
            sleep(0.02)  # 防止获取的是上一张截图
            # 复制剪贴板里面的图片
            im = ImageGrab.grabclipboard()
            im.save('Picture.png')


if __name__ == '__main__':
    baiduapi = BaiDuAPI('password.ini')
    for _ in range(sys.maxsize):
        screenShot()
        texts = baiduapi.picture2Text('Picture.png')
        print(texts)
        GetText.setText(texts)  # 剪贴板剪贴
        sleep(0.02)
        GetText.getText()
        print('退出请按Ctrl+x')
        if keyboard.wait(hotkey='Ctrl+x') == None:
            name = input('请输入保存图像识别文字文件名:')
            f = open(name + '.txt', 'w')
            f.write(texts)
            f.close()
            break
