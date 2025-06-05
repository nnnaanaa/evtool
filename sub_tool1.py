import os
import pyautogui
import time

# 保存先フォルダ
output_folder = "img"

# フォルダが存在しなければ作成
os.makedirs(output_folder, exist_ok=True)

# スクリーンショットを99枚保存
for i in range(1, 22):
    filename = f"3-1-{i}.png"
    filepath = os.path.join(output_folder, filename)

    # スクリーンショットを取得して保存
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)
    print(f"{filename} を保存しました")

    # 必要なら遅延（例: 0.5秒）
    time.sleep(0.01)
