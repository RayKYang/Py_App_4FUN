__author__ = 'rkzyang'

# import pymongo
#
# uri = "mongodb://127.0.0.1:"
# client = pymongo.MongoClient(uri)
# database = client['fullstack']
# collection = database['students']
#
# students = [student for student in collection.find({})] # list comprehension
# # students = [student['mark'] for student in collection.find({})]
# # students = [student['mark'] for student in collection.find({}) if student['mark] == 99.0]
#
# print(students)
#
# # OOP: everything(objects) can be decomposed a collection of properties

from Py_App_models_3.post import Post
from database_3 import Database

Database.initialize()

post = Post(blog_id="123",
            title="Another great post",
            content="This is some same contect",
            author="RKY")
