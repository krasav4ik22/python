import psycopg2
from flask import request, render_template_string,Flask,render_template
import time

 # Настрой дб
connection = psycopg2.connect(host="host", 
                              user='user',
                              password="password",
                              database='database',
                              port=2345)


connection.autocommit = True
cursor = connection.cursor()

def long():
	time.sleep(5)
	return 1


# Активировать промокод два раза, при помощи двух быстрых запросов
@app.route("/")
def index():

	promocode = request.form.get('promocode')

	# Получение статуса промокода

	cursor.execute("""SELECT status FROM table  WHERE promocode=%s""", (promocode,))
	a = cursor.fetchone()[0]
 
	if a:

		# Долгая проверка
		long()
		cursor.execute("""UPDATE table set status = Fasle WHERE promocode(%s);""", (promocode,))

	return render_template_string(" Активировали два разапромокод ")



app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)