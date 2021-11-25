"""
All Prerequisites
"""
from pymongo import MongoClient
url = 'mongodb+srv://admin:admin@cluster0.qghgj.mongodb.net/Cluster0?retryWrites=true&w=majority'
client = MongoClient(url)
db = client.pytech

"""
Student One's information
"""

student_one = {
    'student_id': '1007',
    'first_name' : 'Andrew',
    'last_name' : 'Lythgoe',
    'enrollments' : [
        {
            'term' : 'Fall 2021',
            'gpa' : '4.0',
            'start_date' : '8-21-2021',
            'end_date' : '12-07-2021',
            'courses' : [
                {
                    "course_id" : "410-J313",
                    "description" : "Cyber Security",
                    'instructor' : 'Professor Lappe',
                    'grade' : 'A'
                },
                {
                    'course_id' : '412-J313',
                    'description' : 'Cyber Security 3',
                    'instructor' : 'Professor Lappe',
                    'grade' : 'A'
                }
            ]
        }
    ]
}

"""
Student Two's information
"""
student_two = {
    'student_id' : '1008',
    'first_name' : 'Fake',
    'last_name' : 'Human',
    'enrollments' : [
        {
            'term' : 'Spring 2021', 
            'gpa' : "4.0",
            'start_date' : '01-02-2021',
            'end_date' : '05-05-2021',
            'courses' : [
                {
                     'course_id' : '411-J313',
                     'description' : 'Cybersecurity 2',
                     'instructor' : 'Professor Lappe', 
                     'grade' : 'A'
                },
                {
                    'course_id' : '413-J313',
                    'description' : 'Cybersecurity 4',
                    'instructor' : 'Professor Lappe',
                    'grade' : 'A'
                }
            ]
        }
    ]
}

"""
Student Three's information
"""

student_three = {
    'student_id' : '1009',
    'first_name' : 'Sylvester',
    'last_name' : 'Stallone',
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

students = db.students


    
print('\n --INSERT STATEMENTS --')

student_one_student_id = students.insert_one(student_one).inserted_id
print('Imported student record "Andrew Lythgoe" into the students collection with document ID' + str(student_one_student_id))

student_two_student_id = students.insert_one(student_two).inserted_id
print('Imported student record "Fake Human" into the students collection with document ID' + str(student_two_student_id))

student_three_student_id = students.insert_one(student_three).inserted_id
print('Imported student record for "Sylvestor Stallone into the students collection with document ID' + str(student_three_student_id))

print('\n End of program, press any key to exit...')