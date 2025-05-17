import json


class Settings:
    def __init__(self):
        with open("bin/base.json", "r", encoding="utf-8") as f:  # 读取基本设置
            self.data = json.load(f)
        self.screen_width = self.data["width"]
        self.screen_height = self.data["height"]
        self.game_title = self.data["game_title"]  # 标题
        with open("bin/bin.json", "r", encoding="utf-8") as f:  # 读取版本号
            self.bin_data = json.load(f)
            f.close()
        self.bin = self.bin_data["bin"]  # 版本号
        self.game_music = self.data["game_music"]  # 背景音乐
        self.screen = f"{self.screen_width}x{self.screen_height}"






