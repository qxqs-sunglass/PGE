from EquipResource.equips import *
from witelog import writelog
import json


class ImportEquip:
    def __init__(self):
        """导入装备实例"""
        with open('bin/ReadEquipsList.json', 'r', encoding='utf-8') as f:
            self.equips_dict = json.load(f)  # 装备路径数据
            f.close()
        writelog('装备路径数据加载成功')
        self.equip = Equips()
        self.equips = {}

    def init(self, ai, screen):
        """初始化,
        init需要单独调用, 因为init_equips需要screen参数"""
        for equip_name, equip_path in self.equips_dict.items():
            equip = self.equip.equips_dict[equip_name](equip_path)  # 实例化装备模板
            equip.init(ai, screen)  # 初始化装备
            self.equips[equip_name] = equip  # 装备字典
            writelog(f'{equip_name}装备加载成功')
        self.equips["测试用"] = 测试用()
        self.equips["测试用"].init(ai, screen)
        writelog('装备初始化成功')

