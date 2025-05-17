from modules.module_text import TextModule
from modules.module_act import ActTemplate
from axle_act import AxleAct
from copy import deepcopy
import tkinter as tk
import random
import witelog


class GameAxle(tk.Frame):
    def __init__(self, ai_game, master):
        """游戏行动轴模块"""
        super().__init__(master)
        self.ai_game = ai_game
        self.master = master
        self.message_viewer = self.ai_game.message_viewer  # 信息显示器
        self.pos = (380, 0)  # 坐标
        # 动作轴
        self.action_axle = []  # 行动轴
        # action_axle = [角色名字, 角色名字]
        self.act_axle_dict = {0: TextModule(self.master, self.pos, "行动轴:")}  # 行动轴列表
        # action_axle_list = {0: [TextModule]:TextModule(root, pos, text), 1: [type]:TextModule(),...}
        # 绘制行动轴
        dy = 25  # 行动轴间距
        self.act_axle_dict_num = 30  # 行动轴数量
        for i in range(1, self.act_axle_dict_num + 1):
            x = self.pos[0]
            y = self.pos[1] + i * dy
            ap = TextModule(self.master, (x, y), f"{i}", justify="left")
            self.act_axle_dict[i] = ap
        # print(self.action_axle)
        self.doing_actions = []  # 正在进行的行动角色
        self.doing_now = ""   # 行动轴发生变动的角色
        # 获取角色信息
        self.actor_A = self.ai_game.actor_A  # 玩家A的角色（主战/助战）
        self.actor_B = self.ai_game.actor_B
        self.actor_A_name = self.ai_game.actor_A_name  # 玩家A的角色名字
        self.actor_B_name = self.ai_game.actor_B_name
        # 事件行动轴角色
        self.axle_act_temp = AxleAct()
        self.axle_act = self.axle_act_temp.axle_acts  # 事件行动轴角色字典
        self.event_dict = self.axle_act_temp.event_dict  # 事件字典
        self.axle_event_name = []  # 事件行动轴角色名字
        self.axle_event = {}  # 事件行动轴角色
        self.axle_event_num = 0  # 事件行动轴角色数量
        self.axle_event_init = 20  # 事件行动轴初始位置
        self.actors = {}

    def init(self):
        """初始化游戏行动轴"""
        self.init_role()  # 初始化角色
        self.move_action()  # 所有角色依据自身速度移动到指定行动轴
        self.update_action()  # 更新行动轴

    def init_role(self):
        """初始化角色"""
        # print(self.action_axle)
        for name in self.actor_A_name.values():
            self.actors[name] = self.actor_A[name]
            self.action_axle.append(name)  # 角色加入行动轴
        for name in self.actor_B_name.values():
            self.actors[name] = self.actor_B[name]
            self.action_axle.append(name)  # 角色加入行动轴

    def draw(self):
        """绘制游戏行动轴"""
        for ap in self.act_axle_dict.values():
            ap.draw()

    def undraw(self):
        """隐藏游戏行动轴"""
        for ap in self.act_axle_dict.values():
            ap.undraw()

    def move_action(self):
        while not self.doing_actions:
            for name in self.action_axle:
                if name in self.actors.keys():  # 获取角色信息
                    act = self.actors[name]
                elif name in self.axle_event_name:  # 获取事件行动轴角色信息
                    act = self.axle_event[name]
                # 确认速度合法
                sp = act.attributes['sp'] + act.axle_extra  # 角色速度
                if sp == 0:  # 角色无速度
                    sp = 1  # 角色速度为1
                    self.ai_game.message_viewer.add_message('角色速度为0，本次移动为1')  # 显示信息
                if sp > 10:
                    sp = 10  # 角色速度最大为10
                    self.ai_game.message_viewer.add_message('速度溢出，本次移动为10')  # 显示信息
                # 角色移动到下一个行动轴
                if act.axle - sp > 1:  # 只有大于等于1才移动
                    act.axle -= sp  # 角色移动到下一个行动轴
                elif act.axle - sp <= 1:  # 角色移动至1行动轴，并存储余下的行动值，同时加入doing_actions
                    yu = sp - act.axle
                    act.axle_yu = yu
                    act.axle = 1
                    if name in self.axle_event_name:  # 角色不是事件行动轴角色
                        # print(f"{name}行动轴1结束！")
                        self.ckeck_axle_event(name)  # 触发事件行动轴
                        continue
                    self.doing_actions.append(name)  # 角色加入doing_actions
        # print(f"行动轴1的角色顺序为{self.doing_actions}")
        # (self.action_axle)

        if len(self.doing_actions) >= 2 and self.ai_game.turn == 1:
            # 打乱行动轴1的角色顺序
            temp = random.sample(self.doing_actions, len(self.doing_actions))
            self.doing_actions = temp
            self.doing_now = self.doing_actions[0]  # 第一个角色开始行动
        else:
            self.doing_now = self.doing_actions[0]  # 第一个角色开始行动
        # print(f"行动轴1的角色顺序为{self.doing_actions}")

    def do_action(self, role_name):
        """角色行动"""
        act: ActTemplate
        if role_name in self.actors.keys():  # 获取角色信息
            act = self.actors[role_name]
        # 角色行动
        if act.extra_act:  # 角色有额外行动
            act.extra_act = False  # 更改标记
            self.begin_turn()  # 开始新的回合
            return
        self.doing_actions.remove(role_name)  # 从正在进行的行动角色中移除
        act.axle = act.axle_init
        # 角色回到14行动轴,axle_init是角色执行后回到行动轴时的初始值
        if act.axle_yu > 0:  # 角色有余下的行动值
            act.axle -= act.axle_yu  # 角色行动值减去余下的行动值
            act.axle_yu = 0  # 角色行动值归零
        self.begin_turn()  # 开始新的回合

    def begin_turn(self):
        """开始新的回合"""
        if self.doing_actions:  # 还有正在进行的行动角色
            self.doing_now = self.doing_actions[0]  # 第一个角色开始行动

    def ckeck_axle_event(self, name):
        """触发事件行动轴"""
        name = deepcopy(name)
        act = self.axle_event[name]
        if act.clear_axle:  # 是否删除
            self.ai_game.message_viewer.add_message(f"{name}触发了！")  # 显示信息
            self.axle_event[name].events["axle_event"](self.ai_game.legalMethod)  # 事件行动轴角色触发事件
            self.actors.pop(name)  # 事件行动轴角色从角色字典中移除
            self.axle_event_name.remove(name)  # 事件行动轴角色名字从列表中移除
            self.action_axle.remove(name)  # 角色从行动轴中移除
            self.axle_event_num -= 1  # 事件行动轴角色数量减1

    def update(self):
        """更新游戏行动轴"""
        if self.doing_actions:
            self.do_action(self.doing_now)
        if not self.doing_actions:
            self.move_action()  # 所有角色依据自身速度移动到指定行动轴
        # print(self.action_axle)
        self.update_action()  # 更新行动轴，系统全部处理完后才更新
        # print(self.doing_actions)

    def update_action(self):
        """更新行动轴
        先遍历行动轴上存有的角色，然后依据出入栈的次序，在act_axle_dict中更新角色的位置信息"""
        temp = {}
        for name in self.action_axle:
            act = self.actors[name]
            temp[name] = act.axle  # 角色位置信息加入temp字典
        # print(temp)
        # 检索，并重新排序temp字典
        temp2 = {}
        for name, axle_num in temp.items():
            if axle_num not in temp2.keys():
                temp2[axle_num] = [name]
            else:
                temp2[axle_num].append(name)
        # print(temp2)
        # 更新
        i = 1
        for ap_num in range(1, self.act_axle_dict_num + 1):
            if ap_num not in temp2.keys():  # 行动轴上无角色
                if ap_num > i:
                    self.act_axle_dict[ap_num].set_text(f"{ap_num}:")  # 清空行动轴文本
                continue
            if i <= ap_num:  # 行动轴上有空位，则将角色移动到空位
                i = ap_num
            while temp2[ap_num]:  # 角色不为空，则移动到空位
                name = temp2[ap_num].pop(0)
                txt = f"{i}: {name}({temp[name]})"  # 角色位置信息，格式为“行动轴:角色(位置)”
                self.act_axle_dict[i].set_text(txt)  # 更新角色位置信息
                i += 1
            i -= 1  # 行动轴上最后一个角色的位置信息不显示，所以i减1
        """for ap in self.act_axle_dict.values():
            print(ap.text)"""

    def add_axle(self, name, act_user):
        """在行动轴上添加角色"""
        temp = self.axle_act_temp.get_act(name, act_user)
        temp.init(self.master)
        temp.axle = self.axle_event_init  # 事件行动轴初始位置
        temp.events["init_event"](self.ai_game.legalMethod)
        witelog.writelog(f"{temp.name}被召唤到行动轴！")
        # 以下是事件行动轴角色的初始化
        self.action_axle.append(name)  # 角色加入行动轴
        self.axle_event[name] = temp  # 事件行动轴角色
        self.actors[name] = temp  # 事件行动轴角色加入角色字典
        self.axle_event_name.append(name)  # 事件行动轴角色名字
        self.axle_event_num += 1  # 事件行动轴角色数量
        # print(self.action_axle)
        self.update_action()  # 更新行动轴


