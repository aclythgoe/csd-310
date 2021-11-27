"""
Andrew Lythgoe
Module 6 Assignment 3
"""

"""
Importing and defining
"""
from pymongo import MongoClient
url = 'mongodb+srv://admin:admin@cluster0.qghgj.mongodb.net/Cluster0?retryWrites=true&w=majority'
client = MongoClient(url)
db = client.pytech
students = db.students
students_list = students.find({})
students_list2 = students.find({})

"""
Display all student records
"""
print('\n -- DISPLAYING STUDENTS FROM find() QUERY -- ')
for doc in students_list:
    print('    Student ID: ' + doc["student_id"] + "\n    First Name: " + doc["first_name"] + "\n    Last Name: " + doc["last_name"] + "\n" )

"""
New student document and insert
"""
student_four = {
    'student_id' : '1010',
    'first_name' : 'John',
    'last_name' : 'Doe',
    'enrollments' : [
        {
            'term' : 'Summer 2022',
            'gpa' : "3.7",
            'start_date' : '05-07-2022',
            'end_date' : '08-14-2022',
            'courses' : [
                {
                    'course_id' : '415-J313',
                    'description' : 'Cybersecurity 4',
                    'instructor' : 'Professor Lappe', 
                    'grade' : 'F',
                },
                {
                    'course_id' : '416-J313',
                    'description' : 'Intro to Musical Biomechanics 101',
                    'instructor' : 'Helga Weinerschnitzel',
                    'grade' : 'B+'
                }
            ]
        }
    ]
}

print("\n --INSERT STATEMENTS --")

student_four_student_id = students.insert_one(student_four).inserted_id
print('Imported student record into the students collection with document ID' + str(student_four_student_id))

"""
Displaying student test doc
"""
student_four = students.find_one({"student_id" : "1010"})
print("\n -- DISPLAYING STUDENT TEST DOC --")
print("    Student ID: " + student_four["student_id"] + "\n    First Name: " + student_four["first_name"] + "\n    Last Name: " + student_four["last_name"] + "\n")

"""
Deleting test doc student
"""
deletion = { 'student_id' : '1010'}
students.delete_one(deletion)

"""
Display all student records
"""
print('\n -- DISPLAYING STUDENTS FROM find() QUERY -- ')
for this in students_list2:
    print('    Student ID: ' + this["student_id"] + "\n    First Name: " + this["first_name"] + "\n    Last Name: " + this["last_name"] + "\n" )

print("\n End of program, press any key to continue...")