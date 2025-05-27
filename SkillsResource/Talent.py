"""天赋技能模块"""
from modules.module_talent import ModuleTalent


class Talent:
    def __init__(self):
        self.skills = {
            "万家灯火": 万家灯火, "任务加速": 任务加速, "夜巡游": 夜巡游,
            "扶摇": 扶摇, "千鸿难回天": 千鸿难回天, "飞虹": 飞虹,
            "帝星极威": 帝星极威, "绽华星闪": 绽华星闪, "星茧塑身": 星茧塑身,
            "执行官": 执行官, "极限功率": 极限功率, "神明造物，自我意识": 神明造物自我意识,
            "先攻": 先攻, "传告": 传告, "启航": 启航,
            "葬敌": 葬敌, "葬己": 葬己, "葬界": 葬界,
            "逆长": 逆长, "洗涤": 洗涤, "盛穗": 盛穗,
            "留心": 留心, "决心": 决心, "惑心": 惑心,
            "破敌": 破敌, "渐停": 渐停, "止樱散": 止樱散,
            "第二世界": 第二世界, "夺识": 夺识, "困魂此地": 困魂此地,
            "回光": 回光, "日下非": 日下非, "升华": 升华,
            "望志存心": 望志存心, "回忆前尘": 回忆前尘, "求愿": 求愿,
            "求助": 求助, "神惠": 神惠, "共邀": 共邀,
            "自愈": 自愈, "炼虫": 炼虫, "共生": 共生,
            "五阴木": 五阴木, "梦觉": 梦觉, "斩魂": 斩魂,
            "附魔": 附魔, "齐发": 齐发, "魔规划": 魔规划
        }  # 天赋技能表


class 万家灯火(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "万家灯火"  # 名称
        self.intro = "简介：\n增加自身大招倍率"  # 介绍
        self.description = "详细：\n万家灯火：战斗中，增加自身大招200%倍率。"  # 描述
        self.tag = "天赋"


class 任务加速(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "任务加速"  # 名称
        self.intro = "简介：\n提升自身行动速度"  # 介绍
        self.description = "详细：\n任务加速：战斗中，+2速度。"  # 描述
        self.tag = "天赋"


class 夜巡游(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "夜巡游"  # 名称
        self.intro = "简介：\n提升自身行动速度"  # 介绍
        self.description = "详细：\n夜巡游：战斗中，普攻命中后，多回一点大招能量，且在额外回合中，回能多+1。"  # 描述
        self.tag = "天赋"


class 扶摇(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.name = "扶摇"
        self.intro = "简介：\n提高暴击率"
        self.description = "详细：\n【战技】额外+20%暴击率"
        self.tag = "天赋"


class 千鸿难回天(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.name = "千鸿难回天"
        self.intro = "简介：\n加速自身"
        self.description = "详细：\n释放【百雀难回巢】后行动轴+2"
        self.tag = "天赋"


class 飞虹(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.name = "飞虹"
        self.intro = "简介：\n提高伤害，并无视一定防御"
        self.description = "详细：\n【飞鸿】+100%伤害倍率，且无视对方100防御"
        self.tag = "天赋"


class 帝星极威(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "帝星极威"  # 名称
        self.intro = "简介：\n增加造成的伤害"  # 介绍
        self.description = "详细：\n【星烁】状态下额外增加40%伤害"  # 描述
        self.tag = "天赋"


class 绽华星闪(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "绽华星闪"  # 名称
        self.intro = "简介：\n增加回能"  # 介绍
        self.description = "详细：\n攻击拥有【罪星】的目标时额外回1能量"  # 描述
        self.tag = "天赋"


class 星茧塑身(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "星茧塑身"  # 名称
        self.intro = "简介：\n释放大招回复血量"  # 介绍
        self.description = "详细：\n进入【星烁】状态时回复自身20%血量"  # 描述
        self.tag = "天赋"


class 执行官(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "执行官"  # 名称
        self.intro = "简介：\n增加自身基础攻击"  # 介绍
        self.description = "详细：\n战技额外增加100基础攻击"  # 描述
        self.tag = "天赋"


class 极限功率(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "极限功率"  # 名称
        self.intro = "简介：\n提升自身伤害倍率"  # 介绍
        self.description = "详细：\n攻击拥有【黑子】的目标时，提高20%伤害倍率"  # 描述
        self.tag = "天赋"


class 神明造物自我意识(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 先攻(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "先攻"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 传告(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "传告"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 启航(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "启航"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 葬敌(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "葬敌"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 葬己(ModuleTalent):
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "葬己"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 葬界:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "葬界"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 逆长:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "逆长"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 洗涤:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "洗涤"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 盛穗:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "盛穗"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 留心:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "留心"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 决心:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "决心"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 惑心:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "惑心"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 破敌:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "破敌"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 渐停:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "渐停"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 止樱散:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "止樱散"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 第二世界:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "第二世界"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 夺识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "夺识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 困魂此地:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "困魂此地"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 回光:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "回光"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 日下非:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "日下非"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 升华:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "升华"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 望志存心:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "望志存心"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 回忆前尘:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "回忆前尘"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 求愿:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "求愿"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 求助:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "求助"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神惠:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神惠"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 共邀:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "共邀"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 自愈:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "自愈"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 炼虫:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "炼虫"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 共生:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "共生"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 五阴木:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "五阴木"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 梦觉:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "梦觉"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 斩魂:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "斩魂"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 附魔:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "附魔"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 齐发:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "齐发"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 魔规划:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "魔规划"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神明造物自我意识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 先攻:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "先攻"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 传告:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "传告"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 启航:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "启航"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 葬敌:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "葬敌"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 葬己:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "葬己"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 葬界:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "葬界"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 逆长:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "逆长"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 洗涤:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "洗涤"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 盛穗:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "盛穗"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 留心:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "留心"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 决心:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "决心"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 惑心:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "惑心"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 破敌:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "破敌"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 渐停:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "渐停"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 止樱散:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "止樱散"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 第二世界:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "第二世界"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 夺识:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "夺识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 困魂此地:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "困魂此地"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 回光:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "回光"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 日下非:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "日下非"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 升华:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "升华"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 望志存心:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "望志存心"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 回忆前尘:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "回忆前尘"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 求愿:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "求愿"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 求助:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "求助"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 神惠:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神惠"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 共邀:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "共邀"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 自愈:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "自愈"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 炼虫:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "炼虫"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 共生:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "共生"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 五阴木:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "五阴木"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 梦觉:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "梦觉"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 斩魂:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "斩魂"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 附魔:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "附魔"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 齐发:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "齐发"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 魔规划:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "魔规划"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 血战:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "血战"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 百死:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "百死"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 鏖灭:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "鏖灭"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 一生二:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "一生二"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 二化四:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "神明造物，自我意识"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 四衍八:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "四衍八"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 沉默中爆发:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "沉默中爆发"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 连续剧:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "连续剧"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 合奏曲:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "合奏曲"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 巡游:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "巡游"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 猎杀:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "猎杀"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 大捷:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "大捷"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 花蕾:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "花蕾"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 花开:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "花开"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"


class 花落:
    def __init__(self, user):
        super().__init__()
        self.user = user  # 用户对象
        self.name = "花落"  # 名称
        self.intro = "简介：\n提升自身护盾量，并根据造成的伤害获得额外护盾量，进入战斗获得额外护盾量"  # 介绍
        self.description = ("详细：\n护盾量无上限，并根据已方造成的伤害，获得基于造成伤害60%的额外护盾量，"
                            "进入战斗获得基于自身护盾值100%的额外护盾量")  # 描述
        self.tag = "天赋"
