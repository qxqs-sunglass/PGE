from .AllStr import *
from copy import deepcopy


class LoadCC:
    def __init__(self):
        """加载文件模块"""
        # 各种计数器
        self.bracket_small_count = 0  # 小括号计数器
        self.bracket_middle_count = 0  # 中括号计数器
        self.bracket_big_count = 0  # 大括号计数器，各种括号计数器用于判断代码块,有左括号则计数加1,有右括号则计数减1,为0时表示代码块结束
        self.quota_count = 0  # 引号计数器，用于判断字符串是否结束
        self.def_count = 0  # def计数器 用于判断是否进入函数定义
        # 各种状态
        self.now_domain = {}  # 当前域块，用于判断代码块
        self.region_dict = {}  # 代码块字典，用于存储代码块信息
        # {"region_name": {"region_content": "", "region_type": "", "region_start": 0, "region_end": 0}}

    def load(self, path) -> dict:
        """加载文件"""
        # 各种计数器
        self.bracket_small_count = 0  # 小括号计数器
        self.bracket_middle_count = 0  # 中括号计数器
        self.bracket_big_count = 0  # 大括号计数器，各种括号计数器用于判断代码块,有左括号则计数加1,有右括号则计数减1,为0时表示代码块结束
        self.quota_count = 0  # 引号计数器，用于判断字符串是否结束
        self.def_count = 0  # def计数器 用于判断是否进入函数定义
        # 各种状态
        self.now_domain = {}  # 当前域块，用于判断代码块
        self.region_dict = {}  # 代码块字典，用于存储代码块信息
        # {"region_name": {"region_content": "", "region_type": "", "region_start": 0, "region_end": 0}}
        # 加载文件
        load_file = open(path, "r", encoding="utf-8")
        code = load_file.read()
        load_file.close()
        # 解析代码
        self.parse_code(code)
        return {"temp": "temp"}

    def parse_code(self, code) -> None:
        """解析代码"""
        region_name = ["o"]  # 代码块
        region_content = []  # 代码块内容
        region_type = ""  # 代码块类型
        region_start = 0  # 代码块开始位置
        region_end = 0  # 代码块结束位置
        # 遍历代码
        temp = []
        for line in code.split("\n"):
            # 跳过空行
            if not line.strip():
                continue
            print(line)
            for msg in line.split():
                if "#" in msg:
                    break
                print("字符：", msg)
                temp.append(msg)
                # 解析消息
        print("temp: ", temp, len(temp))
        print("1 ", region_name)
        print("2 ", region_content)
        print("3 ", region_type)
        print("4 ", region_start)
        print("5 ", region_end)
        self.region_dict[region_name[0]] = {
            "region_content": region_content,  # 代码块内容
            "region_type": region_type,  # 代码块类型
            "region_start": region_start,  # 代码块开始位置
            "region_end": region_end  # 代码块结束位置
        }

    def parse_msg(self, msg: str) -> list:
        """解析消息"""
        # 解析字符串
        temp = []
        for s in SPECIAL_STR:
            if not msg.startswith(s):
                continue
            t = msg.split(s)
            for m in t:
                temp.append(m)
                temp.append(s)
            temp.pop(-1)
            break
        return temp

    def bracket_count(self, s: str) -> bool:
        """括号计数
        左括号则计数加1,有右括号则计数减1,为0时表示代码块结束"""
        if s == "(":
            self.bracket_small_count += 1
            return True
        elif s == ")":
            self.bracket_small_count -= 1
            return False
        elif s == "[":
            self.bracket_middle_count += 1
            return True
        elif s == "]":
            self.bracket_middle_count -= 1
            return False
        elif s == "{":
            self.bracket_big_count += 1
            return True
        elif s == "}":
            self.bracket_big_count -= 1
            return False

