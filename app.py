import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)

db = client[DB_NAME]

app = Flask(__name__)

#Get Request ke index.html
@app.route('/', methods=['GET'])
def home():
   return render_template('index.html')

#Get Request ke about.html
@app.route('/about', methods=['GET'])
def about():
   return render_template('about.html')

#GET info ke my_name
@app.route('/info', methods=['GET'])
def get_info():
    my_name = request.args.get('my_name')
    print(my_name)
    return jsonify({ 
        'msg': 'GET info!!'
    })

#POST info ke my_name
@app.route('/info', methods=['POST'])
def post_info():
    my_name = request.form['my_name']
    print(my_name)
    return jsonify({ 
        'msg': 'POST info!!'
    })

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)