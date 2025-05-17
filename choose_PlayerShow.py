from modules.module_text import TextModule
import tkinter as tk


class ChooseShow(tk.Frame):
    def __init__(self, ai, screen, allocation_plan):
        """选择模块的玩家信息展示模块"""
        super().__init__(master=screen)
        self.ai = ai  # 传入上级self实例
        # self.ai_image = self.ai.images  # 图片总类
        self.allocation_plan = allocation_plan  # 传入布局方案
        # 玩家信息
        # self.player_image = None  # 玩家头像
        # self.player_name = ""  # 玩家名称
        # self.player_name_txt = None  # 玩家名称文本模块
        self.main_actor = tk.StringVar()  # 主战，这里是string类型
        self.main_actor.set("主战")  # 主战默认值
        self.main_actor_txt = TextModule(self.master, self.allocation_plan["main_actor"],
                                         self.main_actor, textvariable=True,
                                         justify="center", size=16, color="grey")  # 主战文本
        self.main_actor_txt_fu = TextModule(self.master, self.allocation_plan["main_actor_fu"],
                                            "主战: ", justify="center", size=16)  # 主战文本
        # 装备信息
        self.main_equip = tk.StringVar()  # 武器，这里是string类型
        self.main_equip.set("主战武器")  # 装备默认值
        self.main_equip_txt = TextModule(self.master, self.allocation_plan["main_equip"],
                                         self.main_equip, textvariable=True,
                                         justify="center", size=12, color="grey")  # 装备文本
        self.main_equip_txt_fu = TextModule(self.master, self.allocation_plan["main_equip_fu"],
                                            "武器: ", justify="center", size=12)  # 装备文本

        # 助战信息
        self.helper_actor = tk.StringVar()  # 助战，这里是string类型
        self.helper_actor.set("助战")  # 助战默认值
        self.helper_actor_txt = TextModule(self.master, self.allocation_plan["helper_actor"],
                                           self.helper_actor, textvariable=True,
                                           justify="center", size=16, color="grey")  # 助战文本
        self.helper_actor_txt_fu = TextModule(self.master, self.allocation_plan["helper_actor_fu"],
                                              "助战: ", justify="center", size=16)  # 助战文本
        # 装备信息
        self.helper_equip = tk.StringVar()  # 武器，这里是string类型
        self.helper_equip.set("助战武器")  # 装备默认值
        self.helper_equip_txt = TextModule(self.master, self.allocation_plan["helper_equip"],
                                           self.helper_equip, textvariable=True,
                                           justify="center", size=12, color="grey")  # 装备文本
        self.helper_equip_txt_fu = TextModule(self.master, self.allocation_plan["helper_equip_fu"],
                                              "武器: ", justify="center", size=12)  # 装备文本
        # 天赋信息
        self.talent_info = tk.StringVar()  # 天赋信息，这里是string类型
        self.talent_info.set("天赋信息")  # 天赋信息默认值
        self.talent_info_txt = TextModule(self.master, self.allocation_plan["talent"],
                                          self.talent_info, textvariable=True,
                                          justify="center", size=12, color="grey")  # 天赋信息文本
        self.talent_info_txt_fu = TextModule(self.master, self.allocation_plan["talent_fu"],
                                             "天赋: ", justify="center", size=12)  # 天赋信息文本

        self.shooter_dict = {
            "main": self.main_actor_txt.set_text,
            "main_equip": self.main_equip_txt.set_text,
            "helper": self.helper_actor_txt.set_text,
            "helper_equip": self.helper_equip_txt.set_text,
            "talent": self.talent_info_txt.set_text
        }  # 控制修改
        self.draw()  # 绘制模块

    def draw(self):
        """绘制模块"""
        self.main_actor_txt.draw()
        self.main_actor_txt_fu.draw()
        self.helper_actor_txt.draw()
        self.helper_actor_txt_fu.draw()
        self.main_equip_txt.draw()
        self.main_equip_txt_fu.draw()
        self.helper_equip_txt.draw()
        self.helper_equip_txt_fu.draw()
        self.talent_info_txt.draw()
        self.talent_info_txt_fu.draw()

    def undraw(self):
        """隐藏模块"""
        self.main_actor_txt.undraw()
        self.main_actor_txt_fu.undraw()
        self.helper_actor_txt.undraw()
        self.helper_actor_txt_fu.undraw()
        self.main_equip_txt.undraw()
        self.main_equip_txt_fu.undraw()
        self.helper_equip_txt.undraw()
        self.helper_equip_txt_fu.undraw()
        self.talent_info_txt.undraw()
        self.talent_info_txt_fu.undraw()

    def charge_info(self, charge_value: str, charge_info: None) -> None:
        """更该玩家信息"""
        # charge_value储存的是对应属性的名称，charge_info储存的是对应属性的值
        # print("charge_value:", charge_value, "charge_info:", charge_info)
        if charge_value in self.shooter_dict:
            self.shooter_dict[charge_value](charge_info, color="black")  # 调用对应属性的设置方法



