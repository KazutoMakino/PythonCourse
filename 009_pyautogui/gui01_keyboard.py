"""Pyautogui のキーボード操作について.

References:
- https://pyautogui.readthedocs.io/en/latest/
- https://pyautogui.readthedocs.io/en/latest/keyboard.html

Blog:
- https://slash-z.com/python-pyautogui/

---

KazutoMakino
"""

import time

import pyautogui as pg

######################################################################
# pg.press(keys, presses=1, interval=0, logScreenshot=False)
# ・・・・keys で指定したキーを presses 回押す．
#   keys (str, list):
#       pg.KEYBOARD_KEYS で確認できるキーボード上のキー
#   presses (int):
#       keys を押す回数（初期値：1）
#   interval (float):
#       presses 回繰り返し押すときの待ち時間（初期値：0）
#   logScreenshot (bool):
#       動作終了時にタイムスタンプ名称でスクリーンショットを保存するかどうか
#       （初期値：False）
print("pg.press")
pg.press(keys="win", presses=1, interval=1, logScreenshot=False)
time.sleep(1)
print()

######################################################################
# pg.write(message, interval, logScreenshot)
# ・・・・message の文字列一文字ずつを interval 秒ずつ空けて入力する
#   message (str, list):
#       入力する文字列（日本語入力したい場合は，pyperclip.copy(文字列) → pg.hotkey("ctrl", "v")）
#   interval (float):
#       message 一文字ずつ（list の場合は一つずつ）入力するときの待ち時間
#       （初期値：0）
#   logScreenshot (bool):
#       動作終了時にタイムスタンプ名称でスクリーンショットを保存するかどうか
#       （初期値：False）
print("pg.write")
pg.write(message="calc", interval=0, logScreenshot=False)
time.sleep(1)
print()

######################################################################
# pg.keyDown(key, logScreenshot)
# ・・・・ key を押した状態にする
#   key (str)
#       pg.KEYBOARD_KEYS で確認できるキーボード上のキー
#   logScreenshot (bool):
#       動作終了時にタイムスタンプ名称でスクリーンショットを保存するかどうか
#       （初期値：False）
print("pg.keyDown / pg.press")
pg.keyDown(key="win", logScreenshot=False)

# windows キーを押したまま e で新しいエクスプローラが開く
pg.press(keys="e", interval=1)
# 今開いたエクスプローラに対して windows + 下 2 回で最小化させる
pg.press(keys="down", presses=2, interval=1)
print()

######################################################################
# pg.keyUp(key, logScreenshot)
# ・・・・ key を離した状態にする
#   key (str)
#       pg.KEYBOARD_KEYS で確認できるキーボード上のキー
#   logScreenshot (bool):
#       動作終了時にタイムスタンプ名称でスクリーンショットを保存するかどうか
#       （初期値：False）
print("pg.keyUp")
pg.keyUp(key="win", logScreenshot=False)
print()

######################################################################
# pg.hold(keys, logScreenshot)・・・・keys を押したままにする
# （with ブロックを使うと，ブロックを抜けたときに解除できる）
#   keys (str, list):
#       pg.KEYBOARD_KEYS で確認できるキーボード上のキー
#   logScreenshot (bool):
#       動作終了時にタイムスタンプ名称でスクリーンショットを保存するかどうか
#       （初期値：False）
print("pg.hold / pg.press")
with pg.hold(keys="win", logScreenshot=False):
    for _ in range(3):
        # 新しいエクスプローラを 3 つ立ち上げる
        pg.press(keys="e")
        time.sleep(1)
print()

######################################################################
# pg.hotkey(*args, *keywords)・・・・キー同時押し
print("pg.hotkey")
pg.hotkey("ctrl", "w")
