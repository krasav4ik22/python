import psycopg2
from flask import request, render_template_string,Flask,render_template
import time

 # Хранение пароля в открытом виде
connection = psycopg2.connect(host="host", 
                              user='user',
                              password="password",
                              database='database',
                              port=2345)


connection.autocommit = True
cursor = connection.cursor()
connection.autocommit = True
cursor = connection.cursor()

# Когда получаешь пароль из get параматера - надор взять его хэш
# Хранение пароля в открытом виде, создание аккаунта
@app.route("/")
def index():

	login = request.form.get('login')	
	password = request.form.get('password')

	cursor.execute("""INSERT table_password VALUE(%s, %s);""", (login,password))
	return render_template_string(" Хранение пароля в открытом виде ")

# Хранение пароля в открытом виде, создание аккаунта
@app.route("/reset")
def reset_password():

	login = request.form.get('login')	
	password = request.form.get('password')
	code = request.form.get('code')

	if cursor.execute("""SELECT table_code FROM table  WHERE login=%s AND code = %s""", (login, code)):
		cursor.execute("""UPDATE table_password set password = %s WHERE login=%s;""", (password, login))
	return render_template_string(" Хранение пароля в открытом виде ")


app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)