import tkinter as tk
from tkinter import filedialog

def select_directory():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        selected_directory_label.config(text="選擇的目錄路徑：" + folder_selected)
        next_button.config(state=tk.NORMAL)
    else:
        selected_directory_label.config(text="尚未選擇目錄")
        next_button.config(state=tk.DISABLED)

def next_step():
    introduction_label.config(text="請選擇EXCEL檔案", bg="#9393FF")  # 设置背景色为蓝绿色
    select_directory_button.config(text="選擇EXCEL檔案", command=select_excel_file)
    selected_directory_label.config(text="")

if __name__ == "__main__":
    # 创建主窗口
    root = tk.Tk()
    root.title("模型分析應用程式")

    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")




    # 设置主窗口背景色为蓝绿色
    root.config(bg="#9393FF")

    # 创建应用程序介绍文本，设置背景色为蓝绿色
    introduction_label = tk.Label(root, text="這個應用程式為執行模型分析", bg="#00FFFF")
    introduction_label.pack(pady=10)

    # 创建选择目录按钮
    select_directory_button = tk.Button(root, text="選擇目錄", command=select_directory)
    select_directory_button.pack()

    # 创建显示选中目录的标签
    selected_directory_label = tk.Label(root, text="尚未選擇目錄")
    selected_directory_label.pack(pady=10)

    # 创建下一步按钮
    next_button = tk.Button(root, text="下一步", command=next_step, state=tk.DISABLED)
    next_button.pack(pady=10)

    # 启动主事件循环
    root.mainloop()
