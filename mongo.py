import pymongo

client = pymongo.MongoClient("mongodb+srv://souravpratik:Yubu6&#202@arya.toxr4.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"sourav",
    "mail":"sourav@gmail.com",
     "last name" : "pratik"
}

db1= client ['mongo']
coll=db1['test']
coll.insert_one(d)