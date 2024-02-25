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


# Активировать промокод два раза, при помощи двух быстрых запросов
@app.route("/")
def index():

	id1 = request.form.get('key1') # id певрого
	count = request.form.get('count') # сумма
	id2 = request.form.get('key2') # id второго не существующего человека
	
	# Получение количества денег у первого
	cursor.execute("""SELECT money FROM table  WHERE id=%s""", (id1,))
	money1 = cursor.fetchone()[0]
	if money1 > count:
        #снимим деньги
		cursor.execute("""UPDATE table SET money=%s WHERE id=%s """, (count, id1))
		
        # переведи на не сущетствующий
		cursor.execute("""UPDATE table SET money=%s WHERE id=%s """, (count,id2))

	return render_template_string(" Деньги потерялись ")



app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)