import psycopg2
from flask import request, render_template_string,Flask,render_template
import time

import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('db4.db',check_same_thread=False)
cursor = connection.cursor()

app = Flask(__name__)


# удалим старую таблицу
cursor.execute('''DROP TABLE IF EXISTS Users''')

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
promocode TEXT ,
status TEXT)
''')

cursor.execute('''INSERT INTO Users (promocode, status) VALUES("Alex","True")''')
cursor.execute('''INSERT INTO Users (promocode, status) VALUES("Pavel","False")''')


def long():
	time.sleep(5)
	return 1

# Активировать промокод два раза, при помощи двух быстрых запросов
# http://127.0.0.1:5000/race?username=Alex&promocode=Alex
# http://127.0.0.1:5000/race?username=Pety&promocode=Alex

@app.route("/race")
def index():
	username = request.args.get('username')
	promocode = request.args.get('promocode')
	print(promocode)
	# Получение статуса промокода
	print("""SELECT status FROM Users  WHERE promocode='%s' AND status='True';'""" % promocode)
	
    cursor.execute("""SELECT status FROM Users  WHERE promocode='%s' AND status='True';""" % promocode)

	try:
		a = cursor.fetchone()[0]
	except: 
		a = "False"	
 
	if a =="True":

		# Долгая проверка
		long()
		cursor.execute("""UPDATE Users set status='False' WHERE promocode='%s';""" % promocode)

		return render_template_string(" Промокод активирован для  %s " % username)

	else:
		return render_template_string(" Промокод был активирован %s " % username)
	return render_template_string(" Активировали два разапромокод ")





if __name__ == '__main__':
    app.run()