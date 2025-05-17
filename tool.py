from states import buff_dict_command, buff_dict_reality
from copy import deepcopy
import random
import witelog


def formulate_damage(target, our, damage=0):
    """通用伤害计算器"""
    if damage == 0:
        damage = our["at"]
    # print("我方攻击力:", damage)
    # print("我方攻击力:", our["at"])
    # print("敌方防御力:", target["df"])
    damage = damage - target["df"]  # 减防
    # 伤害倍率
    # print("我方伤害倍率:", our["dr"])
    dr = our["dr"]/100
    damage = round(damage * (1 + dr))  # 伤害倍率
    # 增伤
    # print("我方增伤:", our["ids"])
    ids = our["ids"]/100
    damage = round(damage * (1 + ids))  # 增伤
    # 触发暴击
    # print("暴击率:", our["kr"])
    # print("触发暴击倍率:", our["kd"])
    if random.randint(0, 100) < our["kr"]:  # 触发暴击率
        # print("触发暴击")
        kd = our["kd"]/100
        damage = round(damage * (1+kd))  # 触发暴击倍率
        witelog.writelog("触发暴击")
        our["kr_count"] = "触发暴击"
    # 易伤区
    # print("敌方易伤:", target["vl"])
    vl = (target["vl"]/100)
    damage = round(damage * (1 + vl))  # 易伤
    # 额外乘区
    # print("我方额外乘区:", our["other"])
    other = our["other"]/100
    damage = round(damage * (1 + other))  # 额外乘区
    # 除抗性区
    # print("敌方抗性:", target["rt"])
    if target["rt"] <= 0:
        damage = round(damage / 1)  # 无抗性
    else:
        damage = round(damage / target["rt"])  # 除抗性
    # 减伤
    # print("敌方减伤:", target["rh"])
    damage = round(damage - target["rh"])  # 减伤
    # 免伤
    # print("敌方免伤:", target["ha"])
    damage = round(damage * (1 - target["ha"]))  # 免伤
    if damage < 0:
        damage = 0
    # print("最终伤害:", damage, "\n---------------------------")
    return damage


def main_num_formulate_sub(our, adv=True):
    """主战和助战的技能点数减少"""
    if adv:
        if our["main_num"] < 1:
            return {"error": "技能点不足--->"}
        our["main_num"] -= 1  # 技能消耗
    return {"success": "技能点消耗成功"}


def helper_num_formulate_sub(our, adv=True):
    if adv:
        if our["helper_num"] < 1:
            return {"error": "技能点不足--->"}
        our["helper_num"] -= 1  # 技能消耗
    return {"success": "技能点消耗成功"}


def main_num_formulate_add(our, adv=True):
    """主战的技能点数增加"""
    if adv:
        if our["main_num"] >= our["main_num_max"]:
            return {"success": "技能点已满"}
        our["main_num"] += 1  # 技能增加
    return {"success": "技能点增加成功"}


def helper_num_formulate_add(our, adv=True):
    if adv:
        if our["helper_num"] >= our["helper_num_max"]:
            return {"success": "技能点已满"}
        our["helper_num"] += 1  # 技能增加
    return {"success": "技能点增加成功"}


def use_ultimate_formulate(our, energy_cost):
    """使用终极技能"""
    if our["energy"] >= energy_cost:
        our["energy"] -= energy_cost  # 能量消耗
        return {"success": "终极技能使用成功"}
    else:
        return {"error": "能量不足--->"}


def energy_formulate_add(our, energy_add, adv=True):
    """能量增加"""
    if our["energy"] + energy_add + our["re"] > our["energy_max"] and adv:
        our["energy"] = our["energy_max"]  # 能量上限
    elif our["energy"] + energy_add + our["re"] < our["energy_max"] and adv:
        our["energy"] += energy_add + our["re"]  # 能量增加
    return {"success": "能量增加成功"}


def get_buff(buff_name, **kwargs):
    """获取buff"""
    buff = deepcopy(buff_dict_reality[buff_name])
    if "value" in kwargs:
        for name in kwargs["value"]:
            buff[name] = kwargs["value"][name]
    return buff


def formulate_buff(target, our):
    """通用buff计算器"""
    # 计算我方buff
    for temp in [target["buff"], our["buff"]]:
        for buff in temp.values():
            if buff["type"] == "001":  # 状态buff
                buff_dict_command[buff["name"]](our, buff)  # 计算buff
            elif buff["type"] == "002":  # 属性buff
                buff_dict_command[buff["name"]](our, buff)  # 计算buff
            elif buff["type"] == "003":  # 负面buff
                pass  # 负面buff暂时不做处理
    return {"success": "buff计算成功"}


def formulate_special_buff(target, our):
    """通用特殊buff计算器"""
    for buff in our["buff"]:
        if buff["type"] == "004":  # buff
            buff_dict_command[buff["name"]](our)
            buff_dict_command[buff["name"]](target)
    return {"success": "buff计算成功"}


