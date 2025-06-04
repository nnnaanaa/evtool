import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui
import os
import time
import re
import platform

def choose_folder():
    folder = filedialog.askdirectory(title="保存先フォルダを選択")
    if folder:
        folder_path.set(folder)

def is_valid_filename(name):
    return not re.search(r'[\\/:*?"<>|]', name)

def open_folder(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":  # macOS
        os.system(f'open "{path}"')
    elif platform.system() == "Linux":
        os.system(f'xdg-open "{path}"')

def open_selected_folder():
    folder = folder_path.get()
    if not folder or not os.path.isdir(folder):
        messagebox.showwarning("警告", "有効な保存先フォルダを選択してください。")
        return
    open_folder(folder)

def take_screenshot():
    folder = folder_path.get()
    filename = filename_entry.get().strip()

    if not folder:
        messagebox.showwarning("警告", "保存先フォルダを選択してください。")
        return
    if not filename:
        messagebox.showwarning("警告", "ファイル名を入力してください。")
        return
    if not is_valid_filename(filename):
        messagebox.showwarning("警告", "ファイル名に使用できない文字が含まれています。\n\\ / : * ? \" < > |")
        return

    if not filename.lower().endswith(".png"):
        filename += ".png"

    full_path = os.path.join(folder, filename)

    if os.path.exists(full_path):
        result = messagebox.askyesno("確認", f"{full_path} はすでに存在します。\n上書きしますか？")
        if not result:
            return

    root.withdraw()
    time.sleep(1.0)

    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(full_path)
        messagebox.showinfo("成功", f"スクリーンショットを保存しました:\n{full_path}")
        if open_after_save.get():
            open_folder(folder)
    except Exception as e:
        messagebox.showerror("エラー", f"保存に失敗しました:\n{e}")
    finally:
        root.deiconify()

# GUI の作成
root = tk.Tk()
root.title("スクリーンショットアプリ")
root.geometry("400x300")

folder_path = tk.StringVar()
open_after_save = tk.BooleanVar(value=True)

# 保存先フォルダ選択
tk.Label(root, text="保存先フォルダ:").pack(anchor="w", padx=10, pady=(10, 0))
folder_frame = tk.Frame(root)
folder_frame.pack(fill="x", padx=10)
tk.Entry(folder_frame, textvariable=folder_path).pack(side="left", fill="x", expand=True)
tk.Button(folder_frame, text="参照", command=choose_folder).pack(side="left", padx=5)

# ファイル名入力
tk.Label(root, text="ファイル名（.png）:").pack(anchor="w", padx=10, pady=(10, 0))
filename_entry = tk.Entry(root)
filename_entry.pack(fill="x", padx=10)

# チェックボックス
tk.Checkbutton(root, text="保存後にフォルダを開く", variable=open_after_save).pack(anchor="w", padx=12, pady=(5, 0))

# 横並びボタン
button_frame = tk.Frame(root)
button_frame.pack(pady=20)
tk.Button(button_frame, text="スクリーンショットを保存", command=take_screenshot, height=2).pack(side="left", padx=5)
tk.Button(button_frame, text="保存先を開く", command=open_selected_folder, height=2).pack(side="left", padx=5)

root.mainloop()
