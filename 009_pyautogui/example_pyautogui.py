"""自動化の例: windows10 においてディスプレイの拡大率の変更を自動化

References:
- https://pyautogui.readthedocs.io/en/latest/

Blog:
- https://slash-z.com/python-pyautogui/

---

KazutoMakino

"""

import time

import pyautogui as pg
import pyperclip

# 拡大させるのか縮小させるのかを取得する
ret = pg.confirm(
    text="テキスト、アプリ、その他の項目のサイズを拡大させますか？\nそれとも縮小させますか？",
    title="テキスト、アプリ、その他の項目のサイズの変更",
    buttons=["拡大", "縮小", "キャンセル"],
)
print(f"拡大？ or 縮小？ : {ret}")
if ret == "拡大":
    mode = "expansion"
elif ret == "縮小":
    mode = "shrink"
else:
    exit()

# このターミナルのウィンドウを右に寄せる
print("このターミナルのウィンドウを右に寄せる")
pg.hotkey("win", "right")
time.sleep(1)

# ディスプレイの設定を開く
print("ディスプレイの設定を開く")
pyperclip.copy(text="テキスト、アプリ、その他の項目のサイズを変更する")
pg.press(keys="win")
pg.hotkey("ctrl", "v")
time.sleep(1)
pg.press(keys="enter")
time.sleep(3)

# 設定のウィンドウを左に寄せる
print("設定のウィンドウを左に寄せる")
pg.hotkey("win", "left")
time.sleep(1)

if mode == "expansion":
    # 拡大率が 100 % のときの "テキスト、アプリ、その他の項目のサイズを変更する" の項目のドロップダウンの位置を取得する
    print('拡大率が 100 % のときの "テキスト、アプリ、その他の項目のサイズを変更する" の項目のドロップダウンの位置を取得する')
    locate = pg.locateOnScreen("./img/01.jpg", confidence=0.95, grayscale=True)
    x, y = locate.left + 141, locate.top + 91

    # ドロップダウンにマウスを移動し左クリックする
    print("ドロップダウンにマウスを移動し左クリックする")
    pg.moveTo(x=x, y=y, duration=1)
    pg.leftClick()
    time.sleep(1)

    # ドロップダウンから拡大率 150 % を選択してクリックする
    print("ドロップダウンから拡大率 150 % を選択してクリックする")
    locate = pg.locateOnScreen("./img/02.jpg", confidence=0.95, grayscale=True)
    x, y = locate.left + 60, locate.top + 45
    pg.moveTo(x=x, y=y, duration=1)
    pg.leftClick()

elif mode == "shrink":
    # 拡大率が 150 % のときの "テキスト、アプリ、その他の項目のサイズを変更する" の項目のドロップダウンの位置を取得する
    print('拡大率が 150 % のときの "テキスト、アプリ、その他の項目のサイズを変更する" の項目のドロップダウンの位置を取得する')
    locate = pg.locateOnScreen("./img/03.jpg", confidence=0.95, grayscale=True)
    x, y = locate.left + 215, locate.top + 70

    # ドロップダウンにマウスを移動し左クリックする
    print("ドロップダウンにマウスを移動し左クリックする")
    pg.moveTo(x=x, y=y, duration=1)
    pg.leftClick()
    time.sleep(1)

    # ドロップダウンから拡大率 100 % を選択してクリックする
    print("ドロップダウンから拡大率 100 % を選択してクリックする")
    locate = pg.locateOnScreen("./img/04.jpg", confidence=0.95, grayscale=True)
    x, y = locate.left + 70, locate.top + 25
    pg.moveTo(x=x, y=y, duration=1)
    pg.leftClick()

time.sleep(1)

# 完了ウィンドウを出す
print("完了ウィンドウを出して終了")
pg.alert(text="全ての動作が正常終了しました", title="完了")
