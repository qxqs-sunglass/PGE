from modules.module_image import ImageModule
from PIL import Image, ImageTk
import os
import tkinter as tk


class ImportImage:
    def __init__(self):
        self.file_path = [
            "resources/images/actors/",  # 角色路径
            "resources/images/equips/",  # 武器路径
            "resources/images/others/",  # 其他路径
            "resources/images/user/"  # 用户路径
            ]  # 图片路径
        self.file_type = [".png", ".jpg"]  # 图片类型
        self.file_dict = {}  # 单图片路径字典
        # 整合图片路径
        for path in self.file_path:   # 读取路径下所有文件
            for file in os.listdir(path):
                if os.path.splitext(file)[1] in self.file_type:
                    self.file_dict[file] = os.path.join(path, file)  # {文件名：文件路径}
        # 初始化图片实例
        self.image_dict = {}
        for file, path in self.file_dict.items():
            self.image_dict[file] = Image.open(path)  # {文件名：图片实例}

    def get_sprite_image(self, master, file_name, pos=(0, 0), width=100, height=140):
        """获取图片标签实例"""
        if file_name not in self.file_dict:
            return ImageModule(
                master,
                pos,
                image=self.get_image("error.png"),
                wid_hei=(width, height)
            )
        return ImageModule(
            master,
            pos,
            image=self.get_image(file_name),
            wid_hei=(width, height)
        )

    def get_image(self, file_name):
        """获取图片实例注：此处仅为图片，不能直接使用"""
        return self.image_dict[file_name]



