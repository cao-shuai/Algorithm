from tkinter import *
from tkinter import ttk

class MyApplication:
    windowhight = 640
    windowwidth = 960
    window=Tk()

    def __init__(self):
        self.window.title("我的python应用程序")
        self.window.resizable(True,True)

    def __setdefaultWindowsize__(self):
        screenWidth, screenHeight = self.window.maxsize()  # 获得屏幕宽和高
        geometryParam = '%dx%d+%d+%d' % (
            self.windowwidth, self.windowhight, (screenWidth - self.windowwidth) / 2, (screenHeight - self.windowhight) / 2)
        self.window.geometry(geometryParam)  # 设置窗口大小及偏移坐标

    def setWindowSize(self,width,hight):
        if width >10 and hight > 10:
            self.windowhight=hight
            self.windowWide=width
        else:
            print ("窗口大小恢复初始值")
            self.windowhight = 640
            self.windowwidth = 960
        self.__setdefaultWindowsize__()

    def flushdisplay(self):
        self.window.mainloop()