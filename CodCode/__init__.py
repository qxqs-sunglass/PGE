from load import *

__version__ = "1.0.0"
__author__ = "@bilibili: 秋天会有下雪天, @PGE项目组"
print("当前CodC版本：", __version__)

CALL_STR = [
    "call",
    "callAct",
    "callEquip",
    "callSkill",
    "system",
    "extra",
]  # 所有字符串

__all__ = ["Load", "__version__", "__author__", "CALL_STR"]

