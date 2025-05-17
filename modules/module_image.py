import tkinter as tk
from PIL import ImageTk


class ImageModule:
    def __init__(self, master, pos: (int, int), image=None,
                 wid_hei=(10, 10), pic_mode="img"):
        """图片类模板\n
        master: 父容器\n
        pos: 图片位置\n
        image: 图片对象，如果image参数不能为空
        注：image是PIL.Image对象\n
        wid_hei: 图片宽高\n
        pic_mode: 图片模式(默认img: PIL.Image)(sprite: tkinter.PhotoImage)"""
        self.master = master  # 父容器
        self.pos = pos  # 图片位置
        self.wid_hei = wid_hei  # 图片宽高
        self.width = self.wid_hei[0]  # 图片宽
        self.height = self.wid_hei[1]   # 图片高
        self.pic_mode = pic_mode  # 图片模式
        # 执行图片初始化
        if self.pic_mode == "img":
            self.image_temp = image.resize(self.wid_hei)  # 缩放图片: 注：resize方法返回一个新的图片对象
            self.image: tk.PhotoImage = ImageTk.PhotoImage(self.image_temp)  # 转换为tkinter的图片对象
        elif self.pic_mode == "sprite":
            self.image_temp = image  # 图片对象
            self.image = self.image_temp  # tk图片对象
        self.label = tk.Label(self.master, image=self.image, text="A")  # 创建标签
        self.label.image = self.image  # 绑定图片到标签

    def draw(self):
        """绘制图片"""
        self.label.place(x=self.pos[0], y=self.pos[1])

    def undraw(self):
        """隐藏图片"""
        self.label.place_forget()

    def copy(self):
        """复制图片对象"""
        return ImageModule(self.master, self.pos, image=self.image, wid_hei=self.wid_hei, pic_mode="sprite")

    def set_image(self, image, mode="img"):
        """设置图片对象"""
        if mode == "img":
            image.thumbnail(self.wid_hei)  # 缩放图片
            self.image = ImageTk.PhotoImage(image)  # 转换为tkinter的图片对象
            self.label.configure(image=self.image)  # 设置标签的图片
        elif mode == "sprite":
            self.image = image  # tk图片对象
            self.label.config(image=self.image)
        self.draw()  # 绘制图片



