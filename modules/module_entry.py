from tkinter import Entry
from module_text import TextModule


class EntryModule:
    def __init__(self, master, pos, text,
                 wid_hei=(100, 20), size=12, attr="left",
                 txtpos_mode="xy"):
        """输入框模块
           master: 窗口对象
           pos: 位置坐标
           text: 文本内容
           wid_hei: 控件大小 (宽, 高)
           size: 字体大小
           attr: 文本位置(left, bottom)
           txtpos_mode: 文本位置模式(xy, center)"""
        self.master = master
        self.pos = pos
        self.width, self.height = wid_hei
        self.txtpos_mode = txtpos_mode
        self.attr = attr
        if attr == "left":
            self.txt_pos = (pos[0]+self.width, pos[1])
        elif attr == "bottom":
            self.txt_pos = (pos[0]+self.width/2, pos[1]+self.height)
            self.txtpos_mode = "center"
        self.text_msg = text
        self.text = TextModule(master, self.txt_pos,
                               text=text, size=size, pos_mode=txtpos_mode,
                               textvariable=True)
        self.entry = Entry(self.master)

    def draw(self):
        """绘制控件"""
        self.entry.place(x=self.pos[0], y=self.pos[1], width=self.width, height=self.height)
        self.text.draw()

    def undraw(self):
        """隐藏控件"""
        self.entry.place_forget()
        self.text.undraw()

    def set_pos(self, pos):
        """设置控件位置"""
        self.undraw()
        self.pos = pos
        self.draw()

    def set_text(self, text):
        """设置文本内容"""
        self.entry.insert(0, text)

    def get_text(self):
        """获取文本内容"""
        return self.entry.get()
