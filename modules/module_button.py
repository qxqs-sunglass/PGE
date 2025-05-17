from tkinter import Button, font, CENTER, RIGHT, LEFT
from PIL import ImageTk


class ButtonModule:
    """按键模块"""
    def __init__(self, master, pos, text, command=None, wid_hei=(5, 1),
                 size=12, color="black", font_name="Arial", justify="center",
                 image=None):
        """master: 窗口对象
           pos: 位置坐标
           text: 按钮文字
           command: 按钮命令
           wid_hie: 按钮宽高
           size: 字体大小, 默认12
           color: 字体颜色, 默认黑色
           font_name: 字体类型, 默认Arial
           justify: 文字对齐方式, 默认居中(center)/可选(right, left)
           image: 按钮图片,注：此图片为: tk.PhotoImage 对象"""
        self.master = master
        self.wid_hei = wid_hei
        self.width = self.wid_hei[0]
        self.height = self.wid_hei[1]
        self.text = text
        self.size = size
        self.font_name = font_name
        self.pos = pos
        self.color = color
        self.command = command
        self.justify = justify
        self.image_temp = image
        if self.image_temp is not None:
            self.image_temp = self.image_temp.resize((self.width, self.height))
            self.image = ImageTk.PhotoImage(self.image_temp)
        else:
            self.image = None
        self.justify_dict = {"center": CENTER, "right": RIGHT, "left": LEFT}
        self.font = font.Font(family=self.font_name, size=self.size)
        self.button = Button(self.master, text=self.text, font=self.font,
                             command=command, width=self.width, height=self.height,
                             justify=self.justify_dict[self.justify],
                             fg=self.color, image=self.image, compound="center")

    def set_text(self, text, justify=None):
        self.text = text
        self.button.config(text=self.text)
        if justify is not None:
            self.justify = justify
            if justify == "center":
                self.button.config(justify="center")
            elif justify == "right":
                self.button.config(justify="right")
            elif justify == "left":
                self.button.config(justify="left")
        self.draw()

    def set_command(self, command):
        self.command = command
        self.button.config(command=self.command)

    def set_pos(self, pos):
        self.pos = pos
        self.draw()

    def draw(self):
        self.button.place(x=self.pos[0], y=self.pos[1])

    def undraw(self):
        self.button.place_forget()

    def copy(self):
        return ButtonModule(self.button.master, self.pos, self.text, self.command, self.wid_hei,
                            self.size, self.color, self.font_name, self.button.cget("justify"))

    def lock(self):
        self.button.config(state="disabled")

    def unlock(self):
        self.button.config(state="normal")

