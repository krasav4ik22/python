import psycopg2
from flask import request, render_template_string,Flask,render_template, Markup
import time
from jinja2 import Markup

connection = psycopg2.connect(host="host", 
                              user='user',
                              password="password",
                              database='database',
                              port=2345)


connection.autocommit = True
cursor = connection.cursor()
@app.route("/")
def index():

	promocode = request.form.get('promocode')

	# render_template_string  render_template return

	# render_template_string вставка
	if promocode == "Прямая вставка %s":
		return render_template_string("<div>%s</div>" % request.form.get('promocode'))
	elif promocode == "Прямая вставка format":
		return render_template_string("<div>{}</div>".format(request.form.get('promocode')))
	elif promocode == "Прямая вставка +":
		return render_template_string("<div>" + request.form.get('promocode'))

	if promocode == "Через переменную %s":
		return render_template_string("<div>%s</div>" % promocode)
	elif promocode == "Через переменную  вставка format":
		return render_template_string("<div>{}</div>".format(promocode))
	elif promocode == "Через переменную  вставка {promocode}":
		return render_template_string(f"<div>{promocode}</div>")
	elif promocode == "Через переменную  вставка +":
		return render_template_string("<div>" + promocode)
	
    # Markup
	elif promocode == "Markup через переменную %s":
		html_output = Markup('<p>You searched for: %s ' % promocode)
	elif promocode == "Markup через переменную pro":
		html_output = Markup(f'<p>You searched for: {promocode} ')	
	elif promocode == "Markup через переменную %s":
		html_output = Markup('<p>You searched for: %s '.format(promocode))	
		return render_template_string(html_output)
	elif promocode == "Markup через переменную +":
		html_output = Markup('<p>You searched for: '+promocode)	
		return render_template_string(html_output)
	elif promocode == "Markup на прямую %s":
		html_output = Markup('<p>You searched for: %s ' % request.form.get('promocode'))
	elif promocode == "Markup на прямую format":
		html_output = Markup('<p>You searched for: %s '.format(request.form.get('promocode')))	
		return render_template_string(html_output)		
	elif promocode == "Markup на прямую +":
		html_output = Markup('<p>You searched for: '+ request.form.get('promocode'))	
		return render_template_string(html_output)
	# return через переменную
	if promocode == "Через переменную %s":
		return ("<div>%s</div>" % promocode)
	elif promocode == "Через переменную  вставка format":
		return ("<div>{}</div>".format(promocode))
	elif promocode == "Через переменную  вставка {promocode}":
		return (f"<div>{promocode}</div>")
	elif promocode == "Через переменную  вставка +":
		return (f"<div>" + promocode)
	
    # return напрямую
	if promocode == "Прямая вставка %s":
		return render_template_string("<div>%s</div>" % request.form.get('promocode'))
	elif promocode == "Прямая вставка format":
		return render_template_string("<div>{}</div>".format(request.form.get('promocode')))
	elif promocode == "Прямая вставка +":
		return render_template_string("<div>{}</div>" + request.form.get('promocode'))
	

			
            #HttpResponse

	if promocode == "Через переменную %s":
		return HttpResponse("<div>%s</div>" % promocode)		
	elif promocode == "Через переменную  вставка format":
		return HttpResponse("<div>{}</div>".format(promocode))
	elif promocode == "Через переменную  вставка {promocode}":
		return HttpResponse(f"<div>{promocode}</div>")
	elif promocode == "Через переменную  вставка {promocode}":
		return HttpResponse("<div>"+promocode+"</div>")		

	return HttpResponse("Hello, " + name)

# Не безопасные методы

# __html__ 
# class RawHtml(str):
#   def __html__(self): 
#   return str(self)

# # Использование html_safe
# @html_safe
# class RawHtml(str):
#   pass


# HTML

# render

@app.route("/html")
def html():

	promocode = request.form.get('promocode')

	# Отлюкчение autoescape

	if promocode == "Через отключение autoescape":
		html = "{% autoescape false %}  \
					<p>autoescaping is disabled here  <p> \
					{{ will_not_be_escaped }} \
				{% endautoescape %}	"
		return render_template_string(html)
	elif promocode == "Через отключение autoescape и подстановку напрямую":
		return render_template_string("{% autoescape false %}  \
					<p>autoescaping is disabled here  <p> \
					{{ will_not_be_escaped }} \
				{% endautoescape %}	")

	# Через отключение autoescape в render
	elif promocode == "Через отключение autoescape в render":
		response = render(request, "index.html", {"autoescape": False})

	# Использование безопансых переменных

	if promocode == "Через Использование безопансых переменных":
		html = "{% autoescape false %}  \
					<p>autoescaping is disabled here  <p> \
					{{ name | safe }} \
				{% endautoescape %}	"
		return render_template_string(html)
	
    # Переменная без кавычек в атрибуте

	if promocode == "Переменная без кавычек в атрибуте":
		html = "{% autoescape false %}  \
					<p>autoescaping is disabled here  <p> \
					<div class={{ classes }}></div> \
				{% endautoescape %}	"
		return render_template_string(html)

	# Через href ссылки, так как экранирование здесь не помогает. Нужно url_for

	link = "https://google.com/" + promocode

	if promocode == "render":
		return render_template("XSS.html",data=promocode)
	
	
	if promocode == "Через href ссылки, так как экранирование здесь не помогает. render_template_string":
		html = '''{% autoescape false %}  \
					<p>autoescaping is disabled here  <p> \
					<a href="{{ link }}"></a> \
				{% endautoescape %}	'''
		return render_template("XSS.html")
    elif promocode == "Через href ссылки, так как экранирование здесь не помогает. render_template":
		html = '''{% autoescape false %}  \
					<p>autoescaping is disabled here  <p> \
					<a href="{{ link }}"></a> \
				{% endautoescape %}	'''
		return render_template("XSS.html")
	elif promocode == "Через href ссылки, так как экранирование здесь не помогает. return через переменную":
		html = '''{% autoescape false %}  \
					<p>autoescaping is disabled here  <p> \
					<a href="{{ link }}"></a> \
				{% endautoescape %}	'''
		return html

	elif promocode == "Через href ссылки, так как экранирование здесь не помогает. return напрямую":
		return ('''{% autoescape false %}  \
					<p>autoescaping is disabled here  <p> \
					<a href="{{ link }}"></a> \
				{% endautoescape %}	''')

# отключение настроек

TEMPLATES = [
  {
    ...,
    'OPTIONS': {'autoescape': False}
  }
]

TEMPLATES = [
  {
    ...,
    "OPTIONS": {'autoescape': False}
  }
]

TEMPLATES = [
  {
    ...,
    "OPTIONS": {"autoescape": False}
  }
]

TEMPLATES = [
  {
    ...,
    'OPTIONS': {"autoescape": False}
  }
]




app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)