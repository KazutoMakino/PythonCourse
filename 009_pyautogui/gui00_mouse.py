"""pyautogui のマウス操作について

References:
- https://pyautogui.readthedocs.io/en/latest/
- https://pyautogui.readthedocs.io/en/latest/mouse.html

Blog:
- https://slash-z.com/python-pyautogui/

---

KazutoMakino

"""

import pyautogui as pg

######################################################################
# pg.size()・・・・メインモニタの縦と横のピクセルサイズを取得する
print("pg.size")
width, height = pg.size()
print(f"(width, height) = ({width}, {height})")
print()

######################################################################
# pg.position()・・・・現在のマウスの位置を取得
print("pg.position")
mouse_x, mouse_y = pg.position()
print(f"(mouse_x, mouse_y) = {mouse_x}, {mouse_y}")
print()

######################################################################
# pg.moveTo(x, y, duration=0, logScreenshot=False)
# ・・・・マウスを x, y に duration [s] かけて動かす
#   x, y (int, int):
#       マウスを動した先の座標（原点はモニタの左上の (0, 0)）
#   duration (float):
#       何秒かけて x, y に移動させるか（初期値：0）
#   logScreenshot (bool)
#       動作終了時にタイムスタンプ名称でスクリーンショットを保存するかどうか
#       （初期値：False）
pg.moveTo(x=500, y=300, duration=1.2, logScreenshot=False)
mouse_x, mouse_y = pg.position()
print(f"pg.moveTo(x=500, y=300) -> (mouse_x, mouse_y) = {mouse_x}, {mouse_y}")
# moveTo は絶対座標指定だが，相対座標を指定したい場合は move を用いる

# pg.onScreen(x, y)・・・・指定する x, y 座標がスクリーン上にあるかどうかの判定を返す
#   例えば 1920 x 1080 のモニタの場合，原点は左上の (0, 0) で，右下は (1919, 1079) となる
print("pg.onScreen(x=0, y=0):", pg.onScreen(x=0, y=0))
print("pg.onScreen(x=0, y=-1):", pg.onScreen(x=0, y=-1))
print("pg.onScreen(x=width, y=height):", pg.onScreen(x=width, y=height))
print("pg.onScreen(x=width - 1, y=height - 1):", pg.onScreen(x=width - 1, y=height - 1))
print()

######################################################################
# pg.vscroll(clicks, x=None, y=None, logScreenshot=False)
#   ・・・・x, y 座標で clicks の分だけ縦スクロールする
#   clicks (int, float):
#       スクロールする量
#   x, y (int):
#       スクロールさせるときのマウス位置（初期値：None）
#   logScreenshot (bool):
#       動作終了時にタイムスタンプ名称でスクリーンショットを保存するかどうか
#       （初期値：False）
print("pg.vscroll")
pg.vscroll(clicks=100)
print()

######################################################################
# pg.dragTo(x, y, duration=0, button="right", logScreenshot=False, mouseDownUp=True)
#   ・・・・x, y に duration [s] かけて button を押しながらドラッグする
#   x, y (int, int):
#       マウスを動した先の座標（原点はモニタの左上の (0, 0)）
#   duration (float):
#       何秒かけて x, y に移動させるか（初期値：0）
#   button (str):
#       ドラッグ操作に用いるマウスボタン（初期値："PRIMARY" ("left" と同じ)）．
#       "left", "right", "middle" が有効．
#   logScreenshot (bool):
#       動作終了時にタイムスタンプ名称でスクリーンショットを保存するかどうか
#       （初期値：False）
#   mouseDownUp (bool):
#       True の場合ドラッグ終了後ボタンを離し，False はボタンを押下したままにする
print("pg.dragTo")
pg.dragTo(
    x=100, y=500, duration=1.1, button="right", logScreenshot=False, mouseDownUp=True
)
# dragTo は絶対座標指定だが，相対座標を指定したい場合は drag を用いる
print()

######################################################################
# pg.rightClick(x, y, interval=0, duration=0, logScreenshot=False)
#   ・・・・x, y に duration [s] かけて右クリックする
print("pg.rightClick")
pg.rightClick(x=500, y=200, interval=1.3, duration=1.8, logScreenshot=False)
#   x, y (int, int):
#       マウスを動した先の座標（原点はモニタの左上の (0, 0)）
#   interval (float):
#       x, y 移動後に何秒待つか（初期値：0）
#   duration (float):
#       何秒かけて x, y に移動させるか（初期値：0）
#   logScreenshot (bool):
#       動作終了時にタイムスタンプ名称でスクリーンショットを保存するかどうか
#       （初期値：False）
# leftClick, middleClick, doubleClick などももちろんあるが，
# 誤操作防止の為，今回の例では用いていない
