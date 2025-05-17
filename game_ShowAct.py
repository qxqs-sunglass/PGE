from modules.module_text import TextModule
from modules.module_Progressbar import Progressbar
import tkinter as tk


class ShowAct(tk.Frame):
    def __init__(self, ai_game, master, actors, names, pos, me):
        """游戏展示角色信息模块
        注：一个模块对应一方角色信息
        me: 游戏一方的基础信息，包括：（血量，防御力，抗性，战技点数，助战点数，能量， buff）"""
        super().__init__(master)
        self.ai_game = ai_game
        self.master = master
        self.pos = pos  # 整个模块左上角坐标
        self.actors = actors  # 一方所有角色
        self.names = names  # 一方角色名称
        self.me = me  # 我方信息
        self.main_act = actors[names["主战"]]  # 主战角色
        self.main_act_txt = None  # 主战角色信息文本模块
        self.helper_acts = actors[names["助战"]]  # 助战角色
        self.helper_acts_txt = None  # 助战角色信息文本模
        self.attributes = me  # 我方信息字典
        self.blood_pro = None  # 我方血量
        self.df_txt = None   # 我方防御力
        self.sh_txt = None  # 防御值
        self.rt_txt = None  # 我方抗性文本模块  # 我方抗性
        self.skill_num_txt = None  # 我方战技点数文本模块 # 我方战技点数
        self.helper_num_txt = None  # 我方助战点数文本模块  # 我方助战点数
        self.energy_txt = None  # 我方能量文本模块
        self.buff_txt = None  # 我方buff文本模块
        self.poss = {"main_act_txt": (self.pos[0], self.pos[1]), "helper_acts_txt": (self.pos[0]+175, self.pos[1]),
                     "blood_pro": (self.pos[0], self.pos[1]+30),
                     "df_txt": (self.pos[0], self.pos[1]+50), "rt_txt": (self.pos[0]+125, self.pos[1]+50),
                     "sh_txt": (self.pos[0], self.pos[1]+75),
                     "skill_num_txt": (self.pos[0], self.pos[1]+100), "helper_num_txt": (self.pos[0]+150, self.pos[1]+100),
                     "energy_txt": (self.pos[0], self.pos[1]+125),
                     "buff_txt": (self.pos[0], self.pos[1]+150)}

    def init(self):
        """初始化游戏展示角色信息模块"""
        self.main_act_txt = TextModule(self.master, self.poss["main_act_txt"], self.main_act.name)
        self.helper_acts_txt = TextModule(self.master, self.poss["helper_acts_txt"], f"助战：{self.helper_acts.name}")
        self.blood_pro = Progressbar(self.master, self.poss["blood_pro"],
                                     text=f"血量{self.attributes['hp']}/{self.attributes['hp_max']}",
                                     orient="horizontal", length=200,
                                     maximum=self.attributes['hp_max'], value=self.attributes['hp'], background="red",
                                     thickness=5)
        self.df_txt = TextModule(self.master, self.poss["df_txt"], f"防御力：{self.attributes['df']}")
        self.sh_txt = TextModule(self.master, self.poss["sh_txt"], f"防御值：{self.attributes['sh']}")
        self.rt_txt = TextModule(self.master, self.poss["rt_txt"], f"抗性：{self.attributes['rt']}")
        self.skill_num_txt = TextModule(self.master, self.poss["skill_num_txt"],
                                        f"战技点数：{self.attributes['main_num']}")  # 我方战技点数
        self.helper_num_txt = TextModule(self.master, self.poss["helper_num_txt"],
                                         f"助战点数：{self.attributes['helper_num']}")  # 我方助战点数
        self.energy_txt = TextModule(self.master, self.poss["energy_txt"], f"能量：{self.attributes['energy']}")
        self.buff_txt = TextModule(self.master, self.poss["buff_txt"], f"buff：{self.attributes['buff']}",
                                   width=500, height=5)  # 我方buff文本模块

    def draw(self):
        """绘制游戏展示角色信息模块"""
        self.draw_act()

    def draw_act(self):
        """绘制战斗角色信息"""
        self.main_act_txt.draw()
        self.helper_acts_txt.draw()
        self.blood_pro.draw()
        self.df_txt.draw()
        self.sh_txt.draw()
        self.rt_txt.draw()
        self.skill_num_txt.draw()
        self.helper_num_txt.draw()
        self.energy_txt.draw()
        self.buff_txt.draw()

    def update(self):
        """更新游戏展示角色信息模块"""
        self.update_act()

    def update_act(self):
        """更新战斗角色信息"""
        self.blood_pro.update(self.attributes['hp'], text=f"血量{self.attributes['hp']}/{self.attributes['hp_max']}")
        self.df_txt.set_text(f"防御力：{self.attributes['df']}")
        self.sh_txt.set_text(f"防御值：{self.attributes['sh']}")
        self.rt_txt.set_text(f"抗性：{self.attributes['rt']}")
        self.skill_num_txt.set_text(f"战技点数：{self.attributes['main_num']}")
        self.helper_num_txt.set_text(f"助战点数：{self.attributes['helper_num']}")
        self.energy_txt.set_text(f"能量：{self.attributes['energy']}")
        self.buff_txt.set_text(self.update_buff_txt(self.attributes['buff']))  # 更新buff文本

    @staticmethod
    def update_buff_txt(buff):
        """更新buff文本"""
        if not buff:  # buff为空
            return "buff："
        temp = []
        for value in buff.values():  # 遍历buff字典
            # print(value)
            if not value["dis"]:
                continue  # 无需显示的buff
            temp.append(f"{value['name']}: ({value['turn']})      ")
        return 'buff：' + ''.join(temp)  # 合并buff字典
