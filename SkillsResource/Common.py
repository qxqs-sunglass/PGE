from modules.module_skill import SkillModule
import tool
"""普攻技能模块"""


class Common:
    def __init__(self):
        self.skills = {
            "飞鸿": 飞鸿,
            "执法": 执法,
            "机动": 机动,
            "星华没，星垣现": 星华没星垣现,
            "埋土": 埋土,
            "惠恩": 惠恩
        }  # 普攻映射表
        """"告知": 告知,
        "因其而动": 因其而动,
        "除逆者": 除逆者,
        "一刀": 一刀,
        "取识": 取识,
        "神不可直视": 神不可直视,
        "普通攻击": 普通攻击,
        "虫毒": 虫毒,
        "斩": 斩,
        "射": 射"""


class 飞鸿(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.name = "飞鸿"
        self.intro = "简介：对敌人造成一定伤害"
        self.description = "详细：对目标造成基于自身攻击100%的伤害"
        self.tag = "普攻"
        self.energy_add = 1  # 能量增加
        self.init()

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs:
            return
        damage = our["at"]
        msgs["damage"] = damage


class 执法(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "执法"  # 名称
        self.intro = "简介：对敌人造成一定伤害，并加速自身"  # 介绍
        self.description = "详细：对目标造成基于自身攻击100%的伤害，对自身行动轴+2。"  # 描述
        self.tag = "普攻"  # 标签
        self.energy_add = 1  # 能量增加
        self.update_speed = 2  # 加速效果
        self.init()

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return
        damage = our["at"]
        # 触发加速效果
        self.user.axle_yu += self.update_speed  # 加速自身
        # 存储信息
        msgs["damage"] = damage  # 显示伤害
        msgs["speed"] = str(self.update_speed)  # 显示加速效果


class 机动(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "机动"  # 名称
        self.intro = "简介：对敌人造成一定伤害"  # 介绍
        self.description = "详细：对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签
        self.energy_add = 1  # 能量增加
        self.init()

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return
        damage = our["at"]
        msgs["damage"] = damage


class 星华没星垣现(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "星华没，星垣现"  # 名称
        self.intro = "简介：对敌人造成一定伤害"  # 介绍
        self.description = "详细：对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签
        self.energy_add = 1  # 能量增加
        self.init()

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return
        damage = our["at"]
        msgs["damage"] = damage


class 惠恩(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "惠恩"  # 名称
        self.intro = "简介：对敌人造成一定伤害"  # 介绍
        self.description = "详细：对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return
        damage = our["at"]
        msgs["damage"] = damage


class 埋土(SkillModule):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "埋土"  # 名称
        self.intro = "简介：对敌人造成一定伤害"  # 介绍
        self.description = "详细：对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签

    def use(self, target, our, msgs):
        super().use(target, our, msgs)
        if "error" in msgs.keys():
            return
        damage = our["at"]
        msgs["damage"] = damage


class 告知:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "告知"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害"  # 介绍
        self.description = "详细：\n对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签


class 因其而动:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "因其而动"  # 名称
        self.intro = "简介：对敌人造成一定伤害"  # 介绍
        self.description = "详细：对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签


class 除逆者:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "除逆者"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害"  # 介绍
        self.description = "详细：\n对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签


class 一刀:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "一刀"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害"  # 介绍
        self.description = "详细：\n对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签


class 取识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "取识"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害"  # 介绍
        self.description = "详细：\n对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签


class 神不可直视:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神不可直视"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害"  # 介绍
        self.description = "详细：\n对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签


class 普通攻击:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "普通攻击"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害"  # 介绍
        self.description = "详细：\n对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签


class 虫毒:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "虫毒"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害"  # 介绍
        self.description = "详细：\n对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签


class 斩:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "斩"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害"  # 介绍
        self.description = "详细：\n对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签


class 射:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "射"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害"  # 介绍
        self.description = "详细：\n对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签


class 殊死:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "殊死"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害"  # 介绍
        self.description = "详细：\n对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签


class 肴宴不止:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "肴宴不止"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害"  # 介绍
        self.description = "详细：\n对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签


class 衍化:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "衍化"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害"  # 介绍
        self.description = "详细：\n对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签


class 注视:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "注视"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害"  # 介绍
        self.description = "详细：\n对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签


class 贯彻信念:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "贯彻信念"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害"  # 介绍
        self.description = "详细：\n对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签


class 守秋:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "守秋"  # 名称
        self.intro = "简介：\n对敌人造成一定伤害"  # 介绍
        self.description = "详细：\n对目标造成基于自身攻击100%的伤害"  # 描述
        self.tag = "普攻"  # 标签





