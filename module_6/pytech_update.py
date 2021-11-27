"""
Importing and connecting to Students collection
Defining variables
"""
from pymongo import MongoClient
url = 'mongodb+srv://admin:admin@cluster0.qghgj.mongodb.net/Cluster0?retryWrites=true&w=majority'
client = MongoClient(url)
db = client.pytech
students = db.students
students_list = students.find({})

"""
Printing previously stored names
"""

print('\n -- DISPLAYING STUDENTS FROM find() QUERY -- ')
for doc in students_list:
    print('    Student ID: ' + doc["student_id"] + "\n    First Name: " + doc["first_name"] + "\n    Last Name: " + doc["last_name"] + "\n" )

"""
Creating the filter and values to be called
"""
filter = { 'student_id' : '1007'}
newvalues = { "$set" : { 'last_name' : 'Something Different Than The Originally Saved Name'}}

students.update_one(filter, newvalues)

"""
Printing updated student information for student 1007
"""
student_one = students.find_one({"student_id" : "1007"})
print('\n -- DISPLAYING STUDENT DOCUMENT 1007 ---')
print("  Student ID: " + student_one["student_id"] + "\n  First Name: " + student_one["first_name"] + "\n  Last Name: " + student_one["last_name"] + "\n")
