import datetime
import pprint

import pymongo as pyM

# conectado
client = pyM.MongoClient("mongodb+srv://wordshinigam:testeteste123@cluster0.n1r2g50.mongodb.net/?retryWrites=true&w=majority")

# criar o banco
db = client.test
collection = db.test_collection

# print na coleção (tá vazia)
print(db.test_collection)

# definição de infor para compor o doc
post = {
    "author": "Words",
    "text": "My first mongodb application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# preparando para submeter as infos
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

print(db.posts)
print(db.list_collection_name)
print(db.list_collection_names())
print(db.posts.find_one())

pprint.pprint(db.posts.find_one())

# bulk inserts
new_posts = [{
        "author": "Mike",
        "text": "Another post",
        "tags": ["bulk", "posts", "insert"],
        "date": datetime.datetime.utcnow()},
    {
        "author": "Pedro",
        "text": "Post from Pedro. New post available",
        "title": "Mongo is ok",
        "date": datetime.datetime(2010, 11, 10, 10, 45)}]

result = posts.insert_many(new_posts)
print(result.inserted_ids)
print("\nRecuperação final: ")
pprint.pprint(db.posts.find_one())
pprint.pprint(db.posts.find_one({"author": "Words"}))  # recupera a primeira ocorrência de

print("\nDocumentos presentes na coleção posts")
for post in posts.find():
    pprint.pprint(post)
