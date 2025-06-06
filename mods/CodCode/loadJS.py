import json


class LoadJS:
    def __init__(self):
        """针对json文件进行解析"""
        self.json_data = None
        self.call_type = None
        self.call_type_dict = {
            "Actor": self.verify_actor,  # 角色（一般包含有多个技能）
            "Equip": self.verify_equip,  # 武器（一般拥有唯一的技能）
            "Skill": self.verify_skill  # 独立技能（独立于角色和武器存在, 内部可包含多个技能）
        }

    def load(self, file_path):
        """加载json文件"""
        with open(file_path, 'r', encoding='utf-8') as f:
            self.json_data = json.load(f)
        # 合法性校验
        if "CALL_TYPE" in self.json_data:
            self.call_type = self.json_data["CALL_TYPE"]
            self.call_type_dict[self.call_type](self.json_data)
        else:
            print("warning!!!: CALL_TYPE字段不存在，请检查json文件!!!")

    @staticmethod
    def verify_actor(data):
        """校验角色数据"""
        pass

    @staticmethod
    def verify_equip(data):
        """校验武器数据"""
        pass

    @staticmethod
    def verify_skill(data):
        """校验技能数据"""
        pass

    @staticmethod
    def hint_error_warning(msg, warning=True):
        """提示错误信息"""
        if warning:
            print("warning!!!: " + msg)
        else:
            print("error!!!: " + msg)

    def get_data(self):
        """获取json数据"""
        return self.json_data
