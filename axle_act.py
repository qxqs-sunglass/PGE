import tool
from modules.module_axle_act import AxleActTemplate, WorldAxleTemplate


class AxleAct:
    def __init__(self):
        """行动轴角色总编
        对于角色直接传入角色个体的实例，
        对于大世界环境buff，便是传入legalMethod合法方法。"""
        self.axle_acts = {
            "【黯然】": 黯然
        }  # 召唤物字典
        self.event_dict = {
            "大日圣典": 大日圣典,
            "红月世界": 红月世界,
        }  # 事件字典

    def get_act(self, name, user):
        """获取行动轴角色"""
        if name in self.axle_acts:
            return self.axle_acts[name](name, user)
        elif name in self.event_dict:
            return self.event_dict[name](name, user)
        else:
            return None


class 黯然(AxleActTemplate):
    def __init__(self, name, user):
        super().__init__()
        self.name = name
        self.user = user
        self.clear_axle = True  # 从行动轴移除

    def do_event(self, ai):
        """执行事件"""
        self.user.charge_attribute(self.user.state, remove=True)
        self.user.state = "凡"


class 大日圣典(WorldAxleTemplate):
    def __init__(self, name, user):
        super().__init__()
        self.name = name
        self.user = user
        # 如果时事件这里便是self。 如果是召唤物，则存储的角色信息
        self.clear_axle = True  # 抵达回合时是否移除
        self.event_type = ["0041"]  # 触发事件类型
        self.description = ("【星】类角色，速度+1\n"
                            "主战角色行动时回复1点能量\n"
                            "助战角色行动时额外1点战技点。")  # 事件/召唤物描述

    def use(self, **kwargs):
        """特效"""
        our = kwargs["our"]
        temp = kwargs["temp"]
        if "extra_turn" in temp:
            return  # 额外回合不触发
        # 回复1点能量
        tool.energy_formulate_add(our, 1)
        tool.main_num_formulate_add(our, 1)
        temp["msgs"].append(f"{self.name}触发，回复1点能量,增加1点技能点。")


class 红月世界(WorldAxleTemplate):
    def __init__(self, name, user):
        super().__init__()
        self.name = name
        self.user = user
        # 如果时事件这里便是self。 如果是召唤物，则存储的角色信息
        self.clear_axle = True  # 抵达回合时是否移除
        self.event_type = ["0052"]  # 触发事件类型
        self.description = ("【天】类角色速度+1；"
                            "所有在场角色每次攻击附加100伤害。")  # 事件/召唤物描述

    def use(self, **kwargs):
        """特效"""
        temp = kwargs["temp"]
        # 附加100伤害
        temp["damage"] += 100
        temp["msgs"].append(f"{self.name}触发，增加100点伤害。")


class 旧日复苏(WorldAxleTemplate):
    def __init__(self, name, user):
        super().__init__()
        self.name = name
        self.user = user
        # 如果时事件这里便是self。 如果是召唤物，则存储的角色信息
        self.clear_axle = True  # 抵达回合时是否移除
        self.event_type = []  # 触发事件类型
        self.description = ("【天】类【星】类角色速度+1；"
                            "场上每有1己方召唤物，己方角色+100攻击。")  # 事件/召唤物描述


class 外邪之祸(WorldAxleTemplate):
    def __init__(self, name, user):
        super().__init__()
        self.name = name
        self.user = user
        # 如果时事件这里便是self。 如果是召唤物，则存储的角色信息
        self.clear_axle = True  # 抵达回合时是否移除
        self.event_type = []  # 触发事件类型
        self.description = ("【天】类角色速度+1；"
                            "每消耗1战技点，使本次伤害增伤50%。")  # 事件/召唤物描述


class 流月朁位(WorldAxleTemplate):
    def __init__(self, name, user):
        super().__init__()
        self.name = name
        self.user = user
        # 如果时事件这里便是self。 如果是召唤物，则存储的角色信息
        self.clear_axle = True  # 抵达回合时是否移除
        self.event_type = []  # 触发事件类型
        self.description = ("【冥】类角色速度+1；"
                            "施放战技时，扣除5%己方当前生命和5%敌方当前生命，使本次战技额外+100%攻击力的倍率。")  # 事件/召唤物描述


class 灰雾侵袭(WorldAxleTemplate):
    def __init__(self, name, user):
        super().__init__()
        self.name = name
        self.user = user
        # 如果时事件这里便是self。 如果是召唤物，则存储的角色信息
        self.clear_axle = True  # 抵达回合时是否移除
        self.event_type = []  # 触发事件类型
        self.description = "【冥】类角色速度+1\行动轴不可见\行动轴上随机出现3个“雾霾”\每行动3次或与“雾霾”同阶，+1“异化”：+40%增伤，+5%概率攻击自身。"  # 事件/召唤物描述


class 世界原型(WorldAxleTemplate):
    def __init__(self, name, user):
        super().__init__()
        self.name = name
        self.user = user
        # 如果时事件这里便是self。 如果是召唤物，则存储的角色信息
        self.clear_axle = True  # 抵达回合时是否移除
        self.event_type = []  # 触发事件类型
        self.description = ("全角色速度-1；动轴+6阶；角色以至多5阶，"
                            "至少1阶的速度行动；每角色每回合至多造成1000伤害，"
                            "本轮至多造成5000伤害。")  # 事件/召唤物描述


class 西退(WorldAxleTemplate):
    def __init__(self, name, user):
        super().__init__()
        self.name = name
        self.user = user
        # 如果时事件这里便是self。 如果是召唤物，则存储的角色信息
        self.clear_axle = True  # 抵达回合时是否移除
        self.event_type = []  # 触发事件类型
        self.description = "【冥】类【星】类速度+1\获得护盾量+50%\行动轴出现“徙民”，“徙民”具有3速度，“徙民”行动时，双方+100%防御力的护盾。使用战技使“徙民”+1速（一回合）。"  # 事件/召唤物描述


class 逐雾之日(WorldAxleTemplate):
    def __init__(self, name, user):
        super().__init__()
        self.name = name
        self.user = user
        # 如果时事件这里便是self。 如果是召唤物，则存储的角色信息
        self.clear_axle = True  # 抵达回合时是否移除
        self.event_type = []  # 触发事件类型
        self.description = "【天】类【星】类角色速度+1\一角色造成8次伤害后立即行动，并使其进入“耀斑”：追加攻击无视敌方2抗（一回合）。"  # 事件/召唤物描述


class 腥红日食(AxleActTemplate):
    def __init__(self, name, user):
        super().__init__()
        self.name = name
        self.user = user
        # 如果时事件这里便是self。 如果是召唤物，则存储的角色信息
        self.clear_axle = True  # 抵达回合时是否移除
        self.event_type = []  # 触发事件类型
        self.description = "【冥】类角色速度+1\行动轴上随机出现“日光”。每次行动+1“月光”：每回合受到200伤害（dot）。角色与“日光”同阶，净化所有“月光”。"  # 事件/召唤物描述


class 使者告言(AxleActTemplate):
    def __init__(self, name, user):
        super().__init__()
        self.name = name
        self.user = user
        # 如果时事件这里便是self。 如果是召唤物，则存储的角色信息
        self.clear_axle = True  # 抵达回合时是否移除
        self.event_type = []  # 触发事件类型
        self.description = "【星】类角色速度+1\行动轴上出现“使者”，使用战技或大招使“使者”行动轴+1阶，一方使“使者”行动，则另一方扣除10%当前生命值。"  # 事件/召唤物描述


class 神佑之地(AxleActTemplate):
    def __init__(self, name, user):
        super().__init__()
        self.name = name
        self.user = user
        # 如果时事件这里便是self。 如果是召唤物，则存储的角色信息
        self.clear_axle = True  # 抵达回合时是否移除
        self.event_type = []  # 触发事件类型
        self.description = "【天】类【星】类角色速度+1\行动轴上出现“神佑”，“神佑”以随机2、3速度行动。“神佑”与角色同阶时，该角色获得“眷顾”：攻击力+100，防御力+100，速度+1，抗性+1（两回合）。"  # 事件/召唤物描述


class 升格计划(AxleActTemplate):
    def __init__(self, name, user):
        super().__init__()
        self.name = name
        self.user = user
        # 如果时事件这里便是self。 如果是召唤物，则存储的角色信息
        self.clear_axle = True  # 抵达回合时是否移除
        self.event_type = []  # 触发事件类型
        self.description = "【冥】类角色速+1\每消耗1战技点，使本轮己方的追加攻击和召唤物各增伤20%，直至追加攻击和召唤物触发\本轮最后一次伤害将额外带100%暴率，200%暴伤。"  # 事件/召唤物描述

    def do_event(self):
        """执行事件"""
        pass
