from modules.module_skill import SkillModule
import tool
""""""


class Combat:
    def __init__(self):
        self.skills = {
            "鹏起": 鹏起,
            "执法支援": 执法支援,
            "协约": 协约,
            "百逆罪，诛生世": 百逆罪诛生世,
            "铸就": 铸就,
            "生机勃": 生机勃
        }  # 战技字典, 技能映射
        """"聚众之愿": 聚众之愿,
        "觅神迹": 觅神迹,
        "启凡航程": 启凡航程,
        "试探": 试探,
        "刹那一刀": 刹那一刀,
        "月光所照": 月光所照,
        "日下凡": 日下凡,
        "嫁接": 嫁接,
        "施法": 施法,
        "见梦": 见梦"""


class 鹏起(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.name = "飞鸿"
        self.intro = "简介：获得暴击率，并造成伤害"
        self.description = "详细：获得【+20暴击率】(本回合立即生效，持续2回合)，并对目标造成基于自身攻击100%的伤害"
        self.tag = "战技"
        self.energy_add = 2  # 增加能量值
        self.init()

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return
        # 以下为战技效果
        self.user.tick_tag_buff("暴击率", target=target, our=our, value={"turn": 2, "num": 20})
        # 造成伤害
        damage = our["at"]
        msgs["damage"] = damage


class 执法支援(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "执法支援"  # 名称
        self.intro = "简介：对敌人造成一定伤害"  # 介绍
        self.description = "详细：对目标造成基于自身攻击200%的伤害。"  # 描述
        self.tag = "战技"  # 标签
        self.energy_add = 2  # 能量增加
        self.init()

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return
        # 以下为战技效果
        # 造成伤害
        damage = our["at"] * 2
        msgs["damage"] = damage


class 协约(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "协约"  # 名称
        self.intro = "简介：基于护盾造成伤害"  # 介绍
        self.description = "详细：造成基于拥有的防御力上限的10%护盾的伤害，并额外增加200伤害。"  # 描述
        self.tag = "战技"  # 标签
        self.energy_add = 2  # 能量增加
        self.init()

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return
        # 以下为战技效果
        # 计算护盾
        damage = round(our["sh"] * 0.1) + 200
        msgs["damage"] = damage


class 百逆罪诛生世(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "百逆罪，诛生世"  # 名称
        self.intro = "简介：对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：指定敌方获得【罪星】（三回合，本回合立即生效）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签
        self.energy_add = 2  # 能量增加
        self.init()

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return
        # 以下为战技效果
        self.user.tick_tag_buff("【罪星】", target=target, our=our)
        # 造成伤害
        damage = our["at"]
        msgs["damage"] = damage


class 铸就(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "铸就"  # 名称
        self.intro = "简介：\n获得一定护盾"  # 介绍
        self.description = "详细：\n为我方施加基于自身防御力上限200%的护盾"  # 描述
        self.tag = "战技"  # 标签

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return
        # 以下为战技效果
        msgs["shield"] = round(our["df"] * 2)


class 生机勃(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "生机勃"  # 名称
        self.intro = "简介：\n回复生命值，并为双方施加【丰收】"  # 介绍
        self.description = ("详细：\n为我方回复基于自身攻击力上限的100%的生命值，"
                            "同时为敌我双方施加【丰收】（两回合，效果时间可叠加）。")  # 描述
        self.tag = "战技"  # 标签

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return
        # 以下为战技效果


class 聚众之愿:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = " 聚众之愿"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：\n指定敌方获得【罪星】（三回合）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签


class 觅神迹:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "觅神迹"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：\n指定敌方获得【罪星】（三回合）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签


class 启凡航程:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "启凡航程"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：\n指定敌方获得【罪星】（三回合）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签


class 试探:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "试探"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：\n指定敌方获得【罪星】（三回合）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签


class 刹那一刀:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "刹那一刀"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：\n指定敌方获得【罪星】（三回合）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签


class 见梦:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "见梦"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：\n指定敌方获得【罪星】（三回合）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签


class 月光所照:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "月光所照"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：\n指定敌方获得【罪星】（三回合）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签


class 日下凡:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "日下凡"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：\n指定敌方获得【罪星】（三回合）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签


class 嫁接:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "嫁接"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：\n指定敌方获得【罪星】（三回合）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签


class 施法:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "施法"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：\n指定敌方获得【罪星】（三回合）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签

class 鏖战不休:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "鏖战不休"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：\n指定敌方获得【罪星】（三回合）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签


class 百箓:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "百箓"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：\n指定敌方获得【罪星】（三回合）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签


class 向着星空:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "向着星空"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：\n指定敌方获得【罪星】（三回合）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签


class 曲终人散:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "曲终人散"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：\n指定敌方获得【罪星】（三回合）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签


class 清风:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "清风"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害并获得【罪星】"  # 介绍
        self.description = "详细：\n指定敌方获得【罪星】（三回合）随后对其造成基于自身攻击100%。【罪星】受到伤害+20%。"  # 描述
        self.tag = "战技"  # 标签

