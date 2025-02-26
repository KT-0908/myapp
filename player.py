from flask import Flask, request, render_template
import codecs
app = Flask(__name__)

@app.route("/")
def bbs():

    file = codecs.open("players.txt", "r", "utf-8")
    # file = codecs.open("C:/Flask/myapp/players.txt", "r", "utf-8")

    # この下で、テキストファイルを一括して読み込み、テンプレートに渡すようにする
    players = file.readlines()
    file.close()
    return render_template("index.html", players = players)
