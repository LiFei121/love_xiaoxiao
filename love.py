import tkinter as tk
from tkinter import font as tkfont
import random
import threading
import time

# ═══════════════════════════════════════════════════════════════
# 💕 配置区域 - 可以自定义内容
# ═══════════════════════════════════════════════════════════════

# 温馨提示语列表
messages = [
    "好好爱自己", "保持好心情", "金榜题名", "每天都要元气满满", "想你了",
    "天冷了，多穿衣服", "别熬夜", "梦想成真", "期待下一次见面", "多喝水哦~",
    "今天过得开心", "愿所有烦恼都消失", "保持微笑呀", "顺顺利利", "记得吃水果",
    "你最棒了", "平安喜乐", "万事胜意", "好运连连", "做自己的小太阳"
]

# 精选渐变配色方案（背景色，文字色）
color_schemes = [
    ("#FF6B9D", "#FFFFFF"),  # 粉红渐变
    ("#C56CD6", "#FFFFFF"),  # 紫色渐变
    ("#4FACFE", "#FFFFFF"),  # 天蓝渐变
    ("#43E97B", "#FFFFFF"),  # 绿色渐变
    ("#FA709A", "#FFFFFF"),  # 玫瑰渐变
    ("#FFD26F", "#5A4A42"),  # 金色渐变
    ("#6DD5FA", "#FFFFFF"),  # 海洋渐变
    ("#FFA8A8", "#FFFFFF"),  # 珊瑚渐变
    ("#A8EDEA", "#2C5F6F"),  # 薄荷渐变
    ("#FBC2EB", "#FFFFFF"),  # 梦幻渐变
]

# 弹窗设置
POPUP_WIDTH = 260
POPUP_HEIGHT = 100
POPUP_INTERVAL = 0.2  # 每隔多少秒创建新弹窗
MAX_POPUPS = 100  # 同时显示的最大弹窗数
POPUP_LIFETIME = 10  # 弹窗存活时间（秒）

# 当前活跃的弹窗列表
active_popups = []


# ═══════════════════════════════════════════════════════════════
# 🎨 核心功能
# ═══════════════════════════════════════════════════════════════

def create_popup():
    """创建一个带有动画效果的美观弹窗"""
    
    # 限制弹窗数量
    if len(active_popups) >= MAX_POPUPS:
        return
    
    root = tk.Toplevel()
    root.overrideredirect(True)  # 无边框窗口
    root.attributes('-topmost', True)  # 置顶显示
    root.attributes('-alpha', 0.0)  # 初始透明度为0（用于淡入效果）
    
    # 随机设置窗口位置
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = random.randint(100, screen_width - POPUP_WIDTH - 100)
    y = random.randint(80, screen_height - POPUP_HEIGHT - 100)
    root.geometry(f"{POPUP_WIDTH}x{POPUP_HEIGHT}+{x}+{y}")
    
    # 随机选择提示语和配色
    msg = random.choice(messages)
    bg_color, fg_color = random.choice(color_schemes)
    
    # 创建主框架（带圆角效果的模拟）
    main_frame = tk.Frame(root, bg=bg_color, bd=0)
    main_frame.pack(fill="both", expand=True, padx=3, pady=3)
    
    # 添加内部框架（模拟内边距）
    inner_frame = tk.Frame(main_frame, bg=bg_color, bd=0)
    inner_frame.pack(fill="both", expand=True, padx=15, pady=12)
    
    # 创建心形图标（使用emoji）
    icon_label = tk.Label(
        inner_frame, 
        text="💕", 
        font=("Segoe UI Emoji", 16), 
        bg=bg_color, 
        fg=fg_color
    )
    icon_label.pack(side="top", pady=(0, 5))
    
    # 创建消息标签
    message_label = tk.Label(
        inner_frame,
        text=msg,
        font=("微软雅黑", 13, "bold"),
        bg=bg_color,
        fg=fg_color,
        wraplength=220,
        justify="center"
    )
    message_label.pack(side="top", fill="both", expand=True)
    
    # 创建关闭按钮
    close_btn = tk.Label(
        main_frame,
        text="✕",
        font=("Arial", 10, "bold"),
        bg=bg_color,
        fg=fg_color,
        cursor="hand2"
    )
    close_btn.place(x=POPUP_WIDTH-25, y=5, width=20, height=20)
    
    # 绑定关闭事件
    def close_popup(event=None):
        fade_out(root)
    
    close_btn.bind("<Button-1>", close_popup)
    message_label.bind("<Button-1>", close_popup)
    
    # 鼠标悬停效果
    def on_enter(event):
        close_btn.config(font=("Arial", 12, "bold"))
    
    def on_leave(event):
        close_btn.config(font=("Arial", 10, "bold"))
    
    close_btn.bind("<Enter>", on_enter)
    close_btn.bind("<Leave>", on_leave)
    
    # 添加到活跃列表
    active_popups.append(root)
    
    # 淡入动画
    fade_in(root)
    
    # 设置自动关闭
    root.after(int(POPUP_LIFETIME * 1000), lambda: fade_out(root))


def fade_in(window, alpha=0.0):
    """淡入动画效果"""
    if alpha < 0.95:
        alpha += 0.05
        window.attributes('-alpha', alpha)
        window.after(20, lambda: fade_in(window, alpha))
    else:
        window.attributes('-alpha', 0.95)


def fade_out(window, alpha=0.95):
    """淡出动画效果"""
    try:
        if alpha > 0:
            alpha -= 0.05
            window.attributes('-alpha', alpha)
            window.after(20, lambda: fade_out(window, alpha))
        else:
            if window in active_popups:
                active_popups.remove(window)
            window.destroy()
    except:
        pass  # 窗口已经被关闭


def start_popups():
    """持续创建弹窗"""
    while True:
        try:
            create_popup()
        except:
            pass
        time.sleep(POPUP_INTERVAL)


# ═══════════════════════════════════════════════════════════════
# 🚀 程序入口
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # 创建主窗口
    main_root = tk.Tk()
    main_root.withdraw()  # 隐藏主窗口
    main_root.title("Love Message")
    
    # 启动弹窗线程
    thread = threading.Thread(target=start_popups, daemon=True)
    thread.start()
    
    # 运行主循环
    main_root.mainloop()