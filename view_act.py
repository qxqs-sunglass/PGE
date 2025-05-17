import witelog
from modules.module_text import TextModule
from modules.module_button import ButtonModule
import tkinter
import math


class ViewAct:
    def __init__(self, master, acts):
        """显示角色
        master: 主窗口: tkinter.Tk()
        acts: 角色字典{name[中文]: act[type:class]}"""
        self.root = master  # 主窗口
        self.master = None  # 子窗口
        self.acts = acts  # 角色字典{name[中文]: act[type:class]}
        self.title_text = None  # 标题文字对象
        self.act_buttons = []  # 角色详细信息跳转按钮
        self.act_names = []  # 角色名字/string
        self.interval = 70  # 角色显示之间的间隔
        self.col_number = 5  # 一页页面显示的行数/角色数
        self.page_number = None  # 最大页数
        self.page_text = None  # 页数文字
        self.page = 1  # 页数
        self.last_page_button = None  # 上一页按钮
        self.next_page_button = None  # 下一页按钮

    def unshow(self):
        """隐藏（改变页面时）"""
        # 隐藏角色名和跳转按钮(因为page是1~n, 所以这里是(page-1)~page)
        for i in range((self.page - 1) * self.col_number, self.page * self.col_number):
            if i >= len(self.act_names):  # 索引超出范围
                break
            self.act_names[i].undraw()  # 隐藏角色名
            self.act_buttons[i].undraw()  # 隐藏角色按钮
        # 隐藏角色名和跳转按钮结束
        self.page_text.undraw()  # 隐藏页面文字

    def last_page_button_command(self):
        """上一页指令"""
        if self.page <= 1:
            return
        self.unshow()
        self.page -= 1
        self.show()

    def next_page_button_command(self):
        """下一页指令"""
        if self.page >= self.page_number:
            return
        self.unshow()
        self.page += 1
        self.show()

    def init(self):
        """初始化窗口"""
        self.master = tkinter.Toplevel(self.root)  # 子窗口
        self.master.title("角色")  # 子窗口标题
        self.master.geometry("400x600")
        self.master.protocol("WM_DELETE_WINDOW", self.close)  # 关闭窗口时调用close()方法
        self.master.resizable(False, False)  # 禁止调整窗口大小
        self.master.withdraw()  # 隐藏子窗口
        self.page_number = math.ceil(len(self.acts) / self.col_number)
        self.title_text = TextModule(
            self.master,
            (115, 20),
            "角色信息展示",
            20
        )
        # 角色名对象列表和按钮列表创建
        col = 0  # 遍历每一行的临时变量
        for act_name in self.acts.keys():
            # 创建对象
            text_string = f"{act_name}:"
            button_string = f"详细信息"
            text_module = TextModule(
                self.master,
                (20, 100 + col * self.interval),
                text_string
            )
            button_module = ButtonModule(
                self.master,
                (20 + text_module.width, 100 + col * self.interval),
                button_string,
                self.acts[act_name].show,
                (15, 1)
            )
            # 加入列表
            self.act_names.append(text_module)
            self.act_buttons.append(button_module)
            col += 1  # 行数变多一个
            col %= self.col_number  # 保持在页面行数以下
        # 角色名对象列表和按钮列表创建结束
        self.page_text = TextModule(
            self.master,
            (175, 550),
            "第0页"
        )
        self.last_page_button = ButtonModule(
            self.master,
            (30, 550),
            "上一页",
            self.last_page_button_command
        )
        self.next_page_button = ButtonModule(
            self.master,
            (315, 550),
            "下一页",
            self.next_page_button_command
        )

    def show(self):
        """显示角色"""
        self.title_text.draw()
        self.page_text.set_text(f"第{self.page}页")
        self.page_text.draw()
        self.last_page_button.draw()
        self.next_page_button.draw()
        # 显示角色名和跳转按钮(因为page是1~n, 所以这里是(page-1)~page)
        for i in range((self.page - 1) * self.col_number, self.page * self.col_number):
            if i >= len(self.act_names):  # 索引超出范围
                break
            self.act_names[i].draw()  # 显示角色名
            self.act_buttons[i].draw()  # 显示角色按钮
        # 显示角色名和跳转按钮结束
        self.master.deiconify()  # 显示子窗口

    def close(self):
        """关闭窗口"""
        self.master.withdraw()  # 隐藏子窗口
