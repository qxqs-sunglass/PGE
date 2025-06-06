from witelog import writelog
import tool


class SkillModule:
    def __init__(self):
        """初始化技能模块"""
        self.user = None
        self.name = "技能模块"
        self.intro = "技能模块"
        self.description = "技能模块"
        self.tag = "技能类型"
        self.attributes = {}  # 附加属性
        self.commands = {}  # use指令
        self.energy_cost = 0  # 能量消耗
        self.energy_add = 0  # 能量增加
        # 以上两个可选参数，可在json文件中定义
        self.energy_sys_mode = "auto"  # （auto/manual）能量系统模式, 默认为auto, 控制energy_active是否手动设置
        # 当在初始化中检测到energy_active的存在时, 系统会自动设置energy_sys_mode为manual，也可手动设置
        # 其他的对于energy_sys_mode的设置, 由数据自行决定
        self.energy_active = False  # 是否需要消耗能量, 默认不需要, 在对技能初始化时可由系统设置
        self.main_num_sub_active = True  # 是否消耗战技点, 默认消耗, 在对技能初始化时可由系统设置
        self.main_num_add_active = True  # 是否增加战技点, 默认增加, 在对技能初始化时可由系统设置
        self.helper_num_sub_active = True  # 是否消耗支援技能点, 默认消耗, 在对技能初始化时可由系统设置
        self.helper_num_add_active = False  # 是否增加支援技能点, 默认不增加, 在对技能初始化时可由系统设置
        self.use_tick = {
            "普攻": self.use_common,
            "战技": self.use_combat,
            "大招": self.use_ultimate
        }

    def init(self):
        """初始化技能模块"""
        if self.tag == "战技":
            if self.user.role_type == "主战":
                self.main_num_sub_active = True
            elif self.user.role_type == "助战":
                self.helper_num_sub_active = True

    def use(self, target, our, msgs):
        """使用技能"""
        self.use_tick[msgs["tag"][0]](target, our, msgs)

    def use_ultimate(self, target, our, msgs):
        """使用大招"""
        # 计算大招能量消耗
        if self.energy_active:  # 是否需要消耗能量
            m = tool.use_ultimate_formulate(our, self.energy_cost)
            if "error" in m:  # 错误信息
                msgs["error"] = m["error"]
                return
            self.user.extra_act = True

    def use_combat(self, target, our, msgs):
        """使用战技"""
        # 计算战技点
        if self.main_num_sub_active and self.user.role_type == "主战":
            m = tool.main_num_formulate_sub(our, self.user.cost_num_act)  # 主战消耗战技点, cost_num_act为是否使用技能点
            if "error" in m:  # 错误信息
                msgs["error"] = m["error"]
                return
        elif self.helper_num_sub_active and self.user.role_type == "助战":
            m = tool.helper_num_formulate_sub(our, self.user.cost_num_act)  # 助战消耗支援技能点, cost_num_act为是否使用技能点
            if "error" in m:  # 错误信息
                msgs["error"] = m["error"]
                return
        # 计算能量增加
        m = tool.energy_formulate_add(our, self.energy_add, self.user.state_act)
        if "error" in m:  # 错误信息
            msgs["error"] = m["error"]
            return

    def use_common(self, target, our, msgs):
        """使用普攻"""
        # 计算技能点增加
        if self.user.role_type == "主战":
            m = tool.main_num_formulate_add(our, adv=self.main_num_add_active)
            if "error" in m:  # 错误信息
                msgs["error"] = m["error"]
                return
        elif self.user.role_type == "助战":
            m = tool.helper_num_formulate_add(our, adv=self.helper_num_add_active)
            if "error" in m:  # 错误信息
                msgs["error"] = m["error"]
                return
        # 计算能量增加
        m = tool.energy_formulate_add(our, self.energy_add, self.user.state_act)
        return m

    def get_skill_name(self):
        """获取技能名称"""
        return self.name

    def get_skill_info(self):
        """获取技能信息"""
        return {
            "name": self.name,
            "intro": self.intro,
            "description": self.description,
            "tag": self.tag,
            "energy_cost": self.energy_cost,
            "energy_add": self.energy_add,
            "energy_active": self.energy_active,
            "main_num_active": [self.main_num_add_active, self.main_num_sub_active],
            "helper_num_active": [self.helper_num_add_active, self.helper_num_sub_active]
        }

    def error_msg(self, msg):
        """错误信息"""
        writelog(f"技能模块错误：{msg}")

    def call_act_attr(self, attr_name) -> int:
        """调用自身属性: 获取属性值
        attr_name: 属性名称"""
        return self.user.attributes.get(attr_name, 1)

    def call_in_attr(self, attr_name) -> int:  # 这里是附加属性的调用
        """调用自身属性: 获取属性值
        attr_name: 属性名称"""
        return self.attributes.get(attr_name, 1)

    def call_out_attr(self, attr_name, value) -> None:
        """调用自身属性: 设置属性值
        attr_name: 属性名称
        value: 属性值"""
        self.attributes[attr_name] = value
