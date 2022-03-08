from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.exc81.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print("")
print("- - Pytech COlection List - -")
print(db.list_collection_names())
print("")
input("   End of program, press any key to exit...")
