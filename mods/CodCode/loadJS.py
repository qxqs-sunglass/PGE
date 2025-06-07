import json

__count__ = 0


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
        # 角色
        self.verify_actor_unique_STR = {
            "name": self.verify_unique, "role": self.verify_unique,
            "attributes": self.verify_unique,
        }  # 角色唯一字段
        self.verify_actor_optional_STR = {
            "tick_passive": None, "tick_passive_turn": None,
            "passive_type": None, "image_name": None,
            "author": None, "date": None, "story": None,
        }  # 角色可选字段
        self.verify_actor_special_STR = {
            "common": None, "common_path": self.verify_path,
            "combat": None, "combat_path": self.verify_path,
            "ultimate": None, "ultimate_path": self.verify_path,
            "passive": None, "passive_path": self.verify_path,
            "talent": None, "talent_path": self.verify_path
        }  # 角色特殊字段
        # 武器
        self.verify_equip_unique_STR = {
            "name": self.verify_unique
        }  # 武器唯一字段
        self.verify_equip_optional_STR = {}  # 武器可选字段
        self.verify_equip_special_STR = {}  # 武器特殊字段
        # 技能
        self.verify_skill_unique_STR = {
            "name": self.verify_unique, "tag": self.verify_unique
        }  # 技能唯一字段
        self.verify_skill_optional_STR = {}  # 技能可选字段
        self.verify_skill_special_STR = {}  # 技能特殊字段
        # 所有
        self.verify_actor_all_STR = {
            **self.verify_actor_unique_STR,
            **self.verify_actor_optional_STR,
            **self.verify_actor_special_STR
        }  # 角色所有字段
        self.verify_equip_all_STR = {
            **self.verify_equip_unique_STR,
            **self.verify_equip_optional_STR,
            **self.verify_equip_special_STR
        }  # 武器所有字段
        self.verify_skill_all_STR = {
            **self.verify_skill_unique_STR,
            **self.verify_skill_optional_STR,
            **self.verify_skill_special_STR
        }  # 技能所有字段
        self.verify_other_STR = {}  # 其他字段

    def _init_(self):
        global __count__
        """初始化"""
        self.json_data = None
        self.call_type = None
        __count__ = 0

    def load(self, file_path):
        """加载json文件"""
        self._init_()
        with open(file_path, 'r', encoding='utf-8') as f:
            self.json_data = json.load(f)
            f.close()
        print(self.json_data)
        # 合法性校验
        if "CALL_TYPE" in self.json_data:
            print("CALL_TYPE字段存在，开始校验数据...")
            self.call_type = self.json_data["CALL_TYPE"]
            self.call_type_dict[self.call_type](self.json_data)
        else:
            print("warning!!!: CALL_TYPE字段不存在，请检查json文件!!!")

        return self.json_data

    def verify_actor(self, data):
        """校验角色数据"""
        for key, value in data.items():
            if key == "Actor":
                print(value)
                for k, v in value.items():
                    if k in self.verify_actor_all_STR:
                        if self.verify_actor_all_STR[k] is not None:
                            self.verify_actor_all_STR[k](v, value)
                        else:
                            pass
                    else:
                        self.verify_other_STR[k] = None
                        self.hint_error_warning("字段{}不存在，请检查json文件!!!".format(k))
            elif key == "Skill":
                print(value)
            elif key == "CALL_TYPE":
                pass
            else:
                self.verify_other_STR[key] = None
                self.hint_error_warning("非法字段{}，请检查json文件!!!".format(key))

    def verify_equip(self, data):
        """校验武器数据"""
        pass

    def verify_skill(self, data):
        """校验技能数据"""
        pass

    @staticmethod
    def hint_error_warning(msg, warning=True):
        global __count__
        """提示错误信息"""
        if warning:
            print(__count__, "  warning!!!: " + msg)
            __count__ += 1
        else:
            print(__count__, "error!!!: " + msg)
            __count__ += 1

    def get_data(self):
        """获取json数据"""
        return self.json_data

    @staticmethod
    def verify_unique(unique_dict, data_dict):
        """校验唯一字段数据"""
        pass

    @staticmethod
    def verify_path(path_dict, data_dict):
        """校验路径数据"""
        pass
