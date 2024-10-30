# -*- coding: utf-8 -*-
from flask import Flask, render_template, request ,send_file
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user,current_user
from flask_cors import CORS
import jwt
import datetime
import secrets
from flask_limiter import Limiter
import stripe
import re
import base64
import os

# app = Flask(__name__)
app = Flask(__name__, static_folder='templates/static', template_folder='templates')
# app = Flask(__name__, static_folder='templates')

# getのときの処理
@app.route('/', methods=['GET'])
def get():
	# return render_template('index.html')
	return send_file('templates/index.html')

if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0', port=80)