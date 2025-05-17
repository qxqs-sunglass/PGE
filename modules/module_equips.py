from modules.module_text import TextModule
import json
import tkinter as tk


class EquipTemplate:
    def __init__(self):
        """装备模板类"""
        self.attributes_name = ["at", "kr", "kd", "sp",
                                "vl", "rh", "ha",
                                "dr", "re"]  # 装备属性名称
        # at: 攻击力, kr: 暴击率, kd: 暴击伤害, sp: 速度,
        # vl: 易伤, rh: 减伤, ha: 免伤
        # dr: 伤害倍率, re: 回能
        self.attributes_name_fu = {"at": "攻击力",
                                   "kr": "暴击率", "kd": "暴击伤害",
                                   "sp": "速度", "vl": "易伤",
                                   "rh": "减伤", "ha": "免伤",
                                   "dr": "伤害倍率", "re": "回能"}  # 装备属性名称的复数形式
        self.attr_use = []  # 这里在装备类中定义装备属性的使用情况，比如：["攻击", "防御", "暴击", "速度", "回能"]
        # 根据装备所需要的属性，在attr_use中添加相应的属性名称
        # 装备信息
        self.name = ""  # 装备名称
        self.user = None  # 装备使用者: 角色实例
        self.image = None  # 装备图片
        self.equip_type = []  # 装备类型
        self.equip_global = [False, False]
        self.buff_tag = []  # 装备buff
        self.buff_value = []  # 装备buff值
        self.description = ""  # 装备描
        self.attributes_base = {}  # 装备基础属性
        self.attributes = {}  # 装备属性
        self.path = ""  # 数据文件路径
        self.path_data = {}  # 数据文件内容
        # 信息展示
        self.show_msg_fu = {"at": "攻击力", "kr": "暴击率", "kd": "暴击伤害",
                            "sp": "速度", "re": "回能", "description": "技能描述"}
        self.show_msg_fu2 = {"攻击力": "at", "暴击率": "kr",
                             "暴击伤害": "kd", "速度": "sp", "回能": "re",
                             "技能描述": "description"}
        self.attr_use = []  # 装备属性使用情况
        self.show_msg = {}  # 装备展示信息
        self.screen = None  # 屏幕对象
        self.position_attr = {"1": (10, 10), "2": (10, 75)}
        # 其他
        self.choose_command = None  # 选择命令

    def init(self, ai, screen):
        self.load_data()
        self.init_screen(screen)
        self.init_info(ai)

    def init_screen(self, screen):
        self.screen = tk.Toplevel(screen)
        self.screen.title(self.name)
        self.screen.geometry("300x300")
        self.screen.resizable(False, False)
        self.screen.protocol("WM_DELETE_WINDOW", self.close_window)  # 关闭窗口时调用close_window方法
        self.screen.withdraw()

    def init_info(self, ai):
        """展示装备信息"""
        self.image = ai.images.get_sprite_image(self.screen, self.name, width=200, height=200)
        a = 1
        for attr in self.attr_use:
            txt = f"{self.show_msg_fu[attr]}： {self.attributes[attr]}"
            self.show_msg[attr] = TextModule(self.screen, self.position_attr[str(a)],
                                             txt)
            self.show_msg[attr].draw()
            a += 1

    def update_info(self):
        """更新装备信息"""
        for attr in self.attr_use:
            self.show_msg[attr].set_text(self.attributes[attr])

    def show(self):
        self.screen.deiconify()
        self.update_info()

    def close_window(self):
        self.screen.withdraw()

    def load_data(self):
        if self.path == "":
            return
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.path_data = data
        self.name = data["name"]
        self.description = data["description"]
        for attr in self.attr_use:
            if attr not in data:
                continue
            self.attributes_base[attr] = data[attr]
        self.attributes = self.attributes_base.copy()

    def use(self, **kwargs):
        """使用装备技能"""

    def get_name(self):
        """获取装备名称"""
        return self.name

    def get_description(self):
        """获取装备描述"""
        return self.description

    def get_data(self):
        """获取装备数据"""
        return {
            "name": self.name,
            "image": self.image.image_temp,
            "description": self.description,
            "attributes": self.attributes_base,
            "attr_use": self.attr_use,
        }

    def run_choose_command(self):
        """选择命令"""
        self.choose_command(self.get_data())


