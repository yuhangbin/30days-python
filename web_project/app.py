import json

from flask import Flask, render_template, request, redirect, url_for
import os

from mongodb import mongodb_day27
from bson.json_util import dumps


app = Flask(__name__)


@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='Home')


@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))


client = mongodb_day27.initMongoDB()
db = client.admin


@app.route('/insertStudent')
def insert():
    mongodb_day27.insertStudent(db)
    return '<h1> insert success</h1>'


@app.route('/findStudent')
def find():
    return dumps(mongodb_day27.findStudent(db))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 50000))
    app.run(debug=True, host='0.0.0.0', port=port)
