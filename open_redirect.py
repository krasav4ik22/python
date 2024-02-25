import base64
import mimetypes
import os

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlencode


def unvalidated_redirect(request):
    url = request.GET.get('url')
    return redirect(url)

##

@app.route("/login", methods=['GET', 'POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
       if auth(username, password):
           redirect_url = request.args.get('redirect_url', '/')
           return redirect(redirect_url)
       else:
           flash('Incorrect Credentials Supplied')
   return render_template('login.html', form=form) 
