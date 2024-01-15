import datetime
import pprint

import pymongo as pyM

# conectado
client = pyM.MongoClient("mongodb+srv://wordshinigam:testeteste123@cluster0.n1r2g50.mongodb.net/?retryWrites=true&w=majority")
db = client.test
posts = db.posts

print("Recuperando os documentos presentes na coleção posts")
for post in posts.find():
    pprint.pprint(post)

print(posts.count_documents({}))
print(posts.count_documents({"author": "Words"}))
print(posts.count_documents({"tags": "insert"}))

pprint.pprint(posts.find_one({"tags": "insert"}))

print("\nRecuperando info da coleção post de maneira ordenada")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)

