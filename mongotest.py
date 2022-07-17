import pymongo


client = pymongo.MongoClient("mongodb+srv://rama404:test123@cluster0.ygatu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name":"Mahi",
    "email" : "mahi@gmail.com",
    "surname" : "C",
    "Designation":"SDE1"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )

