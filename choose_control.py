from modules.module_button import ButtonModule
from modules.module_text import TextModule
import tkinter as tk


class ChooseControl(tk.Frame):
    def __init__(self, ai_game, screen, allocation_plan):
        """控制选角页面"""
        super().__init__(screen)  # 继承Frame类，无需再次指定父容器
        self.ai = ai_game  # 传入上级self对象
        self.images = self.ai.images  # 角色图像
        self.allocation_plan = allocation_plan  # 传入布局方案
        # 控制实例
        self.flow = self.ai.flow  # 当前进行的流程
        self.enter_but = ButtonModule(self.master, self.allocation_plan["enter"], "确定",
                                      wid_hei=(10, 4), command=self.enter_click)  # 确认按钮
        self.now_image = self.images.get_sprite_image(self.master, "actor.png",
                                                      pos=self.allocation_plan["image"],
                                                      width=100, height=140)  # 当前选择的目标角色图像
        self.now_name = tk.StringVar()  # 当前选择的目标角色名称
        self.now_name.set("角色名称")  # 默认显示角色名称
        self.now_name_txt = TextModule(self.master, self.allocation_plan["name"], self.now_name,
                                       size=16, textvariable=True, color="grey")  # 当前选择的目标角色名称
        # 介绍文本
        self.intro1 = tk.StringVar()  # 介绍文本1
        self.intro1.set("介绍文本1")  # 默认显示介绍文本1
        self.intro1_txt = TextModule(self.master, self.allocation_plan["intro1"], self.intro1,
                                     size=12, textvariable=True, color="grey",
                                     width=420, height=10)  # 介绍文本1
        self.intro2 = tk.StringVar()  # 介绍文本2
        self.intro2.set("介绍文本2")  # 默认显示介绍文本2
        self.intro2_txt = TextModule(self.master, self.allocation_plan["intro2"], self.intro2,
                                     size=12, textvariable=True, color="grey",
                                     width=200, height=2)  # 介绍文本2
        # 属性文本
        self.attr_txt = []  # 属性文本
        for i in range(4):
            self.attr_txt.append(
                TextModule(self.master, self.allocation_plan["attr"][i], "值：0", size=12,
                           color="grey")
            )  # 属性文本
        # 基础变量
        self.name_base = "角色名称"  # 角色名称基础变量
        # 角色技能文本
        self.skills_txt = {}  # 角色技能文本
        for i in ["common", "combat", "ultimate", "passive"]:
            self.skills_txt[i] = TextModule(self.master, self.allocation_plan["skills"][i], "技能名称", size=12,
                                            color="grey")

        # 按键绑定
        self.key_bind_dict = {
            "space": self.enter_click
        }  # 按键绑定字典
        self.key_flag = False  # 按键标志位
        self.now_choose = self.ai.now_choose  # 当前选择的角色/装备

    def draw(self):
        """绘制页面"""
        self.enter_but.draw()  # 绘制确认按钮
        self.now_image.draw()  # 绘制目标角色图像
        self.now_name_txt.draw()  # 绘制目标角色名称
        for a in self.attr_txt:
            a.draw()  # 绘制属性文本
        self.intro1_txt.draw()  # 绘制介绍文本1
        self.intro2_txt.draw()  # 绘制介绍文本2
        for s in self.skills_txt.values():
            s.draw()  # 绘制角色技能文本

    def undraw(self):
        """清除页面"""
        self.enter_but.undraw()  # 清除确认按钮
        self.now_image.undraw()  # 清除目标角色图像
        self.now_name_txt.undraw()  # 清除目标角色名称
        for a in self.attr_txt:
            a.undraw()  # 清除属性文本
        self.intro1_txt.undraw()  # 清除介绍文本1
        self.intro2_txt.undraw()  # 清除介绍文本2
        for s in self.skills_txt:
            s.undraw()  # 清除角色技能文本

    def modification_data(self, data):
        """更新模块data: 角色/装备数据，这里需要传入数据用于更新"""
        # print(data)
        if self.now_choose == "actor":  # 若当前选择角色，则更新角色数据
            self.now_name_txt.set_text(data["name"], color="black")  # 更新当前选择的目标角色名称
            self.now_image.set_image(data["image"])  # 更新目标角色图像
            self.change_attr(self.attr_txt, data["attr"])  # 更新属性文本
            self.intro1_txt.set_text(data["story"], color="black")  # 更新介绍文本
            self.intro2_txt.set_text(data["role"], color="black")
            self.change_skills(self.skills_txt, data["skills"])  # 更新角色技能文本
            self.name_base = data.get("name_base", "角色名称")  # 更新角色名称基础变量
        elif self.now_choose == "equip":  # 若当前选择装备，则更新装备数据
            self.now_name_txt.set_text(data["name"], color="black")  # 更新当前选择的目标装备名称
            self.now_image.set_image(data["image"])  # 更新目标装备图像
            self.change_attr(self.attr_txt, data["attr"])  # 更新属性文本
            self.intro1_txt.set_text(data["description"], color="black")  # 更新介绍文本
            self.intro2_txt.set_text("", color="black")
        elif self.now_choose == "talent":  # 若当前选择天赋，则更新天赋数据
            self.now_name_txt.set_text(data["name"], color="black")  # 更新当前选择的目标天赋名称
            self.intro1_txt.set_text(data["description"], color="black")  # 更新介绍文本
            self.intro2_txt.set_text(data["tag"], color="black")

        self.key_flag = True  # 按键标志位置为True
        self.draw()  # 绘制页面

    def enter_click(self):
        """确认按钮点击事件"""
        if not self.key_flag:  # 若按键标志位为False，则不进行下一步
            return
        if self.ai.next_stage(self.now_name.get()):  # 进入下一流程
            return
        # 重置页面数据
        self.now_name_txt.set_text("角色名称", color="grey")  # 重置当前选择的目标角色名称
        self.now_image.set_image(self.images.get_image("actor.png"))  # 重置目标角色图像
        self.change_attr(self.attr_txt, ["值：0", "值：0", "值：0", "值：0"], color="grey")  # 重置属性文本
        self.intro1_txt.set_text("介绍文本1", color="grey")  # 重置介绍文本1
        self.intro2_txt.set_text("介绍文本2", color="grey")  # 重置介绍文本2
        for s in self.skills_txt.values():
            s.set_text("技能名称", color="grey")  # 重置角色技能文本
        self.key_flag = False  # 按键标志位置为True

    @staticmethod
    def change_attr(attr_list, value_list, color="black") -> None:
        """修改属性"""
        for i in range(len(attr_list)):  # 遍历属性列表
            if i+1 > len(value_list):  # 若属性值列表长度不足，则不显示属性值
                attr_list[i].set_text("", color=color)
            else:
                attr_list[i].set_text(f"{value_list[i]}", color=color)

    @ staticmethod
    def change_skills(skills_dict, skill_list, color="black") -> None:
        """修改技能"""
        pass





