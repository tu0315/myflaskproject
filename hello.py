# Flaskをインポート
from flask import Flask
from flask import render_template

# Flaskを実体化(インスタンス)
app = Flask(__name__)

# 変数を定義する
html = """
<h1>サンプルHTML</h1>
<ul>
    <li>箇条書き1</li>
    <li>箇条書き2</li>
    <li>箇条書き3</li>
</ul>
"""

# リストで定義
bullets = [
    "箇条書き1",
    "箇条書き2",
    "箇条書き3",
    "箇条書き4",
    "箇条書き5",
    "箇条書き6",
    "箇条書き7",
    "箇条書き8",
    "箇条書き9",
]


# ルーティング：URL作ってるイメージだよ
@app.route("/")
def hello():
    # 1、そのまま書く
    # return "<h1>Hello, World!</h1>"
    # 2，変数から取得する
    # return html
    # 3，テンプレートを用いる
    # return render_template("hello.html")
    # 4，テンプレートを用いる（for文）
    return render_template("hello.html", bullets=bullets)


@app.route("/japan/<city>")
def japan(city):
    # return f"Hello, japan_{city} !"
    # 変数を組み込む
    return render_template("hello.html", city=city, bullets=bullets)
