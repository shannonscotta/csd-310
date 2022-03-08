from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.exc81.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech


students = db.students
student_list = students.find({})

# loop and print
def loop_docs():
    print("\n- - DISPLAYING STUDENT DOCUMENTS FROM THE find() QUERY - -")
    docs = students.find({})
    for doc in docs:
        print(f"Student Id: {doc['student_id']}")
        print(f"First Name: {doc['first_name']}")
        print(f"Last Name: {doc['last_name']}\n")

# method to find student by ID and print
def find_student():
    print("\n- - DISPLAYING STUDENT DOCUMENT FROM THE find_one() QUERY - -")
    result = students.find_one({"student_id": 1007})
    print(f"Student Id: {result['student_id']}")
    print(f"First Name: {result['first_name']}")
    print(f"Last Name: {result['last_name']}\n")

#call methods
loop_docs()
find_student()