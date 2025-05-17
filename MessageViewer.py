import tkinter as tk


class MessageViewer:
    def __init__(self, root, position, size):
        """初始化消息显示组件"""
        self.root = root
        self.pos = position
        self.size = size

        # 创建一个 Frame 容器，用于放置 Text 和 Scrollbar
        self.frame = tk.Frame(self.root)
        self.frame.place(x=self.pos[0], y=self.pos[1], width=self.size[0], height=self.size[1])

        # 创建 Text 控件用于显示消息
        self.text = tk.Text(self.frame, height=7, width=50, wrap=tk.WORD, state="disabled")  # 设置为不可编辑
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 创建滚动条并绑定到 Text 控件
        self.scrollbar = tk.Scrollbar(self.frame, command=self.text.yview, width=15)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.config(yscrollcommand=self.scrollbar.set)

        self.tag_config = {
            "info": {"foreground": "black"},  # 信息
            "warning": {"foreground": "orange"},  # 警示
            "error": {"foreground": "red"},  # 错误
            "tick": {"foreground": "green"},  # 触发
            "cross": {"foreground": "red"},  # 错误
            "use": {"foreground": "blue"}  # 使用
        }
        for tag, config in self.tag_config.items():
            self.text.tag_configure(tag, **config)

    def draw(self):
        """绘制消息显示组件"""
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def clear(self):
        """清空消息显示组件"""
        self.text.config(state="normal")
        self.text.delete(1.0, tk.END)
        self.text.config(state="disabled")

    def undraw(self):
        """隐藏消息显示组件"""
        self.text.pack_forget()
        self.scrollbar.pack_forget()

    def add_message(self, message, tag="info"):
        """添加一条消息到消息显示组件"""
        self.text.config(state="normal")  # 允许编辑
        if tag in self.tag_config:
            self.text.insert(tk.END, message + '\n', tag)
        else:
            self.text.insert(tk.END, message + '\n')
        self.text.see(tk.END)  # 自动滚动到底部
        self.text.config(state="disabled")  # 禁止编辑
        self.root.update()
