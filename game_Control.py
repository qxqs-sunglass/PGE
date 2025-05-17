from modules.module_text import TextModule
from modules.module_button import ButtonModule
import tkinter as tk


class GameControl(tk.Frame):
    def __init__(self, ai_game, master):
        """游戏控制模块"""
        super().__init__(master)
        self.ai = ai_game
        self.master = master
        self.axle_game = self.ai.axle_game  # 行动轴
        self.actor = self.ai.actor  # 角色
        self.actor_name = self.ai.actor_name  # 角色名称
        self.pos = {"A": (30, 250), "B": (700, 250)}
        x, y = self.pos["A"]
        x_b, y_b = self.pos["B"]
        self.pos_dict = {"A": {"choose_now": (x - 25, y + 230), "next_turn": (x + 200, y + 225),
                               "skill_msg": (x - 25, y + 260)},
                         "B": {"choose_now": (x_b - 25, y_b + 230), "next_turn": (x_b + 200, y_b + 225),
                               "skill_msg": (x_b - 25, y_b + 260)}}  # 位置字典
        self.act_use_frame = {}  # 释放技能模块
        self.act_role = ["主战A", "助战A",
                         "主战B", "助战B"]  # 角色所属：主战/助战
        self.now_act = "主战A"  # 当前释放技能的角色。
        self.play = self.ai.play  # 玩家
        self.camp = self.ai.camp  # 阵营
        self.camp_fu = self.ai.camp_fu  # 相对互换
        # 文本
        self.choose_now_txt = None  # 当前选中
        self.skill_msg_txt = None  # 显示技能效果的文本模块
        # 按钮
        self.next_turn_btn = None  # 下一回合按钮
        # 状态变量
        self.choose_active = False  # 选中提示框是否激活
        self.choose_key = None  # 选中提示框的键位
        self.key_bind_dict = {"q": self.key_q, "w": self.key_w, "e": self.key_e,  # 大小写共用
                              "Q": self.key_q, "W": self.key_w, "E": self.key_e}  # 按键绑定字典

    def init(self):
        """初始化游戏控制模块"""
        self.camp = self.ai.actor[self.axle_game.doing_actions[0]].camp
        self.choose_now_txt = TextModule(self.master, self.pos_dict[self.camp]["choose_now"], "当前选中：",
                                         justify="left")
        self.next_turn_btn = ButtonModule(self.master, self.pos_dict[self.camp]["next_turn"], "下一回合",
                                          self.ai.next_turn, wid_hei=(7, 1))
        self.skill_msg_txt = TextModule(self.master, self.pos_dict[self.camp]["skill_msg"], "技能效果：",
                                        justify="left", width=300, height=10)
        for name, act in self.actor_name.items():
            # name：角色所属名称：主战A/助战A/主战B/助战B，act：角色名称
            self.act_use_frame[name] = ChooseModule(self, self.master, self.pos[name[-1]], self.actor[act])  # 释放技能模块
            self.act_use_frame[name].init()   # 初始化释放技能模块
        self.now_act = self.ai.actor_name_fu[self.axle_game.doing_actions[0]]

    def draw(self):
        """绘制游戏控制模块"""
        self.skill_msg_txt.draw()
        self.choose_now_txt.draw()
        self.next_turn_btn.draw()
        self.act_use_frame[self.now_act].draw()

    def undraw(self):
        """隐藏游戏控制模块"""
        self.choose_now_txt.undraw()
        self.next_turn_btn.undraw()

    def undraw_act_use_frame(self):
        """隐藏释放技能模块"""
        self.act_use_frame[self.now_act].undraw()

    def use_skill(self, target, our, temp, actor):
        """释放技能
        在调用角色的use_skill（）前需要将敌我双方的角色信息传入，并将角色名称传入。"""
        actor.use_skill(skill_name=self.act_use_frame[self.now_act].choose_msg,
                        target=target,
                        our=our,
                        temp=temp)
        # 调用角色的use_skill方法释放技能
        self.act_use_frame[self.now_act].choose_msg = ""  # 隐藏选中提示信息
        self.skill_msg_txt.set_text("")  # 隐藏技能效果
        self.choose_now_txt.set_text("")  # 隐藏选中提示信息

    def update_turn(self):
        """更新回合"""
        self.update_now_act()  # 更新当前释放技能的角色
        self.skill_msg_txt.set_text("技能效果：")  # 隐藏技能效果
        self.choose_now_txt.set_text("当前选中：")  # 隐藏选中提示信息

    def update_now_act(self):
        """更新当前释放技能的角色"""
        self.undraw_act_use_frame()  # 隐藏角色技能选择模块
        if not self.axle_game.doing_actions:  # 若无行动，则下一回合
            self.now_act = ""
        else:
            self.now_act = self.ai.actor_name_fu[self.axle_game.doing_actions[0]]
            self.act_use_frame[self.now_act].draw()

    def key_q(self):
        """按键Q"""
        if self.choose_active and self.choose_key == "q":  # 选中提示框激活
            self.choose_active = False  # 关闭选中提示框
            self.next_turn_btn.command()  # 释放技能
        else:
            self.act_use_frame[self.now_act].choose_common()  # 选择普攻
            self.choose_key = "q"
            self.choose_active = True  # 打开选中提示框

    def key_w(self):
        """按键W"""
        if self.choose_active and self.choose_key == "w":  # 选中提示框激活
            self.choose_active = False  # 关闭选中提示框
            self.next_turn_btn.command()  # 释放技能
        else:
            self.act_use_frame[self.now_act].choose_combat()  # 选择战技
            self.choose_key = "w"
            self.choose_active = True  # 打开选中提示框

    def key_e(self):
        """按键E"""
        if self.choose_active and self.choose_key == "e":  # 选中提示框激活
            self.choose_active = False  # 关闭选中提示框
            self.next_turn_btn.command()  # 释放技能
        else:
            self.act_use_frame[self.now_act].choose_ultimate()  # 选择大招
            self.choose_key = "e"
            self.choose_active = True  # 打开选中提示框

    def update_pos(self, camp):
        """更新坐标"""
        pos_dict = self.pos_dict[camp]
        self.skill_msg_txt.set_pos(pos_dict["skill_msg"])
        self.choose_now_txt.set_pos(pos_dict["choose_now"])
        self.next_turn_btn.set_pos(pos_dict["next_turn"])


class ChooseModule(tk.Frame):
    def __init__(self, ai_game, master, pos, act):
        """选择模块, 用于释放技能"""
        super().__init__(master)
        self.ai = ai_game
        self.master = master
        self.axle_game = self.ai.axle_game
        self.act = act
        self.pos = pos  # 传入的pos坐标是原坐标
        x, y = self.pos
        self.skill_name = ["普攻", "战技", "大招"]
        self.pos_dict = {"普攻": (x, y+50), "战技": (x, y+100), "大招": (x, y+150),
                         "玩家": (x, y+25), "name": (x, y)}  # 坐标
        # 按键
        self.common_but = None  # 普攻按钮
        self.combat_but = None  # 战技按钮
        self.Ultimate_but = None  # 大招按钮
        # 文本
        self.name_txt = None  # 显示角色名称的文本模块
        self.skill_msg_txt = self.ai.skill_msg_txt  # 显示技能效果的文本模块
        self.choose_now_txt = self.ai.choose_now_txt  # 选择提示文本模块
        self.choose_msg = ""  # 选中提示信息

    def init(self):
        """初始化选择模块"""
        self.init_text()
        self.init_but()

    def init_text(self):
        """初始化文本模块"""
        self.name_txt = TextModule(self.master, self.pos_dict["name"], f"角色：{self.act.name}")

    def init_but(self):
        self.common_but = ButtonModule(self.master, self.pos_dict["普攻"],
                                       f"普攻：{self.act.skills_name_fu2["普攻"]}", self.choose_common,
                                       wid_hei=[20, 1], justify="left")
        self.combat_but = ButtonModule(self.master, self.pos_dict["战技"],
                                       f"战技：{self.act.skills_name_fu2["战技"]}", self.choose_combat,
                                       wid_hei=[20, 1], justify="left")
        self.Ultimate_but = ButtonModule(self.master, self.pos_dict["大招"],
                                         f"大招：{self.act.skills_name_fu2["大招"]}", self.choose_ultimate,
                                         wid_hei=[20, 1], justify="left")

    def draw(self):
        """绘制选择模块"""
        self.name_txt.draw()
        self.common_but.draw()
        self.combat_but.draw()
        self.Ultimate_but.draw()

    def undraw(self):
        """隐藏选择模块"""
        self.name_txt.undraw()
        self.common_but.undraw()
        self.combat_but.undraw()
        self.Ultimate_but.undraw()

    def choose_common(self):
        """选择普攻"""
        self.choose_msg = f"{self.act.skills_name_fu2['普攻']}"  # 更改选中提示信息
        self.choose_now_txt.set_text(f"当前选中：{self.act.skills_name_fu2['普攻']}")  # 更改选中提示信息
        self.skill_msg_txt.set_text(f"{self.act.skills[self.act.skills_name_fu2['普攻']].description}")  # 显示技能效果
        self.ai.choose_key = "q"
        self.ai.choose_active = self.key_if("q")  # 关闭选中提示框

    def choose_combat(self):
        """选择战技"""
        self.choose_msg = f"{self.act.skills_name_fu2['战技']}"  # 更改选中提示信息
        self.choose_now_txt.set_text(f"当前选中：{self.act.skills_name_fu2['战技']}")  # 更改选中提示信息
        self.skill_msg_txt.set_text(f"{self.act.skills[self.act.skills_name_fu2['战技']].description}")  # 显示技能效果
        self.ai.choose_key = "w"
        self.ai.choose_active = self.key_if("w")  # 关闭选中提示框

    def choose_ultimate(self):
        """选择大招"""
        self.choose_msg = f"{self.act.skills_name_fu2['大招']}"  # 更改选中提示信息
        self.choose_now_txt.set_text(f"当前选中：{self.act.skills_name_fu2['大招']}")  # 更改选中提示信息
        self.skill_msg_txt.set_text(f"{self.act.skills[self.act.skills_name_fu2['大招']].description}")  # 显示技能效果
        self.ai.choose_key = "e"
        self.ai.choose_active = self.key_if("e")  # 关闭选中提示框

    def key_if(self, key):
        if key == self.ai.choose_key:
            return True
        else:
            return False



