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
        self.name_base = ""  # 角色基础名称
        self.now_name.set("角色名称")  # 默认显示角色名称
        self.now_name_txt = TextModule(self.master, self.allocation_plan["name"], self.now_name,
                                       size=16, textvariable=True, color="grey")  # 当前选择的目标角色名称
        self.attr_txt = []  # 属性文本
        for i in range(4):
            self.attr_txt.append(
                TextModule(self.master, self.allocation_plan["attr"][i], "值：0", size=12,
                           color="grey")
            )  # 属性文本
        self.key_bind_dict = {
            "space": self.enter_click
        }  # 按键绑定字典
        self.key_flag = False  # 按键标志位

    def draw(self):
        """绘制页面"""
        self.enter_but.draw()  # 绘制确认按钮
        self.now_image.draw()  # 绘制目标角色图像
        self.now_name_txt.draw()  # 绘制目标角色名称
        for a in self.attr_txt:
            a.draw()  # 绘制属性文本

    def undraw(self):
        """清除页面"""
        self.enter_but.undraw()  # 清除确认按钮

    def modification_data(self, data):
        """更新模块data: 角色/装备数据，这里需要传入数据用于更新"""
        self.now_name_txt.set_text(data["name"], color="black")  # 更新当前选择的目标角色名称
        self.name_base = data["name_base"]  # 更新角色基础名称
        self.now_image.set_image(data["image"])  # 更新目标角色图像
        self.change_attr(self.attr_txt, data["attr"])  # 更新属性文本
        self.key_flag = True  # 按键标志位置为True
        self.draw()  # 绘制页面

    def enter_click(self):
        """确认按钮点击事件"""
        if not self.key_flag:  # 若按键标志位为False，则不进行下一步
            return
        if self.ai.next_stage(self.now_name.get()):  # 进入下一流程
            return
        self.now_name_txt.set_text("角色名称", color="grey")  # 重置当前选择的目标角色名称
        self.now_image.set_image(self.images.get_image("actor.png"))  # 重置目标角色图像
        self.change_attr(self.attr_txt, ["值：0", "值：0", "值：0", "值：0"], color="grey")  # 重置属性文本
        self.key_flag = False  # 按键标志位置为True

    @staticmethod
    def change_attr(attr_list, value_list, color="black"):
        """修改属性"""
        for i in range(len(attr_list)):  # 遍历属性列表
            if i+1 > len(value_list):  # 若属性值列表长度不足，则不显示属性值
                attr_list[i].set_text("", color=color)
            else:
                attr_list[i].set_text(f"{value_list[i]}", color=color)





