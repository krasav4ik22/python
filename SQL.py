import psycopg2
from flask import request, render_template_string,Flask,render_template
import time

password = "qwe"

 # Настрой дб
connection = psycopg2.connect(host="host", 
                              user='user',
                              password="password",
                              database='database',
                              port=2345)


connection.autocommit = True
cursor = connection.cursor()

# SQL инъекция ещё 
# cursor.execute("SELECT * FROM db_table WHERE stud_name = (?)" % promocode)
# cursor.executescript("SELECT * FROM db_table WHERE stud_name = (?)" % promocode)
@app.route("/")
def index():
	promocode = request.args.get('promocode')

	# форматирование 
	cursor.execute("SELECT * FROM db_table WHERE stud_name = %s;" % (promocode,))
	cursor.execute("SELECT * FROM db_table WHERE stud_name = " + promocode + " ;")
	cursor.execute("SELECT * FROM db_table WHERE stud_name = {} ;".format(promocode))
	cursor.execute(f"SELECT * FROM db_table WHERE stud_name = {promocode} ;")

	return render_template_string(" SQL инъекция ")

# SQL инъекция через переменную
@app.route("/sql")
def sql():
	promocode = request.form.get('promocode')
	st1 = "SELECT * FROM db_table WHERE stud_name = %s;" % promocode
	st2 = "SELECT * FROM db_table WHERE stud_name = " + promocode + " ;"
	st3 = "SELECT * FROM db_table WHERE stud_name = {} ;".format(promocode)
	st4 = f"SELECT * FROM db_table WHERE stud_name = {promocode} ;"

	# форматирование 
	cursor.execute(st1)
	cursor.execute(st2)
	cursor.execute(st3)
	cursor.execute(st4)

	return render_template_string(" SQL инъекция ")


app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)