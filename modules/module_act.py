from witelog import *
from modules.module_equips import EquipTemplate
from modules.module_button import ButtonModule
from copy import deepcopy
from tool import get_buff
import json
import tkinter
import tool


class ActTemplate:
    def __init__(self):
        """角色模板
        hp: 生命值
        hp_max: 最大生命值
        at: 攻击力
        df: 防御力
        kr: 暴击率
        kd: 暴击伤害
        sp: 速度
        rt: 抗性
        ids: 增伤
        vl: 易伤
        rh: 减伤
        ha: 免伤
        dr: 伤害倍率
        """
        self.attributes_name = ["at", "df", "kr", "kd",
                                "sp", "rt", "ids", "vl",
                                "rh", "ha", "dr"]  # 角色属性名称
        self.attributes_name_fu = {"at": "攻击力", "df": "防御力",
                                   "kr": "暴击率", "kd": "暴击伤害",
                                   "sp": "速度", "rt": "抗性",
                                   "ids": "增伤", "vl": "易伤",
                                   "rh": "减伤", "ha": "免伤",
                                   "dr": "伤害倍率"}  # 角色属性名称的复数形式
        # 角色技能
        self.skills_name = ["普攻", "战技", "大招", "被动", "天赋"]  # 角色技能名称
        self.skills_name_fu = {"普攻": "skills_普攻",
                               "战技": "skills_战技",
                               "大招": "skills_大招",
                               "被动": "skills_被动",
                               "天赋": "skills_天赋"}
        self.skills_name_fu2 = {"普攻": None,
                                "战技": None,
                                "大招": None,
                                "被动": None,
                                "天赋": None}   # 角色技能名称的复数形式
        self.skills_type = {"普攻": "common",
                            "战技": "combat",
                            "大招": "ultimate",
                            "被动": "passive",
                            "天赋": "talent"}  # 角色技能名称的复数形式
        self.skills = {}  # 角色的技能
        self.skill_list = []  # 角色的技能列表
        self.stats_buff = {}  # 角色的buff(包括Debuff和Buff)
        # 基础信息
        self.name = "默认"  # 角色名称
        self.name_des = "【】"  # 角色称号
        self.name_base = "默认"  # 角色本名
        self.role = "零"  # 角色类型: 天\星\冥
        self.story = "人物故事：无"  # 角色故事
        self.author = "秋雪青山"  # 角色作者
        self.date = "--2025.2.14--"  # 角色创作日期
        self.attributes_base = {"kr": 10, "kd": 50, "energy_max": 25}  # 角色的属性值
        self.attributes_extra = {}  # 角色的额外属性值; 格式为{名字: {属性名称: 属性值}}
        self.attributes = {}  # 角色的属性值
        # 基础属性绝对不变，额外属性用于计算，而attributes为复制的基础属性
        # 在计算的时候使用attributes和attributes_extra叠加计算
        self.image = None  # 角色图片,此处为tk.PhotoImage对象
        self.image_name = "actor.png"  # 角色图片名称
        self.axle = 14  # 角色的行动轴位置
        self.axle_init = 14  # 角色的初始行动轴位置
        self.axle_max = 14  # 角色的最大行动轴位置
        self.axle_yu = 0  # 角色剩余行动点数
        self.axle_extra = 0  # 角色额外行动点数
        self.path = ""  # 数据文件路径
        self.path_data = {}  # 数据文件内容
        self.camp = ""  # 阵营
        self.role_type = ""  # 角色类型: 主战\助战
        self.state = ""  # 角色状态
        self.buff_tag = {}  # 触发buff的名称
        # self.buff_tag = {"名字": "触发目标"}
        # self.tag_buff = {"名字": {"name": 属性名称, "turn": 持续回合数,
        #                  "superposition": 叠加次数, "active": 效果激活状态,
        #                  "type": 效果类型}}
        self.tick_passive = 0  # 被动技能的触发次数
        self.tick_passive_turn = 0  # 被动技能的冷却回合数
        self.passive_type = []  # 被动技能类型
        # tag_buff的格式为buff_name: {"效果名称": {"name": 属性名称, "turn": 持续回合数,
        #                             "active": 效果激活状态, "type": 效果类型}}
        # 状态变量
        self.state_act = True  # 是否回复能量
        self.cost_num_act = True  # 是否消耗战技点数
        self.update_buff_act = True  # 是否更新buff
        self.refresh_buff_act = False  # 是否刷新buff，用于刷新buff的持续时间
        self.add_turn_buff_act = False  # 是否增加buff的持续时间
        self.extra_act = False  # 是否额外行动
        self.passive_global = [False, False]  # 被动
        self.equip_global = [False, False]  # 装备效果
        # [我方回合触发，敌人回合发触发]全局变量，用于判断是否触发被动技能
        # 武器
        self.equip: EquipTemplate = None  # 武器
        self.equip_type = None  # 武器类型
        self.equip_but = None  # 武器按钮
        self.equip_special_attr = {"sp": self.axle_extra}  # 特殊属性
        # 信息展示
        self.screen = None  # 窗口对象
        self.show_info_fu = ["名字", "", "", "", "", ""]
        self.show_info = {}  # 信息展示字典
        self.positions = {
            "名字": (5, 5), "武器": (30, 5)
        }
        # 其他
        self.choose_command = None  # 选择命令
        self._buff_tag = {
            "target": ["target"],
            "our": ["our"],
            "tar_our": ["target", "our"]
        }  # 触发buff的名称

    def init(self, ai, screen):
        """此处的初始化包括了窗口的初始化、数据导入、UI绘制、事件绑定等"""
        self.load_data()
        self.init_screen(screen)
        self.init_ui(ai)

    def init_equip(self):
        """初始化武器"""
        self.equip.user = self  # 武器绑定角色
        self.equip_type = self.equip.equip_type  # 武器类型标
        self.equip_global = self.equip.equip_global  # 武器是否为全局武器
        self.buff_tag.update(self.equip.buff_tag)  # 武器的buff标签

    def init_ui(self, ai):
        """初始化UI"""
        # 在这里写UI初始化代码
        self.image = ai.images.get_sprite_image(self.screen, self.image_name)
        self.equip_but = ButtonModule(self.screen, self.positions["武器"], "武器", self.show_equip)

    def init_screen(self, screen):
        """初始化窗口"""
        self.screen = tkinter.Toplevel(screen)  # 创建窗口
        self.screen.title(self.name)  # 设置窗口标题
        self.screen.geometry("300x200")
        self.screen.resizable(False, False)  # 禁止缩放
        self.screen.protocol("WM_DELETE_WINDOW", self.close_screen)  # 关闭窗口时调用close_screen方法
        self.screen.withdraw()  # 隐藏窗口

    def show_equip(self):
        """显示武器"""
        if self.equip is not None:
            self.equip.show()

    def close_screen(self):
        """关闭窗口, 已与窗口的关闭按钮(事件)绑定"""
        self.screen.withdraw()  # 隐藏窗口

    def show(self):
        """显示窗口
        注：此方法会打开一个新的窗口，并在窗口中显示当前模板的UI。
        只需要调用此方法即可显示窗口"""
        self.screen.deiconify()  # 显示窗口
        self.draw()

    def update(self):
        """更新角色状态"""
        self.update_info()  # 更新信息展示

    def update_info(self):
        """更新信息展示"""

    def draw(self):
        """绘制UI"""
        self.equip_but.draw()  # 绘制武器按钮

    def load_data(self):
        with open(self.path, 'r', encoding='utf-8') as f:  # 加载数据
            data = json.load(f)
            f.close()
        self.path_data = data
        for attr in self.attributes_name:  # 加载属性
            if attr not in self.attributes_base.keys():  # 避免重复加载
                self.attributes_base[attr] = data[attr]  # 加载属性值
        self.attributes = deepcopy(self.attributes_base)  # 复制属性值
        for key in data.keys():  # 加载其他信息
            if key in self.attributes_name:  # 跳过属性
                continue
            self.__dict__[key] = data[key]  # 此处必须保证属性名与字典键名一致
        des_base = self.dispose_name(self.name)
        self.name_des = des_base["name_des"]
        self.name_base = des_base["name_base"]

        for skill_name in self.skills_name:  # 加载技能
            # 这里加载的是技能名称，而不是技能对象
            if type(data[self.skills_name_fu[skill_name]]) == list:  # 加载技能列表
                self.skill_list.extend(data[self.skills_name_fu[skill_name]])  # 多技能加载
                self.skills_name_fu2[skill_name] = data[self.skills_name_fu[skill_name]]  # 加载技能名称的复数形式
            else:  # 加载单个技能
                self.skill_list.append(data[self.skills_name_fu[skill_name]])  # 加载技能名称
                self.skills_name_fu2[skill_name] = data[self.skills_name_fu[skill_name]]  # 加载技能名称的复数形式
        writelog("加载角色数据：" + self.name)

    def tick_tag_buff(self, buff_name, **kwargs):
        """增加buff"""
        if buff_name not in self.buff_tag.keys():
            return  # 无效buff
        tag = self.buff_tag[buff_name]  # 获取标签
        for to_tag in self._buff_tag[tag]:  # 遍历标签
            tag = kwargs[to_tag]  # 获取目标或我们
            if buff_name not in tag["buff"].keys() or self.refresh_buff_act:  # 目标没有该buff或需要刷新buff
                tag["buff"][buff_name] = get_buff(buff_name, **kwargs)  # 给目标添加buff
                return
            elif buff_name not in tag["buff"].keys() or self.add_turn_buff_act:  # 目标没有该buff
                tag["buff"]["turn"] += get_buff(buff_name, **kwargs)["turn"]  # 增加buff持续时间

    def update_buff(self, **kwargs):
        """更新buff"""
        if not self.buff_tag.keys():  # 没有buff
            return  # 无效
        for to_tar in ["target", "our"]:
            buff: dict = kwargs.get(to_tar, dict())["buff"]  # 获取目标或我们
            if len(buff) == 0:  # 无效目标
                continue
            pop_list = []  # 待删除的buff列表
            for buff_value in buff.values():  # 遍历目标的buff
                if not buff_value["active"]:  # 该buff的"active"状态为False
                    continue  # 跳过该buff

                if buff_value["name"] in self.buff_tag.keys() and buff_value["type"] == "001":
                    # 该buff属于该角色，且类型为001(普通buff)
                    if buff_value["turn"]-1 > 0:  # 该buff持续时间大于0
                        buff_value["turn"] -= 1  # 减少buff持续时间
                    else:  # 该buff持续时间等于0
                        pop_list.append(buff_value["name"])  # 待删除的buff列表
                elif buff_value["type"] == "002":  # 属于002(持续效果buff)
                    if buff_value["owner"] == self.name:  # 该buff属于该角色
                        if buff_value["turn"]-1 > 0:  # 该buff持续时间大于0
                            buff_value["turn"] -= 1  # 减少buff持续时间
                        else:  # 该buff持续时间等于0
                            pop_list.append(buff_value["name"])  # 待删除的buff列表
            for name in pop_list:  # 待删除的buff列表
                if name in buff.keys():
                    buff.pop(name)  # 删除buff

    def use_skill(self, skill_name, target, our, temp):
        """释放技能
        skill_name: 技能名称
        target: 目标对象
        our: 我们自己
        注：target和our是字典，包含了目标对象的所有信息，包括血量、攻击力等"""
        # print(self.skills[skill_name].use)
        if skill_name not in self.skills.keys():  # 技能不存在
            return {"error": "技能不存在-->"}  # 报错
        # 使用技能
        temp["tag"][0] = self.skills[skill_name].tag  # 技能的标签

        self.__imp_extra_attr(our)  # 导入额外属性

        self.skills[skill_name].use(target, our, temp)  # 调用技能的use方法，获取技能产生的消息列表
        if "error" in temp.keys():  # 报错
            return  # 报错
        writelog("技能释放：" + skill_name)
        tool.formulate_buff(target, our)  # 计算buff: all; except special buffs
        tool.formulate_special_buff(target, our)

        if "damages" in temp.keys():  # 伤害列表
            i = 0
            temp["damage"] = 0  # 总伤害
            for damage in temp["damages"]:
                damage = tool.formulate_damage(target, our, damage)  # 计算伤害
                temp["msgs"].append(f"第{i + 1}段伤害：{damage}")
                i += 1
                temp["damage"] += damage  # 计算总伤害
        elif "damage" in temp.keys():  # 伤害
            temp["damage"] = tool.formulate_damage(target, our, temp["damage"])  # 计算伤害

        if self.extra_act:  # 额外行动
            self.update_buff_act = False  # 关闭更新buff
            temp["msgs"].append("额外行动！")  # 额外行动提示
        if "kr_count" in our:
            temp["msgs"].append(our["kr_count"])
            our.pop("kr_count")
        # 处理buff
        if self.update_buff_act:  # 更新buff
            self.update_buff(target=target, our=our)  # 更新buff
        else:  # 不更新buff
            self.update_buff_act = True  # 开启更新buff

    def __imp_extra_attr(self, our):
        """导入额外属性"""
        # 这里的额外属性最初是: {"名字": {属性名称: 属性值}}
        # print("导入额外属性：", self.attributes_extra)
        for attr_name, attrdict in self.attributes_extra.items():
            for name, attr in attrdict.items():
                if name in our.keys():
                    our[name] += attr
                else:
                    our[name] = attr
        # 这里的额外属性现在是: {属性名称: 属性值}
        for name, attr in self.equip.attributes.items():
            if name in self.equip_special_attr.keys():
                self.equip_special_attr[name] += attr
            elif name in our.keys():
                our[name] += attr
            else:
                our[name] = attr

    def charge_attribute(self, name, attribute=None, remove=False):
        """增加额外属性
        name: 属性代号
        attribute: 属性值:{属性名称: 属性值}
        remove: 是否删除指定的额外属性值"""
        if remove:  # 减少额外属性值
            # print(name, attribute, remove)
            if name not in self.attributes_extra.keys():  # 不存在额外属性值
                return  # 无效属性
            self.attributes_extra.pop(name)  # 减少额外属性值
            return  # 无效属性
        if attribute is None:  # 增加额外属性值
            return  # 无效属性

        self.attributes_extra[name] = attribute  # 添加额外属性值,注：这里是如果传入相同，会覆盖
        # print("添加额外属性：", self.attributes_extra)

    def use_passive(self, target=None, our=None, passive_type=None, temp=None):
        """使用被动技能"""
        # 使用被动技能
        self.skills[self.skills_name_fu2["被动"]].use(target=target, our=our, passive_type=passive_type, temp=temp)
        temp["tag"].append("被动")

    def use_equip(self, target=None, our=None, equip_type=None, temp=None):
        """使用武器"""
        # 使用装备
        self.equip.use(target=target, our=our, equip_type=equip_type, temp=temp)
        temp["tag"].append("武器")

    def get_name(self):
        """获取角色名称"""
        return self.name

    def get_role(self):
        """获取角色类型"""
        return self.role

    def get_story(self):
        """获取角色故事"""
        return self.story

    def get_attributes(self):
        """获取角色属性"""
        return self.attributes

    def get_skill(self):
        """获取角色技能列表"""
        return self.skill_list

    def get_data(self):
        """获取角色数据"""
        return {
            "name": self.name,
            "name_base": self.name_base,
            "role": self.role,
            "story": self.story,
            "attributes": self.attributes,
            "image": self.image.image_temp,
            "camp": self.camp,
            "role_type": self.role_type,
            "axle": self.axle,
            "axle_yu": self.axle_yu,
            "skills": self.skills.keys()
        }

    def run_choose_command(self):
        """选择命令"""
        self.choose_command(self.get_data())

    @staticmethod
    def dispose_name(name):
        """获取角色称号与真名"""
        if "】" in name:
            ix = name.index("】")
            return {"name_des": name[:ix+1], "name_base": name[ix+1:]}
        else:
            return {"name_des": "【】", "name_base": name}
