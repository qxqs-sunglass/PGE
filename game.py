from MessageViewer import MessageViewer
from modules.module_text import TextModule
from modules.module_button import ButtonModule
from modules.module_act import ActTemplate
from copy import deepcopy
import tkinter as tk
import game_Axle
import game_ShowAct
import game_Control
import random
import tool
import witelog


"""触发类型:
001:
    0011: 造成伤害前
    0012: 造成伤害后
002：
    0021: 减血量前
    0022: 减血量后
    0023: 减防后
003:
    0031: 加防前
    0032: 加防后
004:
    0041: 回合开始
    0042: 回合结束
    0043: 游戏开始
    0044: 游戏结束
005:
    0051: 在角色使用技能前
    0052: 在角色使用技能后
006: 
    0061: 属性计算前
    0062: 属性计算后"""


class GameMain:
    def __init__(self, ai_game, master, acts, equips):
        """游戏主体"""
        self.ai_game = ai_game  # 传入main.py的【self】
        self.root = master  # 传入Tk()对象作为父窗口
        self.master = None  # 子窗口
        self.acts_base = acts  # 所有角色基础数据
        self.equip_base = equips  # 所有武器数据
        self.exit_event = None  # 关闭窗口时调用close()方法
        self.axle_game = None  # 实例化游戏行动轴
        self.control_game = None  # 实例化游戏控制面板
        # 总数据
        self.actor = {}  # 存储游戏双方的角色
        self.actor_name = {}  # 存储游戏双方的角色名称
        self.actor_name_fu = {}  # 存储游戏双方的角色名称
        self.equip = {}  # 存储游戏双方的武器
        self.equip_name = {}  # 存储游戏双方的武器名称
        # 玩家A
        self.actor_A = {}  # 玩家A的游戏角色
        self.actor_A_name = {}  # 玩家A:{"主战": , "助战": }用于存储玩家A的主战/助战角色名称
        self.show_a = None  # 玩家A的展示角色
        # 武器
        self.equip_A = {}  # 玩家A的游戏武器
        self.equip_A_name = {}  # 玩家A:{"主战": , "助战": }用于存储玩家A的主战/助战武器名称
        # 玩家B
        self.actor_B = {}  # 玩家B的游戏角色
        self.actor_B_name = {}  # 玩家B:{"主战": , "助战": }用于存储玩家B的主战/助战角色名称
        self.show_b = None  # 玩家B的展示角色
        # 武器
        self.equip_B = {}  # 玩家B的游戏武器
        self.equip_B_name = {}  # 玩家B:{"主战": , "助战": }用于存储玩家B的主战/助战武器名称
        # 玩家信息
        self.play_fu = ["df", "rt", "rh", "ha"]  # 需要检索的属性列表
        self.play_base = {"hp": 10000, "df": 0, "rt": 0, "rh": 0, "ha": 0,
                          "sh": 0, "camp": "A", "hp_max": 10000, "sh_max": 0,
                          "energy": 5, "main_num": 3, "helper_num": 3,
                          "main_num_max": 5, "helper_num_max": 5,
                          "energy_max": 25, "buff": {}, "other": 0,
                          "name": "", "re": 0}
        # "玩家": {"hp": 血量, "df": 防御力, "rt": 抗性, "rh": 减伤, ”ha“: 免伤,
        #         "sh": 护盾值, "camp": 阵营, "hp_max": 最大血量, "sh_max": 最大护盾值,
        #         "energy": 能量,"main_num": 技能使用次数, "helper_num": 助战技能使用次数,
        #         "main_num_max": 技能最大使用次数, "helper_num_max": 助战技能最大使用次数,
        #         "energy_max": 能量最大值, "buff": 效果字典, ""other": 额外乘区,
        #         "name": 角色名称, "re": 额外回能}
        self.play = None  # 玩家A/B的游戏角色
        self.play_imp = ["at", "kr", "kd", "dr",
                         "sp", "rt", "ids", "vl",
                         "name", "role", "re"]
        self.camp = "A"  # 当前玩家
        self.camp_fu = {"A": "B", "B": "A"}  # 相对互换的阵营
        self.turn = 1  # 当前回合数

        self.camp_to_global_lists = {
            "A": {
                "passive": [],
                "equip": []
            },  # [{"passive_type": [], "command": passive:class, "name": actor.name:str}]
            "B": {
                "passive": [],
                "equip": []
            }  # 列表中必有两个元素
        }   # 存储各阵营的全局被动技能/武器列表
        # 文本模块
        self.bin_text = None  # 复制版本号
        # 其他模块
        self.win = "A"  # 胜利文本
        self.win_txt = None  # 胜利
        self.win_loop = None
        self.win_but_close = None  # 关闭窗口按钮
        # 信息展示模块
        self.message_viewer = None  # 信息展示模块
        self.now_actor = None  # 当前展示角色名称
        self.events = {"damage": self.damage, "shield": self.shield,
                       "speed": self.speed, "df": self.df,
                       "Axle_act": self.axle_act}  # 事件
        # 按键绑定
        self.key_bind_control = {}  # 控制面板按键绑定
        self.key_active_control = False  # 按键是否被激活
        # 其他
        self.add_axle = None  # 增加角色
        self.world_AxleAct = {
            "now": [],
            "temp": []
        }  # 存储世界的行动轴数据
        self.world_use = {}  # 这里储存环境的use()方法
        self.legalMethod = {
            "add_axle": self.add_axle,
            "add_use": self.add_use,
            "sub_use": self.sub_use,
            "exchange_axle": self.exchange_axle,
            "helper_num_formulate_add": self.helper_num_add
        }

    def init(self):
        """初始化游戏
        注：游戏初始化时，应先初始化所有模块，调用run()方法运行游戏。"""
        self.init_var()  # 初始化变量
        self.init_master()  # 初始化游戏
        self.init_game()  # 初始化游戏
        self.init_sprite()  # 初始化实例
        self.init_draw()  # 初始化绘制
        self.init_other()  # 初始化其他模块

    def init_var(self):
        # 角色数据
        self.actor = {}  # 存储游戏双方的角色
        self.actor_name = {}
        self.actor_name_fu = {}  # 存储游戏双方的角色名称
        self.actor_A = {}  # 玩家A的游戏角色
        self.actor_A_name = {}  # 玩家A:{"主战": , "助战": }用于存储玩家A的主战/助战角色名称
        self.show_a = None  # 玩家A的展示角色
        self.actor_B = {}  # 玩家B的游戏角色
        self.actor_B_name = {}  # 玩家B:{"主战": , "助战": }用于存储玩家B的主战/助战角色名称
        # 额外
        self.world_use = {}  # 这里储存环境的use()方法
        self.world_AxleAct = {
            "now": [],
            "temp": []
        }  # 存储世界的行动轴数据

        self.camp_to_global_lists = {
            "A": {
                "passive": [],
                "equip": []
            },  # [{"passive_type": [], "command": passive:class, "name": actor.name:str}]
            "B": {
                "passive": [],
                "equip": []
            }  # 列表中必有两个元素
        }   # 存储各阵营的全局被动技能/武器列表

    def init_master(self):
        """初始化子窗口"""
        self.master = tk.Toplevel(self.root)  # 创建子窗口
        self.master.title("PGE")  # 设置子窗口标题
        self.master.geometry(self.ai_game.screen)  # 设置子窗口大小
        self.master.resizable(False, False)  # 设置子窗口不可缩放
        self.exit_event = self.master.protocol("WM_DELETE_WINDOW", self.close)  # 关闭窗口时调用close()方法
        self.master.bind("<Key>", self.key_press)  # 绑定按键

    def init_game(self):
        """初始化游戏"""
        # 初始化玩家A/B的游戏角色
        self.play = {"A": deepcopy(self.play_base.copy()), "B": deepcopy(self.play_base.copy())}
        self.play["A"]["camp"] = "A"  # 玩家A阵营
        self.play["A"]["name"] = "A"
        self.play["B"]["camp"] = "B"  # 玩家B阵营
        self.play["B"]["name"] = "B"
        # 读取角色数据
        act_data = self.ai_game.game_actor_temp
        equip_data = self.ai_game.game_equip_temp
        # 获取角色名称
        for name in ["主战", "助战"]:
            self.actor_A_name[name] = act_data["A"][name]  # 编入角色名称
            self.actor_name[name + "A"] = self.actor_A_name[name]  # 将角色编入总数据
            self.actor_name_fu[self.actor_A_name[name]] = name + "A"  # 角色名称与阵营对应
            equip_data[self.actor_A_name[name]] = equip_data[name + "A"]
        for name in ["主战", "助战"]:
            self.actor_B_name[name] = act_data["B"][name]  # 编入角色名称
            self.actor_name[name + "B"] = act_data["B"][name]  # 将角色编入总数据
            self.actor_name_fu[self.actor_B_name[name]] = name + "B"  # 角色名称与阵营对应
            equip_data[self.actor_B_name[name]] = equip_data[name + "B"]
        # 实例化角色
        for role_type, name in self.actor_A_name.items():
            actor = self.acts_base[name]  # 实例化角色
            actor.role_type = role_type  # 角色类型标
            actor.equip = self.equip_base[equip_data[name]]  # 武器
            actor.equip.user = actor  # 武器绑定角色
            actor.init_equip()  # 武器初始化
            actor.camp = "A"  # 阵营标记
            self.actor_A[name] = actor
            self.equip_A[actor.equip.name] = actor.equip  # 存储武器
            self.actor[name] = self.actor_A[name]  # 存储角色
            self.equip[actor.equip.name] = self.equip_A[actor.equip.name]  # 存储武器
        self.play["A"]["sh_max"] = round(self.actor_A[self.actor_A_name["主战"]].attributes["df"] * 5)  # 主战的护盾值
        for role_type, name in self.actor_B_name.items():
            actor = self.acts_base[name]  # 实例化角色
            actor.role_type = role_type  # 角色类型标
            actor.equip = self.equip_base[equip_data[name]]  # 武器
            actor.equip.user = actor  # 武器绑定角色
            actor.init_equip()  # 武器初始化
            actor.camp = "B"  # 阵营标记
            self.actor_B[name] = actor
            self.equip_B[actor.equip.name] = actor.equip  # 存储武器
            self.actor[name] = self.actor_B[name]  # 存储角色
            self.equip[actor.equip.name] = self.equip_B[actor.equip.name]  # 存储武器
        self.play["B"]["sh_max"] = round(self.actor_B[self.actor_B_name["主战"]].attributes["df"] * 5)  # 主战的护盾值
        # 角色信息
        for val in ["df", "rt", "rh", "ha", "energy_max"]:
            self.play["A"][val] = self.actor_A[self.actor_A_name["主战"]].attributes[val]  # 主战的属性
            self.play["B"][val] = self.actor_B[self.actor_B_name["主战"]].attributes[val]  # 主战的属性
        self.show_a = game_ShowAct.ShowAct(self, self.master, self.actor_A,
                                           self.actor_A_name, (0, 0), self.play["A"])
        self.show_a.init()
        self.show_b = game_ShowAct.ShowAct(self, self.master, self.actor_B,
                                           self.actor_B_name, (600, 0), self.play["B"])
        self.show_b.init()

    def init_sprite(self):
        """初始化实例"""
        self.axle_game = game_Axle.GameAxle(self, self.master)
        self.control_game = game_Control.GameControl(self, self.master)
        self.axle_game.init()
        self.control_game.init()
        self.bin_text = self.ai_game.bin_text.copy(self.master)  # 复制版本号
        self.message_viewer = MessageViewer(self.master, (350, 525), (300, 200))
        self.message_viewer.add_message("此窗口为消息窗口。")
        self.key_bind_control = self.control_game.key_bind_dict  # 按键绑定

    def init_other(self):
        """初始化其他模块"""
        # 角色被动技能/装备初始化
        for actor in self.actor.values():  # 记录被动&武器是否为全局被动,在不属于自身回合也可执行
            self.process_global_effects(actor)

        for actor in self.actor.values():
            temp = {
                "turn": self.turn,
                "user": actor.name,
                "tag": ["缓存..."],
                "role_type": actor.role_type,
                "msgs": []
            }
            self.use_tick(target=self.play[self.camp_fu[actor.camp]],
                          our=self.play[actor.camp],
                          tick_type="0043", temp=temp,
                          actor=actor)

        self.key_active_control = True  # 按键激活
        self.message_viewer.add_message("--------------------------------", "warning")
        self.message_viewer.add_message(f"回合{self.axle_game.doing_now}开始！", "warning")
        self.now_actor = self.axle_game.doing_now  # 当前展示角色名称
        self.camp = self.actor[self.now_actor].camp  # 切换阵营
        self.turn = 1  # 回合数初始化
        self.play_import(self.now_actor)  # 导入角色数据
        # 大世界buff
        self.add_axle = self.axle_game.add_axle  # 增加角色
        self.world_AxleAct["now"] = list(self.axle_game.event_dict.keys())  # 存储世界的行动轴数据
        name = self.world_AxleAct["now"].pop(0)
        self.world_AxleAct["temp"].append(name)
        self.add_axle(name, self)
        # print(self.world_use)
        # print(self.world_AxleAct)
        actor = self.actor[self.now_actor]  # 当前行动角色实例
        temp = {
            "turn": self.turn,
            "user": actor.name,
            "tag": ["缓存..."],
            "role_type": actor.role_type,
            "msgs": [],
            "damage": 0
        }
        self.use_tick(target=self.play[self.camp_fu[actor.camp]],
                      our=self.play[actor.camp],
                      tick_type="0041", temp=temp,
                      actor=actor)

    def process_global_effects(self, actor):
        """
        处理角色的全局被动技能和装备
        :param actor: 角色对象
        """
        camp = actor.camp
        if camp not in self.camp_to_global_lists:
            return  # 如果阵营不符合预期，直接跳过

        # 获取当前阵营对应的全局列表
        passive_global_A = self.camp_to_global_lists[camp]["passive"]
        passive_global_B = self.camp_to_global_lists[self.camp_fu[camp]]["passive"]
        equip_global_A = self.camp_to_global_lists[camp]["equip"]
        equip_global_B = self.camp_to_global_lists[self.camp_fu[camp]]["equip"]
        # 利用字典特性，依靠阵营标记，将全局被动技能/装备添加到对应列表中

        # 处理被动技能
        if actor.passive_global[0]:  # 当第一个位置为True时，表示该角色加入我方阵营的全局被动技能
            passive_global_A.append({
                "passive_type": actor.passive_type,
                "name": actor.name,
                "command": actor.use_passive,
                "camp": actor.camp
            })

        if actor.passive_global[1]:  # 当第二个位置为True时，表示该角色加入对方阵营的全局被动技能
            passive_global_B.append({
                "passive_type": actor.passive_type,
                "name": actor.name,
                "command": actor.use_passive,
                "camp": actor.camp
            })

        # 处理装备
        if actor.equip_global[0]:  # 当第一个位置为True时，表示该角色加入我方阵营的全局装备
            equip_global_A.append({
                "equip_type": actor.equip_type,
                "name": actor.name,
                "command": actor.use_equip,
                "camp": actor.camp
            })

        if actor.equip_global[1]:  # 当第二个位置为True时，表示该角色加入对方阵营的全局装备
            equip_global_B.append({
                "equip_type": actor.equip_type,
                "name": actor.name,
                "command": actor.use_equip,
                "camp": actor.camp
            })

    def init_draw(self):
        """初始化绘制"""
        self.draw()  # 绘制游戏界面

    def draw(self):
        """绘制游戏界面"""
        self.draw_other()  # 绘制其他模块
        self.draw_text()  # 绘制文本模块

    def draw_text(self):
        """绘制文本模块"""
        self.bin_text.draw()

    def draw_other(self):
        """绘制其他模块"""
        self.axle_game.draw()
        self.control_game.draw()
        self.show_a.draw()
        self.show_b.draw()
        self.message_viewer.draw()

    def run(self):
        """运行游戏"""
        self.init()  # 初始化游戏

    def open(self):
        """打开游戏"""
        self.run()  # 运行游戏

    def close(self):
        """关闭游戏"""
        self.ai_game.open()
        self.master.destroy()  # 销毁子窗口

    def undraw(self):
        """隐藏游戏界面"""
        self.master.withdraw()  # 隐藏子窗口
        self.axle_game.undraw()
        self.control_game.undraw()
        self.show_a.undraw()
        self.show_b.undraw()

    def key_press(self, event):
        """按键绑定"""
        if event.char in self.key_bind_control.keys():
            self.key_bind_control[event.char]()

    def update_play_show(self, temp: dict):
        """更新玩家属性"""
        if temp is None:
            temp = {"000": "缓存..."}  # 若无则为无效字典
        if "msg" in temp:
            self.message_viewer.add_message(temp["msg"], "use")
            witelog.writelog(temp["msg"])
            temp.pop("msg")
        if "msgs" in temp:
            for msg in temp["msgs"]:
                self.message_viewer.add_message(msg, "use")
                witelog.writelog(msg)
            temp["msgs"] = []  # 清空消息列表
        self.show_a.update()
        self.show_b.update()

    def use_tick(self, target, our, temp, actor, tick_type):
        """事件触发：被动和武器触发"""
        if tick_type in self.world_use.keys():
            # print(self.world_use)
            for event in self.world_use[tick_type]:
                event(target=target, our=our, temp=temp, actor=actor)  # 触发世界事件
            self.update_play_show(temp)
        # 当前角色被动
        if tick_type in actor.passive_type:
            actor.use_passive(target=target, our=our, passive_type=tick_type, temp=temp)
            self.update_play_show(temp)
        # 触发装备
        if tick_type in actor.equip_type:
            actor.use_equip(target=target, our=our, equip_type=tick_type, temp=temp)
            self.update_play_show(temp)
        # 触发全局被动/武器
        camp = actor.camp
        passive_global = self.camp_to_global_lists[camp]["passive"]
        equip_global = self.camp_to_global_lists[camp]["equip"]
        for passive in passive_global:
            if tick_type in passive["passive_type"] and passive["name"] != actor.name:
                if actor.camp == passive["camp"]:
                    passive["command"](target=target, our=our, passive_type=tick_type, temp=temp)
                else:
                    passive["command"](target=our, our=target, passive_type=tick_type, temp=temp)
                self.update_play_show(temp)
        for equip in equip_global:
            if tick_type in equip["equip_type"] and equip["name"] != actor.name:
                if actor.camp == equip["camp"]:
                    equip["command"](target=target, our=our, equip_type=tick_type, temp=temp)
                else:
                    equip["command"](target=our, our=target, equip_type=tick_type, temp=temp)
                self.update_play_show(temp)

    def next_turn(self):
        """更新游戏行动轴"""
        if self.control_game.act_use_frame[self.control_game.now_act].choose_msg == "":  # 未选择行动
            self.message_viewer.add_message("请选择技能！")
            return  # 未选择行动
        actor = self.actor[self.now_actor]  # 当前行动角色实例
        self.message_viewer.add_message("----------")
        camp = self.camp_fu[self.camp]  # 获取目标阵营
        play_target = self.play[camp]  # 目标玩家的属性
        play_our = self.play[self.camp]  # 自己的属性
        temp = {
            "turn": self.turn,
            "user": actor.name,
            "tag": ["缓存..."],
            "role_type": actor.role_type,
            "msgs": [],
            "damage": 0
        }

        # 0051 类型被动  技能开始时触发
        self.use_tick(target=play_target, our=play_our, temp=temp, actor=actor, tick_type="0051")
        # 使用技能
        self.control_game.use_skill(target=play_target, our=play_our, temp=temp, actor=actor)
        # 0052 类型被动  技能结束时触发
        self.use_tick(target=play_target, our=play_our, temp=temp, actor=actor, tick_type="0052")
        if "error" in temp:
            self.message_viewer.add_message(temp["error"])
            return  # 技能使用失败

        if temp["tag"][0] == "大招":
            temp["extra_turn"] = "释放大招"
            actor.extra_act = True  # 额外回合标记

        temp_fu = deepcopy(temp)  # 副本
        for event in temp_fu:
            if event in self.events.keys():
                self.events[event](temp, camp, target=play_target, our=play_our, actor=actor)  # 触发事件
            self.update_play_show(temp)
        # 0042 类型被动  回合结束时触发
        self.use_tick(target=play_target, our=play_our, temp=temp, actor=actor, tick_type="0042")

        # 以下是回合结算
        if self.control_game.now_act in self.actor_name.keys():
            self.axle_game.doing_now = self.actor_name[self.control_game.now_act]
        # print(self.camp)
        self.turn += 1
        self.axle_game.update()  # 更新行动轴
        self.control_game.update_turn()  # 更新回合数
        self.now_actor = self.axle_game.doing_now  # 更新当前展示角色名称
        temp["turn"] = self.turn  # 记录回合数

        # 在回合开始时使用
        if self.win_check():  # 判断游戏是否结束
            return  # 结束游戏
        self.key_active_control = False  # 按键不激活
        play_our["re"] = 0  # 额外回能清零
        play_target["re"] = 0  # 额外回能清零
        # 以下是回合开始
        self.message_viewer.add_message("--------------------------------", "warning")
        self.message_viewer.add_message(f"回合{self.now_actor}开始！", "warning")
        witelog.writelog(f"回合{self.now_actor}开始！---------------------------")
        self.camp = self.actor[self.now_actor].camp  # 切换阵营
        self.control_game.update_pos(self.camp)  # 更新位置
        self.play_import(self.now_actor)  # 导入角色属性
        play_target = self.play[camp]  # 目标玩家的属性
        play_our = self.play[self.camp]  # 自己的属性
        actor = self.actor[self.now_actor]  # 当前行动角色实例
        # print(self.world_AxleAct["now"])
        if len(self.world_AxleAct["now"]) == 0:  # 行动轴为空
            self.world_AxleAct["now"] = random.sample(self.world_AxleAct["temp"].copy(), len(self.world_AxleAct["temp"]))  # 重置行动轴
            self.world_AxleAct["temp"] = []  # 清空临时行动轴
        # 0041 类型被动  回合开始时触发
        self.use_tick(target=play_target, our=play_our,
                      temp=temp, actor=actor, tick_type="0041")

    def play_import(self, act_name):
        act: ActTemplate = self.actor[act_name]  # 角色
        camp = act.camp  # 阵营
        camp_fu = self.camp_fu[camp]  # 相对阵营
        act_fu: ActTemplate = self.actor[self.actor_name[f"主战{camp_fu}"]]  # 相对角色
        for val in self.play_imp:  # 导入角色属性
            if val in act.attributes.keys():  # 角色有属性
                self.play[camp][val] = deepcopy(act.attributes[val])  # 导入属性

            if val in act_fu.attributes.keys():  # 角色有相对阵营的属性
                self.play[camp_fu][val] = deepcopy(act_fu.attributes[val])  # 导入相对阵营的属性
        witelog.writelog(f"当前{camp}的属性：{self.play[camp]}")
        witelog.writelog(f"当前{camp_fu}的属性：{self.play[camp_fu]}")

    def damage(self, temp, camp, target, our, actor):
        """造成伤害"""
        # 在造成伤害前使用
        self.use_tick(target=target, our=our, temp=temp, actor=actor, tick_type="0011")
        # 造成伤害
        self.work_out_damage(temp, camp, target, our, actor)
        # 在造成伤害后使用
        self.use_tick(target=target, our=our, temp=temp, actor=actor, tick_type="0012")

    def speed(self, temp, camp, target, our, actor):
        """加速"""
        self.message_viewer.add_message(f"{our['name']}的角色加速了{temp['speed']}", "tick")

    def axle_act(self, temp, camp, target, our, actor):
        """行动轴出现角色"""
        self.axle_game.add_axle(temp["Axle_act"], actor)
        self.message_viewer.add_message(f"行动轴上出现了{temp['Axle_act']}，行动轴回应了{our['name']}！", "tick")

    def shield(self, temp, camp, target, our, actor):
        """护盾值"""
        # 在加护盾前使用
        self.use_tick(target=target, our=our, temp=temp, actor=actor, tick_type="0031")

        self.play[self.camp]["sh"] += temp["shield"]
        self.message_viewer.add_message(f"{our['name']}的护盾值增加了{temp['shield']}", "tick")

        # 在加护盾后使用
        self.use_tick(target=target, our=our, temp=temp, actor=actor, tick_type="0032")

    def work_out_damage(self, temp, camp, target, our, actor):
        """计算伤害"""
        damage = temp["damage"]
        # 在受伤前使用
        self.use_tick(target=target, our=our, temp=temp, actor=actor, tick_type="0021")

        self.message_viewer.add_message(f"{our['name']}: 造成了{damage}点伤害！", "tick")
        if self.play[camp]["sh"] - damage <= 0:
            self.play[camp]["sh"] = 0
            damage_yu = damage - self.play[camp]["sh"]
            if damage_yu > 0:
                self.play[camp]["hp"] -= damage_yu
        else:
            self.play[camp]["sh"] -= damage
        if self.play[camp]["energy"] + 2 + target["re"] < 25:  # 受击回能
            self.play[camp]["energy"] += 2 + target["re"]
        elif self.play[camp]["energy"] + 2 + target["re"] >= 25:
            self.play[camp]["energy"] = 25  # 回能上限

        # 在减伤后使用
        self.use_tick(target=target, our=our, temp=temp, actor=actor, tick_type="0022")

    def add_use(self, may):
        """此处需要传入实例
        添加触发事件"""
        for e_type in may.event_type:
            if e_type not in self.world_use.keys():  # 类型不存在则添加
                self.world_use[e_type] = [may.use]
            else:
                self.world_use[e_type].append(may.use)
        # print(self.world_use)

    def sub_use(self, may):
        """此处需要传入实例
        删除触发事件"""
        for e_type in may.event_type:
            if e_type in self.world_use.keys():  # 类型存在则删除
                self.world_use[e_type].remove(may.use)
        # print(self.world_use)

    def exchange_axle(self):
        """交换事件"""
        self.add_axle(self.world_AxleAct["now"][0], self)
        self.world_AxleAct["temp"].append(self.world_AxleAct["now"][0])
        self.world_AxleAct["now"].pop(0)

    def helper_num_add(self):
        """助战点+1"""
        tool.helper_num_formulate_add(self.play["A"], 2)
        tool.helper_num_formulate_add(self.play["B"], 2)

    def win_init(self):
        """初始化胜利/失败"""
        self.master.withdraw()  # 隐藏子窗口
        self.win_loop = tk.Toplevel(self.master)  # 创建胜利/失败框
        self.win_loop.title("胜利")  # 设置标题
        self.win_loop.geometry("400x200")  # 设置大小
        self.win_loop.resizable(False, False)  # 设置不可缩放
        self.win_loop.protocol("WM_DELETE_WINDOW", self.win_close)  # 关闭窗口时调用win_close()方法
        self.win_loop.grab_set()  # 锁定窗口
        self.win_txt = TextModule(self.win_loop, (120, 20), f"玩家{self.win}胜利！")
        self.win_but_close = ButtonModule(self.win_loop, (120, 60), text="关闭", command=self.win_close)
        self.win_txt.draw()
        self.win_but_close.draw()

    def win_check(self):
        """判断游戏是否结束"""
        if self.play["A"]["hp"] <= 0:
            self.win = "B"
            self.win_init()
            return True
        elif self.play["B"]["hp"] <= 0:
            self.win = "A"
            self.win_init()
            return True
        else:
            return False

    def win_close(self):
        """关闭胜利/失败框"""
        self.close()  # 关闭游戏
        self.win_loop.destroy()  # 销毁窗口


