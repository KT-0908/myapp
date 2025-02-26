import pymysql

print("世界の皆さん、こんにちは")

connection = pymysql.connect(
        host='localhost',
        db='mydb',
        user='root',
        password='',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )

sql = "SELECT * FROM players"
cursor = connection.cursor()
cursor.execute(sql)
players = cursor.fetchall()

cursor.close()
connection.close()

for player in players:
    print(player["name"])
