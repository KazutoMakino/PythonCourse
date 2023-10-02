"""Pyautogui のスクリーンショット関連について.

References:
- https://pyautogui.readthedocs.io/en/latest/
- https://pyautogui.readthedocs.io/en/latest/screenshot.html

Blog:
- https://slash-z.com/python-pyautogui/

---

KazutoMakino
"""

from pathlib import Path
from pprint import pprint

import pyautogui as pg

# 画像ファイルのパス
img_path = "./screenshot.jpg"

######################################################################
# pg.screenshot(imageFilename=None, region=None)
# ・・・・スクリーンショットを取得する．戻り値はスクリーンショットの画像の PIL.Image.Image．
#   imageFilename (str): パス文字列を指定した場合は，スクリーンショットが保存される
#       (初期値: None・・・・スクリーンショットは保存されない)
#   region (tuple): 左上の x, y 座標と幅と高さ (x, y, w, h) を指定することで
#       スクリーンショットの領域を指定することができる
#       (初期値: None ・・・・全体の領域)
img = pg.screenshot(imageFilename=img_path, region=(100, 100, 800, 600))
print("--- pg.screenshot")
print(f"img.size = {img.size}")
print(f"file exists: {Path(img_path).exists()}")
print()

######################################################################
# pg.locateOnScreen(filepath, confidence=1.0, grayscale=False)
# ・・・・filepath で指定した画像と画面をパターンマッチングし，適合した画像の左上の x, y 座標と
# 幅と高さを取得する．候補が複数ある場合は，一番左上の値を取得する．
# cv2.matchTemplate を用いるため opencv-python が必要．
# また，opencv は日本語を受け付けないため，パス文字列には日本語が入らないようにする．
#   filepath (str): パターンマッチングする画像ファイルのパス文字列．
#   confidence (float): パターンマッチングする精度で，1.0 未満を指定することで，
#       少しのピクセル誤差であれば許容することができ，パターンマッチングが成功しやすくなる (初期値: 1.0)
#   grayscale (bool): パターンマッチングするときに互いをグレイスケールで比較することで，
#       高速化させることができるが精度は低くなる (初期値: False)
location = pg.locateOnScreen(img_path, confidence=0.9, grayscale=False)
print("--- pg.locateOnScreen")
print(f"location = {location}")
print(f"type(location) = {type(location)}")
print(f"location.left = {location.left}")
print()

######################################################################
# pg.locateCenterOnScreen(filepath, confidence=1.0, grayscale=False)
# ・・・・filepath で指定した画像と画面をパターンマッチングし，適合した画像の中心の x, y 座標を取得する．
# 候補が複数ある場合は，一番左上の値を取得する．cv2.matchTemplate を用いるため opencv-python が必要．
# また，opencv は日本語を受け付けないため，パス文字列には日本語が入らないようにする．
#   filepath (str): パターンマッチングする画像ファイルのパス文字列．
#   confidence (float): パターンマッチングする精度で，1.0 未満を指定することで，
#       少しのピクセル誤差であれば許容することができ，パターンマッチングが成功しやすくなる (初期値: 1.0)
#   grayscale (bool): パターンマッチングするときに互いをグレイスケールで比較することで，
#       高速化させることができるが精度は低くなる (初期値: False)
location = pg.locateCenterOnScreen(img_path, confidence=0.9, grayscale=False)
print("--- pg.locateCenterOnScreen")
print(f"location = {location}")
print()

######################################################################
# pg.locateAllOnScreen(filepath, confidence=1.0, grayscale=False)
# ・・・・filepath で指定した画像と画面をパターンマッチングし，適合した全ての画像の左上の x, y 座標と
# 幅と高さをジェネレータとして返す．cv2.matchTemplate を用いるため opencv-python が必要．
# また，opencv は日本語を受け付けないため，パス文字列には日本語が入らないようにする．
#   filepath (str): パターンマッチングする画像ファイルのパス文字列．
#   confidence (float): パターンマッチングする精度で，1.0 未満を指定することで，
#       少しのピクセル誤差であれば許容することができ，パターンマッチングが成功しやすくなる (初期値: 1.0)
#   grayscale (bool): パターンマッチングするときに互いをグレイスケールで比較することで，
#       高速化させることができるが精度は低くなる (初期値: False)
locations = pg.locateAllOnScreen(img_path, confidence=0.9, grayscale=False)
print("--- pg.locateAllOnScreen")
print(f"locations = {locations}")
print(f"type(locations) = {type(locations)}")
print("list(locations) =")
pprint(list(locations))
