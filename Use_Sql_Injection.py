import psycopg2
from flask import request, render_template_string,Flask,render_template
import time
import sqlite3
import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('db3.db',check_same_thread=False)
cursor = connection.cursor()



# удалим старую таблицу
cursor.execute('''DROP TABLE IF EXISTS Users''')

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT ,
password TEXT)
''')

cursor.execute('''INSERT INTO Users (username, password) VALUES("Alex","Alex")''')
cursor.execute('''INSERT INTO Users (username, password) VALUES("Pavel","Pavel")''')
cursor.execute('''INSERT INTO Users (username, password) VALUES("Sergey","Sergey")''')

app = Flask(__name__)

# SQL инъекция
# Обход авторизации

# http://127.0.0.1:5000/sql?login=Alex&password=Alex - верное
# http://127.0.0.1:5000/sql?login=Alex&password=Alex2- неверное
# http://127.0.0.1:5000/sql?login=Alex%27;-- обход авторизации


@app.route("/sql")
def index():

	login = request.args.get('login')
	password = request.args.get('password')
 
	
	cursor.execute(f"SELECT username FROM Users WHERE username = '{login}' AND password = '{password}';")
	connection.commit()
	records = cursor.fetchall()

	if records:
		return render_template_string(" Вы авторизировались ")
	else:
		return (" Не получилось")





if __name__ == '__main__':
    app.run()