import psycopg2
from flask import request, render_template_string,Flask,render_template
import time
import subprocess
import sys
import shlex
import os
import asyncio

from dotenv import load_dotenv

load_dotenv()

print(os.getenv("username2"))

connection = psycopg2.connect(host="host", 
                              user='user',
                              password="password",
                              database='database',
                              port=2345)


connection.autocommit = True
cursor = connection.cursor()

# Os injection

@app.route("/")
def index_subprocess():
	# На прямую subprocess
	address = request.args.get("address")

	subprocess.run(["ls", address])

	subprocess.call("grep -R {} .".format(address), shell=True)
	subprocess.call("grep -R %s ." % address, shell=True)
	subprocess.call("grep -R" + address + " .", shell=True)
	subprocess.call(f"grep -R {address} .", shell=True)

	subprocess.call("grep -R {} .".format(address), shell=True)
	subprocess.call("grep -R %s ." % address, shell=True)
	subprocess.call("grep -R" + address + " .", shell=True)
	subprocess.call(f"grep -R {address} .", shell=True)

	subprocess.popen("grep -R {} .".format(address), shell=True)
	subprocess.popen("grep -R %s ." % address, shell=True)
	subprocess.popen("grep -R" + address + " .", shell=True)
	subprocess.popen(f"grep -R {address} .", shell=True)
	return render_template_string(" SQL инъекция ")


@app.route("/")
def index_os():
	# На прямую os
	address = request.args.get("address")
	os.system("grep -R {} .".format(address))
	os.system("grep -R %s ." % address)
	os.system("grep -R" + address + " .")
	os.system(f"grep -R {address} .")

	os.popen("grep -R {} .".format(address))
	os.popen("grep -R %s ." % address)
	os.popen("grep -R" + address + " .")
	os.popen(f"grep -R {address} .")

	os.spawnlpe(os.P_WAIT, address, ["-a"], os.environ)
	os.spawnve(os.P_WAIT, address, ["-a"], os.environ)
	os.spawnl(os.P_WAIT, address, ["-a"], os.environ)
	os.spawnle(os.P_WAIT, address, ["-a"], os.environ)
	os.spawnlp(os.P_WAIT, address, ["-a"], os.environ)
	os.spawnv(os.P_WAIT, address, ["-a"], os.environ)
	os.spawnve(os.P_WAIT, address, ["-a"], os.environ)
	os.spawnvpe(os.P_WAIT, address, ["-a"], os.environ)
	os.posix_spawn(os.P_WAIT, address, ["-a"], os.environ)
	
	os.spawnlpe(os.P_WAIT, "/bin/bash", ["-c", address], os.environ)
	os.spawnve(os.P_WAIT, "/bin/bash", ["-c", address], os.environ)
	os.spawnl(os.P_WAIT, "/bin/bash", ["-c", address], os.environ)
	os.spawnle(os.P_WAIT, "/bin/bash", ["-c", address], os.environ)
	os.spawnlp(os.P_WAIT, "/bin/bash", ["-c", address], os.environ)
	os.spawnv(os.P_WAIT, "/bin/bash", ["-c", address], os.environ)
	os.spawnve(os.P_WAIT, "/bin/bash", ["-c", address], os.environ)
	os.spawnvp(os.P_WAIT, "/bin/bash", ["-c", address], os.environ)
	os.spawnvpe(os.P_WAIT, "/bin/bash", ["-c", address], os.environ)
	os.posix_spawn(os.P_WAIT, "/bin/bash", ["-c", address], os.environ)

	def index_os_execl():
		os.execl("/bin/bash", ["/bin/bash", "-c", address], os.environ)
	def index_os_execle():
		os.execle("/bin/bash", ["/bin/bash", "-c", address], os.environ)
	def index_os_execlp():	
		os.execlp("/bin/bash", ["/bin/bash", "-c", address], os.environ)
	def index_os_execlpe():	
		os.execlpe("/bin/bash", ["/bin/bash", "-c", address], os.environ)
	def index_os_execv():	
		os.execv("/bin/bash", ["/bin/bash", "-c", address], os.environ)
	def index_os_execve():	
		os.execve("/bin/bash", ["/bin/bash", "-c", address], os.environ)
	def index_os_execvp():	
		os.execvp("/bin/bash", ["/bin/bash", "-c", address], os.environ)
	def index_os_execvpe():	
		os.execvpe("/bin/bash", ["/bin/bash", "-c", address], os.environ)

	index_os_execl()
	index_os_execle()
	index_os_execlp()
	index_os_execlpe()
	index_os_execv()
	index_os_execve()
	index_os_execvp()
	index_os_execvpe()
	return render_template_string(" SQL инъекция ")

@app.route("/")
def index_anycio():
	address = request.args.get("address")
    # ansycio
	loop = asyncio.new_event_loop()

	loop.subprocess_shell(asyncio.SubprocessProtocol, address)
	loop.subprocess_exec(asyncio.SubprocessProtocol, [user_input, "--parameter"])
	loop.subprocess_exec(asyncio.SubprocessProtocol, ['ls', '-l', address])


	asyncio.subprocess.create_subprocess_shell(address)
	asyncio.subprocess.create_subprocess_exec("bash", ["bash", "-c", address])
	return render_template_string(" SQL инъекция ")

@app.route("/")
def index_with_variable():
	address = request.args.get("address")
	# Через переменную
	command = "ping -c 1 {}".format(address)
	subprocess.call(command)
	return render_template_string(" SQL инъекция ")

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)