from modules.module_act import ActTemplate
import CodCode


class LoadAct:
    def __init__(self):
        """这个用于加载角色"""
        self.path = "resources/Act/Suxiao.cod"  # 角色的文件路径
        self.special_str = [
            "(", ")", "[", "]", "{", "}",
            ":", ",", ".",
            "==", "!=", ">", "<", ">=", "<=", "=",
            "and", "or", "not", "in", "is",
            "main", "def"
        ]  # 特殊字符串
        # 各种字符串
        self.call_str = [
            "call",
            "callAct",
            "callEquip",
            "callSkill",
            "system",
            "extra",
        ]  # 所有字符串
        self.system_str = [
            "name", "attributes", "intro", "description",
            "name_base"
        ]  # 系统字符串
        self.extra_str = []  # 额外字符串

        self.system_dict = {
            "name"
        }  # 系统功能字典
        self.extra_dict = {}  # 额外功能字典
        self.call_dict = {
            "system": self.system_dict,
            "extra": self.extra_dict
        }  # 调用功能字典映射
        self.top_dict = {
            "call": self.call_dict,  # 调用功能字典
            "def": self.def_func,  # 定义函数功能字典
            "\"": self.quote_func,  # 字符串定义
        }  # 顶层字典
        self.all_str = self.call_str + self.system_str + self.extra_str + self.special_str  # 所有字符串
        # 各种计数器
        self.bracket_small_count = 0  # 小括号计数器
        self.bracket_middle_count = 0  # 中括号计数器
        self.bracket_big_count = 0  # 大括号计数器，各种括号计数器用于判断代码块,有左括号则计数加1,有右括号则计数减1,为0时表示代码块结束
        self.quota_count = 0  # 引号计数器，用于判断字符串是否结束
        self.def_count = 0  # def计数器 用于判断是否进入函数定义
        self.now_domain = []  # 当前域块，用于判断代码块

    def init(self):
        """初始化"""
        temp = []
        with open(self.path, "r", encoding="utf-8") as f:  # 打开文件
            # 读取文件内容
            for line in f:
                if line != "\n" and line != "\r\n":
                    if "#" in line:
                        line = line[:line.index("#")]  # 删除注释
                    line = line.strip()
                    temp.append(line)
            f.close()
        # 解析文件内容
        data = []
        for line in temp:
            # 解析属性
            print(1, line)
            s = ""
            t = []
            for msg in line:
                """在这里解析属性"""
                s += msg
            print(3, t)
            data.append(t)
        print(4, data)

    def run(self):
        """测试时使用"""

    def def_func(self, func_name, var_list):
        """定义函数"""
        print(func_name, var_list)
        self.now_domain.append(func_name)
        self.def_count += 1

    def def_end(self):
        """函数定义结束"""
        self.now_domain.pop()
        self.def_count -= 1
        if self.def_count < 0:
            return {"error": "domain error: def_count < 0!!!"}

    def quote_func(self):
        """字符串定义"""
        if self.quota_count == 0:
            pass
        else:
            pass


if __name__ == '__main__':
    loadact = LoadAct()
    loadact.init()
    loadact.run()

