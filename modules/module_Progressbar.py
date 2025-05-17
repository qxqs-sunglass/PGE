from tkinter import ttk
from modules.module_text import TextModule


class Progressbar:
    def __init__(self, master, pos, **kwargs):
        self.master = master
        self.progressbar = None  # 进度条对象
        self.parameter_names = ["orient", "length", "mode",
                                "maximum", "value", "variable",
                                "phase", "troughcolor", "background",
                                "text", "thickness"]  # 参数名称列表
        self.parameter_noneed = ["text", "thickness", "troughcolor", "background"]  # 参数名称列表，不需要传递
        self.orient = None  # 进度条方向，可选值：horizontal、vertical
        self.length = None  # 进度条长度，单位为像素
        self.mode = None  # 进度条模式
        self.maximum = None  # 进度条最大值
        self.value = None  # 进度条当前值
        self.variable = None  # 进度条变量
        self.phase = None  # 进度条阶段
        self.text = ""  # 进度条文字
        self.text_txt = None  # 进度条文字
        self.thickness = 10  # 进度条厚度
        self.troughcolor = "white"  # 进度条背景色
        self.background = "black"  # 进度条前景色
        self.pos = pos  # 进度条位置
        self.kwargs = kwargs  # 参数字典
        self.style = ttk.Style()  # 进度条样式
        self.style.theme_use("default")  # 设置默认主题
        self.init()

    def init(self):
        """初始化进度条"""
        for name in self.parameter_names:
            if name in self.kwargs:
                self.__dict__[name] = self.kwargs.get(name)
        for name in self.parameter_noneed:
            if name in self.kwargs:
                self.kwargs.pop(name)
        self.progressbar = ttk.Progressbar(self.master, **self.kwargs)
        self.style.configure("TProgressbar", troughcolor=self.troughcolor, background=self.background,
                             thickness=self.thickness)
        self.text_txt = TextModule(self.master, (self.pos[0] + self.length+5, self.pos[1]-10), self.text,
                                   size=self.thickness*2)

    def draw(self):
        """绘制进度条"""
        self.progressbar.place(x=self.pos[0], y=self.pos[1])
        self.text_txt.draw()

    def update(self, value, text=None):
        """更新进度条"""
        if value > self.maximum:
            value = self.maximum
        elif value < 0:
            value = 0
        if text is not None:
            self.text = text
        self.text_txt.set_text(self.text)
        self.progressbar.configure(value=value)
