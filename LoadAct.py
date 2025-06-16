from mods.CodCode import loadJS
import json


class LoadAct:
    def __init__(self):
        """这个用于加载角色"""
        with open("resources/Act/path.json", 'r', encoding='utf-8') as f:
            self.path = json.load(f)  # 角色的文件路径
        print(self.path)

        self.load = loadJS.LoadJS()  # 加载工具类
        self.data = dict()  # 角色数据

    def run(self):
        """运行"""
        for key, value in self.path.items():
            print(key, value)
            print(self.load.load(value))


if __name__ == '__main__':
    loadact = LoadAct()
    loadact.run()

