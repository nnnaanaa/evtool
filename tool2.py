import tkinter as tk

def resize_border(event):
    # ウィンドウサイズに合わせて枠を再描画
    w = event.width
    h = event.height
    canvas.delete("border")
    pad = 5
    canvas.create_rectangle(pad, pad, w - pad, h - pad, outline="purple", width=2, tags="border")

root = tk.Tk()
root.title("確認アプリ")
root.geometry("300x200+300+300")

transparent_color = "white"
root.config(bg=transparent_color)
root.wm_attributes("-transparentcolor", transparent_color)

canvas = tk.Canvas(root, bg=transparent_color, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# 初期枠描画
canvas.create_rectangle(5, 5, 295, 195, outline="purple", width=2, tags="border")

# リサイズ時に枠を追従
canvas.bind("<Configure>", resize_border)

root.mainloop()
