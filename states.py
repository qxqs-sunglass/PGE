buff_dict_reality = {
    "【罪星】": {"name": "【罪星】", "turn": 3, "superposition": 1, "active": True, "type": "001", "dis": True},
    "【黑子】": {"name": "【黑子】", "turn": 3, "superposition": 1, "active": True, "type": "001", "dis": True},
    "【还魂】": {"name": "【还魂】", "turn": 1, "superposition": 1, "active": False, "type": "001", "dis": True},
    "【丰收】": {"name": "【丰收】", "turn": 2, "superposition": 1, "active": True, "type": "001", "dis": True},
    "【暴击率】": {"name": "【暴击率】", "turn": 1, "superposition": 1, "active": True, "type": "002", "num": 10, "dis": False},
    "【暴击伤害】": {"name": "【暴击伤害】", "turn": 1, "superposition": 1, "active": True, "type": "002", "num": 10, "dis": False},
    "【攻击力】": {"name": "【攻击力】", "turn": 1, "superposition": 1, "active": True, "type": "002", "num": 10, "dis": False},
    "【增伤】": {"name": "【增伤】", "turn": 1, "superposition": 1, "active": True, "type": "002", "num": 10, "dis": False},
    "【均衡】": {"name": "【均衡】", "turn": 1, "superposition": 1, "active": False, "type": "004", "dis": False}
}
""" 效果标签
001: 状态 -> 传入target[buff]，our[buff]项即可
002: 效果 -> 传入target[buff]，our[buff]项即可
003: 负面状态(具有持续伤害) -> 传入target[buff]，our[buff]项即可
004: 特殊效果 -> 传入our[buff]项即可
name: 状态名
turn: 持续回合数
superposition: 叠加次数
active: 是否减少回合数
type: 效果类型
num: 效果值
dis: 是否显示"""


def 还魂(target, our):
    """还魂: 001"""
    our["kr"] += 20


def 罪星(target, our):
    """罪星: 001"""
    target["vl"] += 20


def 黑子(target, our):
    """黑子: 001"""
    target["vl"] += 20


def 丰收(target, our):
    """丰收: 001"""


def 均衡(our):
    """均衡: 004"""
    if our["at"] > 600:
        temp = round((our["at"] - 600) * 0.5)  # 计算出削减的伤害
        our["at"] = temp + 600  # 削减伤害
    elif our["at"] > 1000:
        temp = round((our["at"] - 1000) * 0.3)  # 计算出削减的伤害
        our["at"] = temp + 1000  # 削减伤害
    if our["df"] > 300:
        temp = round((our["df"] - 300) * 0.3)  # 计算出削减的防御
        our["df"] = temp + 300  # 削减防御
    if our["kd"] > 100:
        temp = round((our["kd"] - 100) * 0.5)  # 计算出削减的暴击伤害
        our["kd"] = temp + 100  # 削减暴击伤害
    if our["ids"] > 100:
        temp = round((our["ids"] - 100) * 0.6)  # 计算出削减的增伤
        our["ids"] = temp + 100  # 削减增伤


def kr_buff(our, buff):
    """暴击率buff: 002"""
    buff["num"] = our["superposition"] * buff["num"]
    our["kr"] += buff["num"]


def kd_buff(our, buff):
    """暴击伤害: 002"""
    buff["num"] = buff["superposition"] * buff["num"]
    our["kd"] += buff["num"]


def at_buff(our, buff):
    """攻击buff: 002"""
    buff["num"] = buff["superposition"] * buff["num"]
    our["at"] += buff["num"]


def ids_buff(our, buff):
    """增伤buff: 002"""
    buff["num"] = buff["superposition"] * buff["num"]
    our["ids"] += buff["num"]


buff_dict_command = {
    "【还魂】": 还魂, "【丰收】": 丰收, "【罪星】": 罪星, "【黑子】": 黑子,
    "【暴击率】": kr_buff, "【暴击伤害】": kd_buff,
    "【攻击力】": at_buff, "【增伤】": ids_buff
}
