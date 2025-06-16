import json
import os

__count__ = 0
__warning__ = 0
__error__ = 0


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
        self.verify_actor_unique_STR = [
            "name", "role",
            "attributes",
        ]  # 角色唯一字段
        self.verify_actor_optional_STR = [
            "tick_passive", "tick_passive_turn",
            "passive_type", "image_name",
            "author", "date", "story",
        ]  # 角色可选字段
        self.verify_actor_special_STR = [
            "common", "common_path",
            "combat", "combat_path",
            "ultimate", "ultimate_path",
            "passive", "passive_path",
            "talent", "talent_path"
        ]  # 角色特殊字段
        # 武器
        self.verify_equip_unique_STR = [
            "name"
        ]  # 武器唯一字段
        self.verify_equip_optional_STR = []  # 武器可选字段
        self.verify_equip_special_STR = []  # 武器特殊字段
        # 技能
        self.verify_skill_unique_STR = [
            "name", "tag", "command"
        ]  # 技能唯一字段
        self.verify_skill_optional_STR = [
            "intro", "desc"
        ]  # 技能可选字段
        self.verify_skill_special_STR = [
            "energy_add", "attributes", "energy_active", "main_num_sub_active",
            "main_num_add_active", "helper_num_sub_active", "helper_num_add_active"
        ]  # 技能特殊字段（非必选字段）  不用弹警告
        # 所有
        self.verify_actor_all_STR = (
                self.verify_actor_unique_STR +
                self.verify_actor_optional_STR +
                self.verify_actor_special_STR)  # 角色所有字段
        # print(self.verify_actor_all_STR)
        self.verify_equip_all_STR = (
            self.verify_equip_unique_STR +
            self.verify_equip_optional_STR +
            self.verify_equip_special_STR
        )  # 武器所有字段
        self.verify_skill_all_STR = (
            self.verify_skill_unique_STR +
            self.verify_skill_optional_STR +
            self.verify_skill_special_STR
        )  # 技能所有字段
        self.verify_other_STR = []  # 其他字段
        # 技能组件
        self.skill_dict = {
            "common": self.skill_verify,
            "combat": self.skill_verify,
            "ultimate": self.skill_verify,
            "passive": self.skill_verify,
            "talent": self.talent_verify
        }  # 技能字典

    def _init_(self):
        global __count__, __warning__, __error__
        """初始化"""
        self.json_data = None
        self.call_type = None
        __count__ = 0
        __warning__ = 0
        __error__ = 0

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
            self.hint_error_warning("CALL_TYPE字段不存在，请检查json文件!!!", False)

        print("数据校验完毕！")
        print("共{}个错误提示，{}个警告提示。".format(__error__, __warning__ + 1))
        print("---------------------")
        os.system("cls")

        return self.json_data

    def verify_actor(self, data):
        """校验角色数据"""
        for key, value in data.items():
            if key == "Actor":
                # print(value)
                for k in self.verify_actor_unique_STR:
                    if k in value.keys():
                        print("{}：    {}".format(k, value[k]))
                    else:
                        self.hint_error_warning("字段{}不存在，请检查json文件!!!".format(k), False)
                for k in self.verify_actor_optional_STR:
                    if k in value.keys():
                        print("{}：    {}".format(k, value[k]))
                    else:
                        self.hint_error_warning("字段{}不存在，请检查json文件!!!".format(k))
                for k in self.verify_actor_special_STR:
                    if k in value.keys():
                        print("{}：    {}".format(k, value[k]))
                    else:
                        self.hint_error_warning("字段{}不存在，请检查json文件!!!".format(k))
            elif key == "Skill":
                # print(value)
                for may, skill in value.items():
                    if may in self.skill_dict:
                        self.skill_dict[may](skill)
                    else:
                        self.hint_error_warning("技能类型{}不存在，请检查json文件!!!".format(may))
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
        global __count__, __warning__, __error__
        """提示错误信息"""
        if warning:
            print(__count__, "  warning!!!: " + msg)
            __count__ += 1
            __warning__ += 1
        else:
            print(__count__, "error!!!: " + msg)
            __count__ += 1
            __error__ += 1

    def get_data(self):
        """获取json数据"""
        return self.json_data

    def talent_verify(self, data):
        """校验天赋数据"""
        for v in data:
            self.skill_verify(v)

    def skill_verify(self, data):
        """校验普攻数据"""
        print("当前数据为：", data)
        for k in self.verify_skill_unique_STR:
            if k in data.keys():
                print("{}：    {}".format(k, data[k]))
            else:
                self.hint_error_warning("字段{}不存在，请检查json文件!!!".format(k), False)
        for k in self.verify_skill_optional_STR:
            if k in data.keys():
                print("{}：    {}".format(k, data[k]))
            else:
                self.hint_error_warning("字段{}不存在，请检查json文件!!!".format(k))
        for k in self.verify_skill_special_STR:
            if k in data.keys():
                print("{}：    {}".format(k, data[k]))
