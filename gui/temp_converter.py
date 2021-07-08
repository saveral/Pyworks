# 온도변환기 app
from tkinter import *
from gui.converters import Converters

class App:
    def __init__(self, master):
        self.conv = Converters('C','F',1.8, 32)
        frame = Frame(master)
        frame.pack()

        Label(frame, text='deg C').grid(row=0, column=0)
        self.c = DoubleVar()    # 실수형 변수 선언
        Entry(frame, textvariable=self.c).grid(row=0, column=1)

        Label(frame, text='deg F').grid(row=1, column=0)
        self.f = DoubleVar()
        Label(frame, textvariable=self.f).grid(row=1, column=1)

        Button(frame, text="변환", command=self.convert).grid(row=2, columnspan=2)

    def convert(self):
        c = self.c.get()  # deg C의 값 가져오기
        c_f = str(self.conv.convert(c))[0:5] # C -> f 계산값
        self.f.set(c_f)   # def f에 넣어준다

root = Tk()
root.title("온도 변환기")
app = App(root)

root.mainloop(0)
