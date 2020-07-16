from flask import Flask,Blueprint, render_template, request, jsonify, redirect, url_for
from flask_login import login_user,logout_user,login_required
import hashlib
import base64
import binascii
import json
import datetime
from pathlib import Path
from pymongo import MongoClient
import requests
from flask_cors import CORS


import requests

app = Flask(__name__)
CORS(app)

import os

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')  

if __name__ == '__main__':
   app.run(host='localhost',port="3000")

    

    



  

  

