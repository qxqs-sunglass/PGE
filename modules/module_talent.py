class ModuleTalent:
    def __init__(self):
        """天赋技能模板"""
        self.user = None  # 所有者
        self.name = "默认名称"  # 名称
        self.intro = "默认介绍"  # 介绍
        self.description = "默认描述"  # 描述
        self.tag = "默认标签"  # 标签
        # 用于记录天赋的类型
        # 001:
        # 002:
        # 003:
        # 以上为基础属性，可以根据实际情况更改
        self.choose_command = None  # 用于系统判定

    def init(self):
        pass

    def use(self, user, target, temp):
        pass

    def run_choose_command(self):
        """选择命令"""
        self.choose_command(self.get_data())

    def get_data(self):
        """获取技能信息"""
        return {
            "name": self.name,
            "intro": self.intro,
            "description": self.description,
            "tag": self.tag,
            "skill": self.use
        }

