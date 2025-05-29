from SkillsResource.Common import Common   # 导入Common类，普攻
from SkillsResource.Combat import Combat   # 导入Combat类，战技
from SkillsResource.Ultimate import Ultimate   # 导入Ultimate类，大招
from SkillsResource.Talent import Talent   # 导入Talent类，天赋
from SkillsResource.Passive import Passive   # 导入Passive类,被动


class Skills:
    def __init__(self):
        """技能类，用于管理所有技能的实例"""
        self.skills = {}
        self.common = Common()  # 实例化普攻类
        self.combat = Combat()  # 实例化战技类
        self.ultimate = Ultimate()  # 实例化大招类
        self.talent = Talent()  # 实例化天赋类
        self.passive = Passive()  # 实例化被动类
        # 各技能类实例化，技能的名称和技能函数绑定在实例的skills字典中
        for temp in [self.common, self.combat, self.ultimate, self.talent, self.passive]:  # 遍历所有技能类
            for name, skill in temp.skills.items():  # 遍历技能字典
                self.skills[name] = skill  # 将技能添加到技能字典中
        # print("技能初始化完成！", self.skills)

    def get_skills(self, name):
        if name not in self.skills:
            return None
        return self.skills[name]


class SkillTest:
    def __init__(self):
        """2.0技能测试类"""

