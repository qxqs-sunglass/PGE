from tkinter import Label, RIGHT, LEFT, CENTER, font, StringVar


class TextModule:
    """文本模块"""
    def __init__(self, master, pos, text, size=12, color="black",
                 font_name="Arial", justify="left", width=200, height=1, text_mode="auto",
                 textvariable=False, pos_mode="xy"):
        """master: 窗口对象\n
           pos: 位置坐标\n
           text: 文本内容\n
           size: 字体大小 (默认12)\n
           color: 字体颜色 (默认黑色)\n
           font_name: 字体名称 (默认Arial)\n
           justify: 对齐方式 (默认左对齐)\n
           font_name: 字体名称 (默认Arial)\n
           justify: 对齐方式 (默认居中)\n
           text_mode: 文本模式 (默认自动模式)(//wh: 宽高模式 / auto: 自动模式)\n
           width: 文本宽度 (默认300)\n
           height: 文本高度 (默认1)\n
           textvariable: 文本变量\n
           pos_mode: 位置模式 (默认xy模式)(xy: 绝对坐标/center: 中心坐标)\n"""
        self.master = master
        if textvariable:
            self.text = text
        else:
            self.text = StringVar()
            self.text.set(text)
        self.size = size
        self.color = color
        self.font_name = font_name
        self.pos = pos
        self.pos_center = (pos[0] - width / 2, pos[1] - height / 2)
        self.text_mode = text_mode
        self.width = width
        self.height = height
        self.pos_mode = pos_mode
        self.justify = justify
        self.font = font.Font(family=font_name, size=size)
        self.justify_dict = {"left": LEFT, "center": CENTER, "right": RIGHT}
        self.label = Label(master, font=self.font, fg=color,
                           justify=self.justify_dict[justify], wraplength=width, height=height,
                           textvariable=self.text)

    def set_text(self, text, **kwargs):
        """设置文本"""
        self.text.set(text)
        if kwargs:
            self.set_config(**kwargs)

    def set_pos(self, pos):
        """设置位置"""
        self.undraw()
        self.pos = pos
        self.pos_center = (pos[0] + self.width / 2, pos[1] + self.height / 2)
        self.draw()

    def draw(self):
        """绘制模块"""
        # print("Drawing TextModule", self.text)
        if self.pos_mode == "center":
            self.label.place(x=self.pos_center[0], y=self.pos_center[1])
        elif self.pos_mode == "xy":
            self.label.place(x=self.pos[0], y=self.pos[1])

    def undraw(self):
        self.label.place_forget()

    def copy(self, master):
        """复制模块
        复制时需要窗口信息，因此需要传入master"""
        return TextModule(master, self.pos, self.text.get(), self.size, self.color, self.font_name)

    def get_text(self):
        """获取文本"""
        return self.text.get()

    def set_config(self, **kwargs):
        """设置配置"""
        for key, value in kwargs.items():
            if key in self.__dict__:
                self.__dict__[key] = value
        self.label.config(
            fg=self.color,
            font=self.font,
            justify=self.justify_dict[self.justify],
            wraplength=self.width,
            height=self.height,
            textvariable=self.text
        )
