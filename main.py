from modules.module_button import ButtonModule
from modules.module_text import TextModule
from view_act import ViewAct
from import_act import ImportAct
from improt_eqiup import ImportEquip
from setting import Settings
from witelog import writelog, resetlog
from game import GameMain
from game_choose import GameChoose
from import_image import ImportImage
from pygame import mixer
import tkinter


class Main(Settings):
    def __init__(self):
        super().__init__()
        # 创建窗口
        self.root = tkinter.Tk()
        self.root.title(self.game_title)
        self.root.geometry(self.screen)
        self.root.resizable(False, False)  # 禁止调整窗口大小
        # 基础模块
        # 导入角色&武器模块
        self.import_act = None  # 导入角色模块
        self.import_equip = None  # 导入武器模块
        # 浏览角色模块
        self.view_act = None  # 浏览角色模块
        # 游戏模块
        self.game_main = None  # 游戏模块
        # 游戏选择模块
        self.game_choose = None  # 游戏选择模块
        # 设置模块
        self.setting_act = None  # 设置模块
        # 图片模组
        self.images = None  # 图片模块
        # 文本模块
        self.bin_text = TextModule(self.root, (5, 700), self.bin)  # 版本信息
        # 按钮模块
        self.view_btn = None  # 浏览角色按钮
        self.game_btn = None  # 开始游戏按钮
        self.setting_btn = None  # 设置按钮
        # 其他
        self.actors = None  # 角色字典：{"name[中文]": Actor}
        self.equips = None  # 武器字典：{"name[中文]": Equip}
        self.game_actor_temp = {"A": {"主战": "【执剑】苏晓", "助战": "【星主】苍居宫微"},
                                "B": {"主战": "【葬土之神】域圻", "助战": "【神明造物002】共"}}  # 游戏选中角色
        self.game_equip_temp = {"主战A": "至死方休",
                                "主战B": "于人之法",
                                "助战A": "樱弥散",
                                "助战B": "测试用"}  # 游戏选中武器
        self.game_talent_temp = ["auto", "auto"]  # 双方游戏天赋由系统自动选择

    def run(self):
        # 初始化
        self.init()
        # 启动主循环
        self.root.mainloop()

    def init(self):
        # 重置日志
        writelog("窗口初始化完成", cmd_show=True)
        resetlog()
        self.init_sprite()
        writelog("实例初始化完成", cmd_show=True)
        # 初始化画面
        self.init_draw()
        writelog("画面初始化完成", cmd_show=True)
        self.init_all()
        writelog("所有模块初始化完成", cmd_show=True)
        writelog("所有模块初始化完成", True, False, cmd_show=True)
        writelog(f"当前版本：{self.bin}", timeshow=False, cmd_show=True)

    def init_sprite(self):
        """初始化实例"""
        mixer.init()  # 初始化音效
        writelog("音效初始化完成")
        # 设置背景音乐
        mixer.music.set_volume(1.0)  # 设置音量
        mixer.music.load(self.game_music)  # 加载背景音乐
        mixer.music.play(-1)  # 播放背景音乐
        # 导入图片模块
        self.images = ImportImage()  # 图片模块
        writelog("图片模块初始化完成", cmd_show=True)
        # 导入角色模块
        self.import_act = ImportAct()  # 导入角色模块
        self.actors = self.import_act.actors  # 角色字典
        writelog("导入角色模块初始化完成", cmd_show=True)
        # 导入武器模块
        self.import_equip = ImportEquip()  # 导入武器模块
        self.equips = self.import_equip.equips  # 武器字典
        writelog("导入武器模块初始化完成", cmd_show=True)
        # 创建浏览模块
        self.view_act = ViewAct(self.root, self.actors)  # 浏览角色模块
        writelog("浏览角色模块初始化完成", cmd_show=True)
        # 创建游戏选择模块
        self.game_choose = GameChoose(self.root, self)  # 游戏选择模块
        writelog("游戏选择模块初始化完成", cmd_show=True)
        # 创建游戏模块
        self.game_main = GameMain(self, self.root, self.actors, self.equips)
        writelog("游戏模块初始化完成", cmd_show=True)
        # 创建按钮模块
        writelog("按钮模块初始化完成", cmd_show=True)
        self.game_btn = ButtonModule(self.root, (750, 350), "开始游戏", command=self.game_choose_show,
                                     wid_hei=[150, 50],
                                     image=self.images.get_image("but1.png"))  # 开始游戏按钮
        self.view_btn = ButtonModule(self.root, (700, 450), "预览角色", command=self.view_act_show,
                                     wid_hei=[150, 50],
                                     image=self.images.get_image("but1.png"))  # 浏览角色按钮
        writelog("按钮模块初始化完成", cmd_show=True)
        self.setting_btn = ButtonModule(self.root, (650, 550), "设置", command=self.setting_act_show,
                                        wid_hei=[150, 50],
                                        image=self.images.get_image("but1.png"))  # 设置按钮

    def init_all(self):
        """初始化所有模块"""
        self.import_act.init(self, self.root)  # 导入角色模块初始化
        self.import_equip.init(self, self.root)  # 导入武器模块初始化
        self.view_act.init()  # 浏览角色模块初始化

    def init_draw(self):
        self.draw()

    def draw(self):
        self.draw_btn()
        self.draw_text()

    def draw_btn(self):
        self.view_btn.draw()  # 浏览角色按钮
        self.game_btn.draw()  # 开始游戏按钮
        self.setting_btn.draw()  # 设置按钮

    def draw_text(self):
        self.bin_text.draw()

    def view_act_show(self):
        self.view_act.show()

    def undraw(self):
        self.game_btn.undraw()
        self.setting_btn.undraw()
        self.view_btn.undraw()

    def close(self):
        """关闭窗口"""
        self.root.withdraw()

    def open(self):
        """打开窗口"""
        self.root.deiconify()

    def game_choose_show(self):
        self.close()
        self.game_choose.open()

    def game_main_show(self):
        """开始游戏"""
        self.close()
        self.game_main.open()

    def setting_act_show(self):
        pass


if __name__ == '__main__':
    m = Main()
    m.run()
