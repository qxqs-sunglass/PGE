import time
import os

def get_time():
    """获取程序运行时间"""
    time_str = time.thread_time()
    return time_str


def writelog(message, flag=False, timeshow=True, cmd_show=False):
    """日志记录函数"""
    if flag:
        # 清空控制台输出
        os.system('cls')
    if timeshow:
        message += f"        t：{get_time()}"
    if cmd_show:
        print(message)
    message += '\n'
    with open('logs/log.txt', 'a', encoding='utf-8') as f:
        f.write(message)
        f.close()


def resetlog():
    """日志重置函数"""
    with open('logs/log.txt', 'w', encoding='utf-8') as f:
        f.write(f'日期：{get_time()}：\n')
        f.close()
