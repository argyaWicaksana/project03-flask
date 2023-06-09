import os
from os.path import join, dirname
from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv

app = Flask(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]


@app.route('/')
def main():
    return render_template("index.html")

@app.route('/map')
def map():
    return render_template("prac_map.html", token=ACCESS_TOKEN)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
