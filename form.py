from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def show():
    message = "hello world"
    return render_template("form.html", message = message)

# @app.route("/about")
# def about():
#     return "This is paiza"

@app.route("/result", methods = ["GET","POST"])
def result():
    message = "Welcome to the Hololive"
    if request.method == "POST":
        article = request.form["article"]
        name = request.form["name"]
    else:
        article = request.args.get("article")
        name = request.args.get("name")
    return render_template("form.html", message = message, article = article, name = name)



