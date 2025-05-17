from modules.module_skill import SkillModule
import tool
"""大招技能模块
大招类技能，必要时要改成英文字符"""


class Ultimate:
    def __init__(self):
        self.skills = {
            "黎明前的血色": 黎明前的血色,
            "百雀难回巢": 百雀难回巢,
            "三十三，星神临": 三十三星神临,
            "文明尽头": CivilizationEnd,
            "守护": 守护,
            "生命以求顺": 生命以求顺
        }  # 大招技能映射表
        """
            "全视未来": 全视未来,
            "超越时空的一刀": 超越时空的一刀,
            "红月初升，其道异者": 红月初升其道异者,
            "辉煌天": 辉煌天,
            "愿行与人前": 愿行与人前,
            "见神": 见神,
            "蛊祸": 蛊祸,
            "梦渊之魂": 梦渊之魂,
            "穹顶界域": 穹顶界域"""


class 黎明前的血色(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "黎明前的血色"  # 名称
        self.intro = "简介：消耗能量，对敌人造成一定伤害"  # 介绍
        self.description = "详细：（13能量）对目标造成基于自身攻击400%的伤害"  # 描述
        self.tag = "大招"  # 标签
        self.energy_cost = 13  # 能量消耗
        self.init()

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return
        msgs["damage"] = our["at"]*4


class 百雀难回巢(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "百雀难回巢"  # 名称
        self.intro = "简介：消耗能量，对敌人造成基于自身速度的多段伤害，并固定回复敌方能量"  # 介绍
        self.description = "详细：（12能量）对目标造成（基于自身速度*50%）次的多段伤害，每段伤害基于自身100%的攻击力，为敌方回复2点能量"  # 描述
        self.tag = "大招"
        self.energy_cost = 12  # 能量消耗
        self.init()

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return
        ticks = round(self.user.attributes["sp"]*0.5)  # 计算伤害次数
        msgs["damages"] = []
        for i in range(ticks):
            damage = our["at"]
            tool.energy_formulate_add(target, 2)
            msgs["damages"].append(damage)


class 三十三星神临(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "三十三，星神临"  # 名称
        self.intro = "简介：消耗能量，在行动轴上出现一个【暗然】，同时自身进入【星烁】状态"  # 介绍
        self.description = ("详细：(21能量)释放大招，自身进入【星烁】状态。"
                            "\n【星烁】：行动轴出现一个速度为3的【黯然】事件，【黯然】触发时退出【星烁】状态。"
                            "同时，自身攻击力增加300%，暴击率增加50%（期间不回能量）")  # 描述
        self.tag = "大招"  # 标签
        self.energy_cost = 21  # 能量消耗
        self.init()

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return
        self.user.state = "【星烁】"
        self.user.state_act = False
        msgs["Axle_act"] = "【黯然】"
        var1 = self.user.attributes_base["at"] * 3
        var2 = self.user.attributes_base["kr"] + 50
        self.user.charge_attribute(self.user.state, {"at": var1, "kr": var2})
        msgs["msgs"].append(f"【星烁】状态开始， 获得{var1}攻击力， {var2}暴击率")
        self.user.charge_attribute("【黯然】", {"at": var1, "kr": var2}, True)


class CivilizationEnd(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "文明尽头"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n(19能量)对敌方施加【黑子】（3回合/本回合立即生效），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "\n【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签
        self.energy_cost = 19  # 能量消耗
        self.init()

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return
        self.user.tick_tag_buff("【黑子】", target=target, our=our)
        if our["sh"] > 0:
            d = round(our["sh"] * 0.5)
        else:
            d = 0
        msgs["damage"] = d


class 生命以求顺(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "生命以求顺"  # 名称
        self.intro = "简介：\n消耗一定能量，"  # 介绍
        self.description = ("详细：\n（14能量）为双方施加【丰收】（2回合/本回合立即生效）（效果时间可叠加），"
                            "同时回复基于自身攻击力200%的生命值；同时驱散一个敌方一个buff（不限类型）"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签
        self.energy_cost = 14  # 能量消耗
        self.init()

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return


class 守护(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "守护"  # 名称
        self.intro = "简介：\n消耗能量，获得一定护盾值"  # 介绍
        self.description = "详细：\n（15能量）为我方增加基于自身防御力300%+300的护盾值"  # 描述
        self.tag = "大招"  # 标签
        self.energy_cost = 15  # 能量消耗
        self.init()

    def use(self, target, our, temp):
        super().use(target, our, temp)
        if "error" in temp.keys():
            return
        # 被动技能
        sh = round(our["df"] * 3 + 300)
        temp["shield"] = sh  # 赋值
        temp["msgs"].append(f"获得护盾值：{sh}")





class 全视未来:
    def __init__(self, user):
        self.user = user  # 用户对象
        self.name = "全视未来"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 超越时空的一刀:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "超越时空的一刀"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 红月初升其道异者:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "红月初升，其道异者"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 辉煌天:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "辉煌天"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 愿行与人前:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "愿行与人前"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 见神:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "见神"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 蛊祸:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "蛊祸"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 梦渊之魂:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "梦渊之魂"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 穹顶界域:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "穹顶界域"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 源于判罪之罚:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "源于判罪之罚"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 秋风随起幽兰望谷:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "秋风随起，幽兰望谷"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 这一击贯穿星辰:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "这一击，贯穿星辰"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 沉默中灭亡:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "沉默中灭亡"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 涵玄:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "涵玄"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 万死不辞:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "万死不辞"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 文明尽头:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "文明尽头"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 文明尽头:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "文明尽头"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签


class 文明尽头:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "文明尽头"  # 名称
        self.intro = "简介：\n消耗能量，对敌人造成基于护盾量的伤害，并对目标施加【黑子】"  # 介绍
        self.description = ("详细：\n（19能量）对敌方施加【黑子】（3回合），并对目标造成基于自身拥有的50%护盾量的伤害"
                            "【黑子】：受到伤害+20%")  # 描述
        self.tag = "大招"  # 标签
