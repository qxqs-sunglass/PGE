from mods.CodCode import loadCC


class LoadAct:
    def __init__(self):
        """这个用于加载角色"""
        self.path = "resources/Act/Suxiao.cod"  # 角色的文件路径
        self.load = loadCC.Load()  # 加载工具类
        self.data = self.load.load(self.path)  # 加载角色数据

    def run(self):
        """运行"""
        print(self.data)


if __name__ == '__main__':
    loadact = LoadAct()
    loadact.run()

