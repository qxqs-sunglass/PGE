from bin.axle_dicts import axle_dicts
from modules.module_text import TextModule
from modules.module_image import ImageModule
import tkinter


class AxleActTemplate:
    def __init__(self):
        """此类为行动轴事件（召唤）模板类"""
        self.user = None  # 用户
        self.name = None  # 名称
        self.description = ""  # 描述
        self.attributes_name = ["at", "df", "kr", "kd",
                                "sp", "rt", "ids", "vl",
                                "rh", "ha", "dr", "re"]  # 属性名称
        self.attributes = {}  # 属性
        self.events = {
            "use_evnet": self.use,
            "axle_event": self.do_event,
            "init_event": self._init_event
        }  # 事件
        # 以下为辅助属性
        self.axle = 0  # 所属行动轴
        self.axle_yu = 0  # 余下行动力
        self.axle_extra = 0  # 额外行动力
        # 需要
        self.clear_axle = True  # 是否删除当前行动轴
        self.event_global = False  # 是否全局事件
        self.event_type = []  # 事件类型
        # 若是需要触发必须在do_event方法中，调用method["add_use"](self)方法
        self.screen = None

    def init(self, screen):
        """此处的初始化包括了窗口的初始化、数据导入、UI绘制、事件绑定等"""
        self.load_data()
        self.init_screen(screen)
        self.init_ui()

    def init_ui(self):
        """初始化UI"""
        # 窗口初始化

        # 在这里写UI初始化代码

        # 显示
        self.draw()

    def init_screen(self, screen):
        """初始化窗口"""
        self.screen = tkinter.Toplevel(screen)  # 创建窗口
        self.screen.title(self.name)  # 设置窗口标题
        self.screen.geometry("300x200")
        self.screen.resizable(False, False)  # 禁止缩放
        self.screen.protocol("WM_DELETE_WINDOW", self.close_screen)  # 关闭窗口时调用close_screen方法
        self.screen.withdraw()  # 隐藏窗口

    def close_screen(self):
        """关闭窗口, 已与窗口的关闭按钮(事件)绑定"""
        self.screen.withdraw()  # 隐藏窗口

    def draw(self):
        """绘制窗口
        在这个方法中，需要调用TextModule和ImageModule的draw方法"""

    def display(self):
        """显示窗口
        注：此方法会打开一个新的窗口，并在窗口中显示当前模板的UI。
        只需要调用此方法即可显示窗口"""
        self.screen.deiconify()  # 显示窗口

    def load_data(self):
        """导入数据"""
        for key in self.attributes_name:
            if key in axle_dicts[self.name]:
                self.attributes[key] = axle_dicts[self.name][key]
            else:
                self.attributes[key] = 0

    def use(self, target, our, temp, actor):
        """使用技能"""
        pass

    def _init_event(self, method):
        """初始化事件
        这里传入一个self的合法方法，以便于调用其方法"""

    def do_event(self, method):
        """执行事件
        这里传入一个self的游戏对象，以便于调用其方法"""
        pass

    def get_name(self):
        """获取名称"""
        return self.name

    def get_description(self):
        """获取描述"""
        return self.description


class WorldAxleTemplate(AxleActTemplate):
    def __init__(self):
        """此类为世界行动轴事件（召唤）模板类"""
        super().__init__()

    def _init_event(self, method):
        """初始化事件"""
        method["add_use"](self)  # 绑定触发事件

    def do_event(self, method):
        """执行事件"""
        method["sub_use"](self)
        method["exchange_axle"]()  # 切换大世界
        method["helper_num_formulate_add"]()




