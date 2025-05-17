"""被动技能模块"""


class Passive:
    def __init__(self):
        self.skills = {
            "剑心": 剑心,
            "加班中": 加班中,
            "神明造物，为他之识": 神明造物为他之识,
            "群星拱，帝徐莅": 群星拱帝徐莅,
            "扬灰": 扬灰,
            "风雨听顺": 风雨听顺
        }  # 被动技能字典
        """"知其前瞻": 知其前瞻,
        "时滞之界": 时滞之界,
        "意识与混乱": 意识与混乱,
        "进化与希望": 进化与希望,
        "我愿，此行": 我愿此行,
        "寻神何处": 寻神何处,
        "我即虫灾": 我即虫灾,
        "战斗意识": 战斗意识,
        "回响空间": 回响空间"""


class 剑心:
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.name = "剑心"
        self.intro = "简介：\n依据自身速度，增加爆伤和攻击力。"
        self.description = "详细：\n每拥有1点速度+10爆伤，每拥有2点速度，+100攻击力"
        self.tag = "被动"

    def use(self, **kwargs):
        """使用技能"""
        temp = kwargs["temp"]
        var1 = round(self.user.attributes["sp"]*10)  # 计算爆伤
        a = round(self.user.attributes["sp"] / 2)  # 计算攻击力
        var2 = round(a * 100)
        self.user.charge_attribute(self.name, {"kd": var1, "at": var2})
        temp["msg"] = f"{self.user.name}触发被动。"


class 加班中:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "加班中"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（冷却两回合）。"  # 描述
        self.tag = "被动"  # 标签

    def use(self, *args, **kwargs):
        """使用技能"""
        # print(kwargs)
        temp = kwargs["temp"]
        if self.user.tick_passive > 0:  # 冷却时间未到，只有战技能触发额外回合
            self.user.tick_passive -= 1
            temp["extra_turn"] = f"被动剩余：{self.user.tick_passive}回合"
            return
        elif self.user.tick_passive <= 0 and temp["tag"][0] == "战技":
            self.user.tick_passive = self.user.tick_passive_turn
            self.user.extra_act = True  # 开启额外回合
            temp["extra_turn"] = "你进入了额外回合！"
            temp["msg"] = f"{self.user.name}触发被动。"


class 神明造物为他之识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，为他之识"  # 名称
        self.intro = "简介：护盾无上限，根据伤害值加护盾值，在第一个与自身回合开始前获得护盾。"  # 介绍
        self.description = "详细：护盾无上限，根据【共】攻击所造成的伤害获的等值的护盾值，在自身回合开始前获得基于自身防御力100%的护盾。"  # 描述
        self.tag = "被动"  # 标签

    def use(self, **kwargs):
        """使用技能"""
        passive_type = kwargs["passive_type"]
        our = kwargs["our"]
        temp = kwargs["temp"]
        if passive_type == "0012":  # 造成伤害后
            temp = kwargs["temp"]
            if "damage" in temp and temp["user"] == self.user.name:
                damage = temp["damage"]
                if damage > 0:
                    our["sh"] += damage
                    temp["msg"] = f"{self.user.name}:\n攻击{damage}点伤害，获得{damage}点护盾。"
                else:
                    temp["msg"] = "未触发伤害！"
            else:
                temp["msg"] = "未释放被动！"
        elif passive_type == "0041":  # 回合开始前
            our["sh"] = round(self.user.attributes['df'] * 1)
            temp["msg"] = (f"{self.user.name}触发被动:\n"
                           f"防御力{self.user.attributes['df']}，获得{round(self.user.attributes['df'] * 1)}点护盾。")


class 群星拱帝徐莅:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "群星拱，帝徐莅"  # 名称
        self.intro = "简介：减少血量时，增加自身基础暴击率。当血量低至0时，回复基于血量上限5%的血量，同时获得【还魂】。"  # 介绍
        self.description = ("详细：当自身血量减少时，每减少1000点血量，增加自身基础暴击率20%。"
                            "当自身血量低至0时，回复基于血量上限5%的血量，同时获得【还魂】。"
                            "【还魂】：基础攻击力+100， 抗性+1")  # 描述
        self.tag = "被动"  # 标签
        self.hp_reduce = 0  # 血量减少值, 用于存储上一次血量减少值

    def use(self, target, our, passive_type, temp):
        """使用技能"""
        temp["msgs"] = []
        if passive_type == "0022":  # 血量减少
            hp = our["hp_max"] - our['hp']  # 计算血量减少值
            self.hp_reduce = hp  # 存储血量减少值
            superposition = hp//1000
            if our["hp"] <= 0:  # 血量低至0
                our["hp"] = round(our["hp_max"] * 0.05)
                self.user.tick_tag_buff("【还魂】", target=target, our=our)
                temp["resurgence"] = "你已归来！"
                temp["msgs"].append(f"{self.user.name}触发被动，获得【还魂】。")
            if superposition > 0:  # 触发
                kr = round(20 * superposition)
                self.user.charge_attribute(self.name, {"kr": self.user.attributes_base['kr'] + kr})
            temp["msgs"].append(f"{self.user.name}触发被动，减少了{hp}点血量。")


class 扬灰:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "扬灰"  # 名称
        self.intro = "简介：\n当持有护盾，可对敌方一定比例的伤害。"  # 介绍
        self.description = "详细：\n当我方持有护盾时，根据对我方造成的伤害返回当前护盾值10%的伤害。"  # 描述
        self.tag = "被动"  # 标签

    def use(self, *args, **kwargs):
        """使用技能"""
        temp = kwargs["temp"]
        target = kwargs["target"]
        our = kwargs["our"]
        # print(our["sh"], temp["damage"])
        if our["sh"] > 0 and temp["damage"] > 0:  # 我方有护盾
            damage = round(our["sh"] * 0.1)
            target["hp"] -= damage
            temp["msgs"].append(f"{self.user.name}:\n护盾{our['sh']}点，对{target['name']}造成{damage}点伤害。")


class 知其前瞻:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "知其前瞻"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签


class 风雨听顺:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "风雨听顺"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签


class 时滞之界:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "时滞之界"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签


class 意识与混乱:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "意识与混乱"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签


class 进化与希望:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "进化与希望"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签


class 我愿此行:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "我愿，此行"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签


class 寻神何处:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "寻神何处"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签


class 我即虫灾:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "我即虫灾"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签


class 战斗意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "战斗意识"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签


class 回响空间:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "回响空间"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签


class 往返青祇:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "往返青祇"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签


class 清秋幽兰:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "清秋幽兰"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签


class 无处可逃:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "无处可逃"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签


class 独奏曲:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "独奏曲"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签


class 两极反转:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "两极反转"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签


class 来自天绝:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "来自天绝"  # 名称
        self.intro = "简介：\n进入额外回合"  # 介绍
        self.description = "详细：\n使用技能后，进入额外回合（一次/二回合）。"  # 描述
        self.tag = "被动"  # 标签






