from flask import Flask, render_template
import pymysql
app = Flask(__name__)

def getConnection():
    return pymysql.connect(
        host='localhost',
        db='laravel_task',
        user='root',
        password='',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def select_sql():
    connection = getConnection()
    message = "Hello world"

    sql = "SELECT * FROM contact_forms LIMIT 25"
    cursor = connection.cursor()
    cursor.execute(sql)
    players = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('view.html', message = message, players = players)