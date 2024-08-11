from flask import Flask, render_template
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

usr = 'root'
pwd = 'root'
client = MongoClient("localhost", 27017)
db = client.admin
# print(db)
#db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
print(client.list_database_names())

student = db.students.find_one()
#print(student)

student = db.students.find_one({'_id':ObjectId('66b8d738b9013fc9d22785d8')})

query = {
    "country":"Finland"
}
students = db.students.find(query)
for student in students:
    print(student)


query = {'age': 250}
new_value = {'$set': {'age': 38}}

db.students.update_one(query, new_value)

db.students.delete_one(query)
db.students.drop()
