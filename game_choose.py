""""用来完成对对局角色的选择"""
from modules.module_button import ButtonModule
from modules.module_text import TextModule
from choose_PlayerShow import ChooseShow
from choose_control import ChooseControl
from witelog import writelog
import tkinter as tk


class GameChoose:
    def __init__(self, screen, ai_game):
        """初始化游戏角色选择界面模块"""
        self.ai = ai_game  # 上级self实例
        self.images = self.ai.images  # 角色图片
        self.ai_screen = screen  # 屏幕实例
        self.screen = None
        # 角色选择
        self.actors = self.ai.actors  # 获取角色列表
        self.actor_choose = None  # 角色选择（数据模块）
        # 武器选择
        self.equips = self.ai.equips  # 获取武器列表
        self.equip_choose = None  # 武器选择（数据模块）
        # 天赋选择
        self.talents_choose = None  # 天赋选择（数据模块）
        # 界面初始化
        self.bin_text = None  # 版本号模块
        # 控制变量
        self.allocation_plan = {
            "PlayerShow": {
                "A": {"images": (10, 10), "player_name": (10, 80),
                      "main_actor": (70, 200), "main_actor_fu": (10, 200),
                      "main_equip": (70, 225), "main_equip_fu": (10, 225),
                      "helper_actor": (70, 300), "helper_actor_fu": (10, 300),
                      "helper_equip": (70, 325), "helper_equip_fu": (10, 325),
                      "talent": (70, 400), "talent_fu": (10, 400)},
                "B": {"images": (900, 10), "player_name": (900, 80),
                      "main_actor": (900, 200), "main_actor_fu": (835, 200),
                      "main_equip": (900, 225), "main_equip_fu": (835, 225),
                      "helper_actor": (900, 300), "helper_actor_fu": (835, 300),
                      "helper_equip": (900, 325), "helper_equip_fu": (835, 325),
                      "talent": (900, 400), "talent_fu": (835, 400)}},
            "Control": {
                "enter": (850, 550), "image": (10, 530), "name": (150, 550),
                "attr": [(150, 580), (250, 580), (150, 610), (250, 610)],
                "intro1": (370, 470), "intro2": (150, 620),
                "skills": {"common": (370, 650), "combat": (500, 650),
                           "ultimate": (370, 680), "passive": (500, 680)}}
        }  # 角色布局方案
        # 其他
        self.now_flow_txt = None  # 当前流程提示
        self.showA = None  # 玩家A的角色选择模块（显示模块）
        self.showB = None  # 玩家B的角色选择模块（显示模块）
        self.show_dict = None  # 角色选择模块字典（显示模块）
        self.control = None  # 控制模块（显示模块）
        self.get_actor_data = {
            "A": {},
            "B": {}
        }  # 角色/武器选择数据
        self.get_equip_data = {}
        # 控制变量
        self.camp = "A"  # 阵营
        self.camp_fu = {"A": "B", "B": "A"}  # 阵营互换
        self.now_choose = "actor"  # 当前选择类型
        self.choose_type = {"actor": "equip", "equip": "talent"}
        self.flow = "主战"  # 当前正在进行的选择
        self.flow_fu = {"主战": "助战", "助战": "武器", "武器": "天赋"}
        self.tag_flow = "主战"
        self.tag_flow_fu = {"主战": "助战", "助战": "主战"}  # 主助战标记
        self.stage = tk.StringVar()  # 角色提示信息
        self.stage2 = tk.StringVar()  # 角色提示信息
        self.stage_txt = None  # 当前流程提示
        self.stage_txt2 = None  # 当前流程提示
        self.stage_fu = {
            "主战": "当前流程：选择主战角色",
            "助战": "当前流程：选择助战角色",
            "武器": "当前流程：选择武器",
            "天赋": "当前流程：选择天赋"}  # 角色提示信息对应字典
        self.flow_fu2 = {
            "主战": "main",
            "助战": "helper",
            "武器": "equip",
            "天赋": "talent"}  # 角色选择流程对应字典
        self.stage_list = []
        # 其他
        self.need_actor_attr = ["at", "df", "sp", "rt"]  # 角色属性
        # 武器属性由内部模块读取
        self.attributes_name_fu = {
            "at": "攻击力", "df": "防御力",
            "kr": "暴击率", "kd": "暴击伤害",
            "sp": "速度", "rt": "抗性",
            "ids": "增伤", "vl": "易伤",
            "rh": "减伤", "ha": "免伤",
            "dr": "伤害倍率", "re": "回能"}  # 角色属性名称的复数形式
        self.key_bind_dict = {}  # 绑定键盘事件

    def init(self):
        """初始化游戏选择界面"""
        self.init_var()  # 初始化变量
        self.init_screen()  # 初始化游戏选择界面
        self.init_other()  # 初始化其他模块
        self.init_choose_config()  # 初始化角色选择配置
        self.draw()  # 绘制角色选择界面
        self.draw_fu()  # 绘制角色选择界面

    def init_var(self):
        """初始化变量"""
        self.get_actor_data = {
            "A": {},
            "B": {}
        }  # 角色选择数据
        self.get_equip_data = {}  # 武器选择数据
        self.camp = "A"  # 阵营
        self.now_choose = "actor"  # 当前选择类型
        self.flow = "主战"  # 当前正在进行的选择
        self.tag_flow = "主战"  # 主助战标记

    def init_screen(self):
        """初始化游戏选择界面"""
        self.screen = tk.Toplevel(self.ai_screen)
        self.screen.geometry(self.ai.screen)  # 注：此处的ai.screen为窗口大小，非窗口实例
        self.screen.title("游戏角色选择")
        self.screen.resizable(False, False)  # 禁止调整窗口大小
        self.screen.protocol("WM_DELETE_WINDOW", self.close)  # 关闭窗口时调用close()方法
        self.screen.bind("<Key>", self.key_press)

    def init_other(self):
        """初始化其他模块"""
        self.stage.set(self.stage_fu[self.flow])
        self.stage_txt = TextModule(self.screen, (600, 20), self.stage,
                                    size=14, width=400, textvariable=True,
                                    pos_mode="center")  # 当前流程提示
        self.stage2.set(f"选择方：{self.camp}")
        self.stage_txt2 = TextModule(self.screen, (600, 50), self.stage2,
                                     size=14, width=400, textvariable=True,
                                     pos_mode="center")  # 当前流程提示

        self.showA = ChooseShow(self, self.screen, self.allocation_plan["PlayerShow"]["A"])  # 实例化玩家A的角色选择模块
        self.showB = ChooseShow(self, self.screen, self.allocation_plan["PlayerShow"]["B"])  # 实例化玩家B的角色选择模块
        self.show_dict = {"A": self.showA, "B": self.showB}  # 角色选择模块字典
        self.control = ChooseControl(self, self.screen, self.allocation_plan["Control"])  # 实例化控制模块

        self.actor_choose = ActorChoose(self, self.screen, self.actors)  # 实例化角色选择模块
        self.actor_choose.init()  # 初始化角色选择界面
        self.equip_choose = EquipChoose(self, self.screen, self.equips)  # 实例化装备选择模块
        self.equip_choose.init()  # 初始化武器选择界面
        self.talents_choose = TalentChoose(self, self.screen)  # 实例化天赋选择模块
        self.bin_text = self.ai.bin_text.copy(self.screen)  # 复制版本号

    def init_talent(self):
        """初始化天赋选择"""
        self.talents_choose.init()
        return "初始化天赋"

    def init_choose_config(self):
        """初始化角色选择配置"""
        self.stage_list = [
            self.charge_camp,  # 切换阵营A->B
            [self.charge_flow, self.charge_tag_flow],  # 切换流程主战->助战
            self.charge_camp,  # 切换阵营B->A
            [self.charge_flow,  # 切换流程助战->武器
             self.charge_tag_flow,  # and 切换主助战标记, 助战->主战
             self.charge_choose_type,  # and 切换选择类型actor->equip
             self.charge_camp],  # 切换阵营A->B
            self.charge_tag_flow,  # 切换主助战标记, 主战->助战
            [self.charge_camp,  # 切换阵营B->A
             self.charge_tag_flow],  # and 切换主助战标记, 助战->主战
            self.charge_tag_flow,  # 切换阵营A->B
            [self.init_talent, self.charge_choose_type]  # 初始化天赋并切换选择类型actor->equip
        ]  # 流程图
        self.key_bind_dict = self.control.key_bind_dict  # 绑定键盘事件

    def draw(self):
        """绘制游戏选择界面"""
        self.showA.draw()
        self.showB.draw()
        self.control.draw()
        self.draw_text()

    def draw_fu(self):
        """作为切换流程时调用"""
        if self.now_choose == "actor":
            self.actor_choose.draw()
        elif self.now_choose == "equip":
            self.equip_choose.draw()
        elif self.now_choose == "talent":
            self.talents_choose.draw()

    def undraw(self):
        """隐藏游戏选择界面"""
        self.showA.undraw()
        self.showB.undraw()
        self.control.undraw()
        self.undraw_text()

    def undraw_fu(self):
        if self.now_choose == "actor":
            self.actor_choose.undraw()
        elif self.now_choose == "equip":
            self.equip_choose.undraw()
        elif self.now_choose == "talent":
            self.talents_choose.undraw()

    def draw_text(self):
        """绘制文本"""
        self.bin_text.draw()
        self.stage_txt.draw()
        self.stage_txt2.draw()

    def undraw_text(self):
        """隐藏文本"""
        self.bin_text.undraw()
        self.stage_txt.undraw()
        self.stage_txt2.undraw()

    def open(self):
        """打开游戏选择界面"""
        self.run()

    def run(self):
        """运行游戏选择界面"""
        self.init()

    def close(self):
        """关闭游戏"""
        self.ai.open()
        self.screen.destroy()  # 销毁子窗口

    def decide(self, temp):  # 这里的temp是选中的角色/武器数据
        """确定选择: 注：此处会在角色/武器内部调用"""
        attr_temp = []
        # 保存选中数据
        data = {}
        if self.now_choose == "actor":  # 角色属性读取
            skills_temp = {}
            for attr in self.need_actor_attr:  # 读取角色属性
                attr_temp.append(f"{self.attributes_name_fu[attr]}: {temp['attributes'][attr]}")
                # "at: 100, df: 100, sp: 100, rt: 100" 类似这样的字符串
            data = {
                "name": temp["name"],
                "name_base": temp.get("name_base", ""),
                "attr": attr_temp,
                "image": temp["image"],
                "story": temp.get("story", ""),
                "role": temp.get("role", ""),
                "skills": temp.get("skills", "")
            }
        if self.now_choose == "equip":  # 武器属性读取
            for attr in temp["attr_use"]:
                attr_temp.append(f"{self.attributes_name_fu[attr]}: {temp['attributes'][attr]}")
                # "at: 100, df: 100, sp: 100, rt: 100" 类似这样的字符串
            data = {
                "name": temp["name"],
                "attr": attr_temp,
                "image": temp["image"],
                "description": temp.get("description", "")
            }
        if self.now_choose == "talent":  # 天赋读取
            data = {
                "name": temp["name"],
                "description": temp.get("description", ""),
                "tag": temp.get("tag", "")
            }
        self.control.modification_data(data)

    def next_stage(self, name):
        """进入下一阶段"""
        active = True  # 标记是否切换流程
        if self.now_choose == "actor":
            self.actor_choose.actor_buttons[name].lock()
            self.show_dict[self.camp].charge_info(
                self.flow_fu2[self.flow],
                self.control.name_base
            )
            active = False
            self.get_actor_data[self.camp][self.flow] = name
            writelog(f"选择角色：{self.camp} {self.flow} {name}")
        elif self.now_choose == "equip":
            self.equip_choose.equip_buttons[name].lock()
            self.show_dict[self.camp].charge_info(
                f"{self.flow_fu2[self.tag_flow]}_{self.flow_fu2[self.flow]}",
                self.control.now_name.get()
            )
            active = False
            self.get_equip_data[self.tag_flow + self.camp] = name
            writelog(f"选择武器：{self.tag_flow} {self.camp} {name}")
        elif self.now_choose == "talent":
            active = False
            writelog(f"选择天赋：{self.tag_flow} {self.camp} {name}")

        if active:  # 若为True，则意味着没有触发
            return
        # 切换流程
        if len(self.stage_list) == 0:  # 若流程图为空，则意味着选择结束
            self.begin_game()
            return True  # 结束选择
        # 切换当前流程
        temp = self.stage_list.pop(0)
        if type(temp) is list:
            for i in temp:
                writelog(i())
        else:
            writelog(temp())
        self.stage.set(self.stage_fu[self.flow])
        self.stage2.set(f"选择方：{self.camp}")

    def charge_camp(self):
        """切换阵营"""
        self.camp = self.camp_fu[self.camp]
        return f"切换阵营：{self.camp}"

    def charge_tag_flow(self):
        """切换主助战标记"""
        self.tag_flow = self.tag_flow_fu[self.tag_flow]
        return f"切换主助战标记：{self.tag_flow}"

    def charge_flow(self):
        """切换流程"""
        self.flow = self.flow_fu[self.flow]
        return f"切换流程：{self.flow}"

    def charge_choose_type(self):
        """切换选择类型"""
        self.undraw_fu()
        self.now_choose = self.choose_type[self.now_choose]
        self.control.now_choose = self.now_choose
        self.draw_fu()
        return f"切换选择类型：{self.now_choose}"

    def key_press(self, event):
        """键盘事件"""
        if event.keysym in self.key_bind_dict:
            self.key_bind_dict[event.keysym]()  # 调用绑定的函数

    def begin_game(self):
        """开始游戏"""
        self.ai.game_actor_temp = self.get_actor_data
        self.ai.game_equip_temp = self.get_equip_data
        writelog("选择角色：" + str(self.get_actor_data))
        writelog("选择武器：" + str(self.get_equip_data))
        self.close()
        self.ai.game_main_show()  # 进入游戏


class ActorChoose(tk.Frame):
    def __init__(self, ai, screen, actors: dict):
        super().__init__(screen)
        self.ai = ai  # 上级self实例
        self.actors = actors  # 获取角色列表
        self.actor_buttons = {}
        self.pos = (220, 75)  # 模块位置

    def init(self):
        """初始化角色选择界面"""
        x = 0
        y = 0
        for name, actor in self.actors.items():
            actor.choose_command = self.ai.decide
            button = ButtonModule(self.master, (self.pos[0] + x, self.pos[1] + y),
                                  actor.name_base,
                                  command=actor.run_choose_command,
                                  wid_hei=(10, 2), size=9)
            self.actor_buttons[name] = button
            if x > 700:
                x = 0
                y += 30
            else:
                x += 100

    def draw(self):
        """绘制角色选择界面"""
        for button in self.actor_buttons.values():
            button.draw()

    def undraw(self):
        """隐藏角色选择界面"""
        for button in self.actor_buttons.values():
            button.undraw()


class EquipChoose(tk.Frame):
    def __init__(self, ai, screen, equips: dict):
        super().__init__(screen)
        self.ai = ai  # 上级self实例
        self.equips = equips  # 获取
        self.equip_buttons = {}
        self.pos = (220, 75)  # 模块位置

    def init(self):
        """初始化装备选择界面"""
        x = 0
        y = 0
        for name, equip in self.equips.items():
            equip.choose_command = self.ai.decide
            button = ButtonModule(self.master, (self.pos[0] + x, self.pos[1] + y),
                                  equip.name,
                                  command=equip.run_choose_command,
                                  wid_hei=(10, 2), size=9)
            if x > 700:
                x = 0
                y += 30
            else:
                x += 100
            self.equip_buttons[name] = button

    def draw(self):
        """绘制装备选择界面"""
        for button in self.equip_buttons.values():
            button.draw()

    def undraw(self):
        """隐藏装备选择界面"""
        for button in self.equip_buttons.values():
            button.undraw()


class TalentChoose(tk.Frame):
    def __init__(self, ai, screen):
        """天赋选择模块
        其中天赋数据需要在当前选择的角色数据中获取"""
        super().__init__(screen)
        self.ai = ai  # 上级self实例
        self.actors = self.ai.actors  # 获取角色列表
        self.get_actor_data = self.ai.get_actor_data  # 角色选择数据
        self.talents_buttons_A = {}  # A天赋列表
        self.talents_buttons_B = {}  # B天赋列表
        self.talents_fu = {
            "A": self.talents_buttons_A,
            "B": self.talents_buttons_B
        }  # 阵营指向
        self.pos = (220, 75)  # 模块位置
        self.camp = self.ai.camp  # 阵营
        self.camp_fu = {"A": "B", "B": "A"}  # 阵营切换

    def init(self):
        """初始化天赋选择界面"""
        for camp in ["A", "B"]:
            self.init_talents(self.talents_fu[camp], self.get_actor_data[camp]["主战"])

    def init_talents(self, data_dict, name):
        """初始化天赋选择界面"""
        x = 0
        y = 0
        print(self.actors[name].talents)
        for talent_name in self.actors[name].talents:
            button = ButtonModule(self.master, (self.pos[0] + x, self.pos[1] + y),
                                  talent_name,
                                  command=None,
                                  wid_hei=(10, 2), size=9)
            if x > 700:
                x = 0
                y += 30
            else:
                x += 100
            data_dict[talent_name] = button

    def draw(self):
        """绘制天赋选择界面"""
        if self.camp == "A":
            for button in self.talents_buttons_A.values():
                button.draw()
        else:
            for button in self.talents_buttons_B.values():
                button.draw()

    def undraw(self):
        """隐藏天赋选择界面"""
        if self.camp == "A":
            for button in self.talents_buttons_A.values():
                button.undraw()
        else:
            for button in self.talents_buttons_B.values():
                button.undraw()
