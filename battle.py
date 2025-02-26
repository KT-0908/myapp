from flask import Flask, request, render_template
app = Flask(__name__)

# ここで、enemiesに値を追加する
enemies = ["スライム","モンスター","ドラゴン"]

@app.route("/")
def show():
    message = "あらたなモンスターがあらわれた"
    return render_template("battle.html", message = message, enemies = enemies)

@app.route("/result", methods=["POST"])
def result():
    name = request.form["name"]
    message = "勇者は、"  + name + "と戦った"
    return render_template("battle.html", message = message, enemies = enemies)

