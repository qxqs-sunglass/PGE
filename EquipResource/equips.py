from copy import deepcopy
from modules.module_equips import EquipTemplate
"""装备的类型与被动所使用的触发器是共用的
装备类型:
001:
    0011: 计算伤害前
    0012: 计算伤害后
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
005:
    0051: 在角色使用技能前
    0052: 在角色使用技能后"""


class Equips:
    def __init__(self):
        self.equips_dict = {
            "于人之法": 于人之法,
            "至死方休": 至死方休,
            "樱弥散": 樱弥散,
            "测试用": 测试用
        }  # 映射表


class 于人之法(EquipTemplate):
    def __init__(self, path):
        super().__init__()
        self.attr_use = ["at", "sp"]  # 需要的属性
        self.path = path  # 装备图片路径
        self.equip_type = ["0052"]  # 装备类型
        self.equip_global = [False, False]  # 是否全局使用
        self.buff_tag = {"【攻击力】": "our", "【增伤】": "our"}  # 标签buff
        self.buff_value = {"【攻击力】": {"num": 100, "turn": 2, "extra_turn": 1},
                           "【增伤】": {"num": 40, "turn": 1, "extra_turn": 1}}  # 标签buff值

    def use(self, **kwargs):
        temp = kwargs["temp"]
        if temp["tag"][0] != "战技":
            return {"error": "装备类型错误"}
        target = kwargs["target"]
        our = kwargs["our"]
        value = deepcopy(self.buff_value["【攻击力】"])
        value["owner"] = temp["user"]
        self.user.tick_tag_buff("【攻击力】", target=target, our=our,  value=value)   # 加入标签buff
        if "extra_turn" in temp:
            value = deepcopy(self.buff_value["【增伤】"])
            value["owner"] = temp["user"]
            self.user.tick_tag_buff("【增伤】", target=target, our=our, value=value)
            temp["msgs"].append(f"获得了{self.name}的增伤效果")
        temp["msgs"].append(f"{self.name}发动了")


class 至死方休(EquipTemplate):
    def __init__(self, path):
        super().__init__()
        self.attr_use = ["kr", "kd"]  # 需要的属性
        self.path = path  # 装备图片路径
        self.equip_type = ["0051"]  # 装备类型
        self.equip_global = [False, False]  # 是否全局使用

    def use(self, **kwargs):
        temp = kwargs["temp"]
        temp["msg"] = f"{self.name}发动了"


class 樱弥散(EquipTemplate):
    def __init__(self, path):
        super().__init__()
        self.attr_use = ["re", "sp"]  # 需要的属性
        self.path = path  # 装备图片路径
        self.equip_type = ["0041"]  # 装备类型
        self.equip_global = [False, False]  # 是否全局使用

    def use(self, **kwargs):
        temp = kwargs["temp"]
        target = kwargs["target"]
        our = kwargs["our"]

        temp["msgs"].append(f"当前速度{self.user.attributes['sp']}")
        if self.user.attributes["sp"] > 4:
            a = self.user.attributes["sp"] - 4
            value = deepcopy(self.buff_value.get("【暴击率】"))
            value["owner"] = temp["user"]
            value["num"] = 20*a
            self.user.tick_tag_buff("【暴击率】", target=target, our=our, value=value)  # 加入标签buff
            temp["msgs"].append(f"获得了{self.name}的暴击率效果，{20*a}点")
            value = deepcopy(self.buff_value.get("【暴击伤害】"))
            value["owner"] = temp["user"]
            if 20*a > 100:  # 防止暴击伤害大于100
                value["num"] = 100
            else:
                value["num"] = 20*a
            self.user.tick_tag_buff("【暴击伤害】", target=target, our=our, value=value)  # 加入标签buff
            temp["msgs"].append(f"获得了{self.name}的暴击伤害效果，{20*a}点")
        temp["msgs"].append(f"{self.name}发动了")


class 测试用(EquipTemplate):
    def __init__(self):
        super().__init__()
        self.name = "测试用"
        self.name_base = "测试用武器"
        self.description = "这是一个测试用武器"
        self.attr_use = ["at", "kr"]  # 需要的属性
        self.attributes_base = {"at": 200, "kr": 70}
        self.attributes = self.attributes_base.copy()
        self.equip_type = ["0012"]  # 装备类型
        self.equip_global = [False, False]  # 是否全局使用

    def use(self, **kwargs):
        target = kwargs["target"]
        target["hp"] -= self.attributes["at"]
        temp = kwargs["temp"]
        temp["msg"] = f"{self.name}对{target['name']}造成了{self.attributes['at']}点伤害"






