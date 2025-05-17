from modules.module_act import ActTemplate
from SkillsResource.Skills import Skills
from witelog import writelog
import json
"""
被动类型:
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


class ImportAct:
    def __init__(self):
        """导入角色"""
        # 获取需要导入的角色列表
        with open("bin/ReadActList.json", "r", encoding="utf-8") as f:
            self.act_read_list = json.load(f)
            f.close()
        writelog(f"角色列表:{self.act_read_list}")
        # print("角色列表:", self.act_dict)
        self.actors = {}  # 角色字典
        self.skills = Skills()  # 技能类

    def init(self, ai, screen):
        """初始化界面"""
        self.init_acts(ai, screen)
        self.init_skill()

    def init_skill(self):
        """初始化技能"""
        writelog("开始加载技能")
        for act in self.actors.values():
            for skill_name in act.skill_list:  # 获取角色的技能列表
                # 获取角色的技能
                skill = self.skills.get_skills(skill_name)  # 获取对应技能
                if skill is None:  # 找不到技能
                    continue
                temp = skill(act)
                act.skills[skill_name] = temp  # 角色技能字典
            writelog(f"{act.name}技能:{act.skills.keys()}")

    def init_acts(self, ai, screen):
        """初始化角色导入"""
        for name, path in self.act_read_list.items():
            # name:角色名称，path:角色路径
            actor = ActTemplate()
            actor.path = path
            actor.init(ai, screen)
            self.actors[name] = actor
        writelog(f"角色字典:{self.actors}")
        # print("角色字典:", self.acts)
