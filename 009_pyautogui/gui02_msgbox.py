"""pyautogui のメッセージボックスについて

References:
- https://pyautogui.readthedocs.io/en/latest/
- https://pyautogui.readthedocs.io/en/latest/msgbox.html

Blog:
- https://slash-z.com/python-pyautogui/

---

KazutoMakino

"""

import pyautogui as pg

######################################################################
# pg.alert(text="", title="", button="", timeout=None)
# ・・・・警告のメッセージボックスを出す．戻り値は button の値．
#   text (str): メッセージボックスで表示するテキスト (初期値："")
#   title (str): メッセージボックスウィンドウのタイトル (初期値："")
#   button (str): メッセージボックスのボタンのテキスト (初期値："")
#   timeout (int):
#       メッセージボックスを表示する時間制限 [ms]．
#       指定時間をすぎるとメッセージボックスが閉じ，"Timeout" が返される．
#       (初期値：None)
print("pg.alert")
print(pg.alert(text="テキスト", title="pg.alert", button="閉じる", timeout=5000))
print()

######################################################################
# pg.confirm(text="", title="", buttons=["OK", "Cancel"], timeout=None)
# ・・・・警告のメッセージボックスを出す．戻り値は buttons の値．
#   text (str): メッセージボックスで表示するテキスト (初期値："")
#   title (str): メッセージボックスウィンドウのタイトル (初期値："")
#   buttons (list): メッセージボックス内の複数のボタンのテキスト (初期値："")
#   timeout (int):
#       メッセージボックスを表示する時間制限 [ms]．
#       指定時間をすぎるとメッセージボックスが閉じ，"Timeout" が返される．
#       (初期値：None)
print("pg.confirm")
print(
    pg.confirm(
        text="テキスト", title="pg.confirm", buttons=["はい", "いいえ", "キャンセル"], timeout=5000
    )
)
print()

######################################################################
# pg.prompt(text="", title="", default="", timeout=None)
# ・・・・テキスト入力部のあるメッセージボックスを出す．戻り値は入力したテキスト．
#   text (str): メッセージボックスで表示するテキスト (初期値："")
#   title (str): メッセージボックスウィンドウのタイトル (初期値："")
#   default (str): テキスト入力部の初期値 (初期値："")
#   timeout (int):
#       メッセージボックスを表示する時間制限 [ms]．
#       指定時間をすぎるとメッセージボックスが閉じ，"Timeout" が返される．
#       (初期値：None)
print("pg.prompt")
print(pg.prompt(text="テキスト", title="pg.prompt", default="デフォルト", timeout=5000))
print()

######################################################################
# pg.password(text="", title="", default="", mask="*", timeout=None)
# ・・・・テキスト入力部のあるメッセージボックスを出す．戻り値は入力したテキスト．
#   text (str): メッセージボックスで表示するテキスト (初期値："")
#   title (str): メッセージボックスウィンドウのタイトル (初期値："")
#   default (str): テキスト入力部の初期値 (初期値："")
#   mask (str): パスワード入力を隠す文字列 (初期値："*")
#   timeout (int):
#       メッセージボックスを表示する時間制限 [ms]．
#       指定時間をすぎるとメッセージボックスが閉じ，"Timeout" が返される．
#       (初期値：None)
print("pg.password")
print(
    pg.password(
        text="テキスト", title="pg.password", default="デフォルト", mask="x", timeout=5000
    )
)
