import tkinter as tk
import random
from tkinter import ttk


class MyProgressBar:
    _inst_count = 0  # 类实例计数器

    def __init__(self, master, **kwargs):
        type(self)._inst_count += 1  # 增加类实例计数器
        self.maximum = kwargs.get('maximum', 100)  # 获取最大值，默认为100
        self.master = master  # 获取父容器
        self.background = kwargs.pop('background', 'blue')  # 获取背景色，默认为蓝色
        self.foreground = kwargs.pop('foreground', 'white')  # 获取前景色，默认为白色
        self.style = kwargs.pop('style', ttk.Style())  # 获取样式
        self.stylename = kwargs.pop('stylename', f'progressbar{type(self)._inst_count}')  # 获取样式名
        self.style.configure(self.stylename, text=f'0/{self.maximum}',
                             background=self.background, foreground=self.foreground)
        self.progressbar = ttk.Progressbar(self.master, style=self.stylename, **kwargs)

    def update_progress_bar(self, value):
        """value: 当前进度值"""
        if value <= self.maximum:
            self.progressbar['value'] = value
            self.style.configure(self.stylename, text=f'{value}/{self.maximum}')


def start_progress_bar(progress_bar):
    progress_bar.update_progress_bar(random.randint(1, 100))


# 为每个实例创建一个独立的样式
style = ttk.Style()
stylename = f'text.Horizontal.TProgressbar'
style.layout(stylename,
             [('Horizontal.Progressbar.trough',
               {'children': [('Horizontal.Progressbar.pbar',
                              {'side': 'left', 'sticky': 'ns'})],
                'sticky': 'nswe'}),
              ('Horizontal.Progressbar.label', {'sticky': ''})])

root = tk.Tk()
root.geometry("300x200")

progress_bar = MyProgressBar(root, style=style, stylename=stylename, length=200, maximum=100, background='red')
progress_bar.progressbar.pack()

start_button = tk.Button(root, text="开始", command=lambda: start_progress_bar(progress_bar))
start_button.pack()

root.mainloop()
