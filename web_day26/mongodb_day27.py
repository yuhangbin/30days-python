from flask import Flask, render_template
import os
from pymongo import MongoClient
usr = 'root'
pwd = 'example'
url = '127.0.0.1:27017'
MONGODB_URI = "mongodb://" + usr + ":" + pwd + "@" + \
    url + "/admin?authSource=admin&retryWrites=true&w=majority"
client = MongoClient(MONGODB_URI)
try:
    client.admin.command('ping')
    print("connected")
except Exception as e:
    print(e)