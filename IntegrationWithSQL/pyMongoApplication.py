import datetime
import pprint

import pymongo as pym

cliente = pym.MongoClient("mongodb+srv://kevinsplourenco:6mAodUlzCrOY5mWz@cluster0.hopz2us.mongodb.net/?retryWrites=true&w=majority")

db = cliente.test
collection = db.test_collection

# criando info que irá compor minha doc

post = {
    'author': 'Kevin',
    'text': 'My first mongodb application based on python',
    'tags': ['mongodb', 'python3', 'pymongo'],
    'date': datetime.datetime.utcnow()
}

# preparando para submeter as infos

posts = db.posts
post_id = posts.insert_one(post).inserted_id
# print(post_id)

# pprint.pprint(db.posts.find_one())

# bulk inserts

new_posts =[{
    'author': 'Kevin',
    'text': 'Another post',
    'tags': ['bulk', 'python3', 'insert'],
    'date': datetime.datetime.utcnow()
},
    {
        'author': 'Camila',
        'text': 'Another post again',
        'title': 'Mongo is fun',
        'date': datetime.datetime.utcnow()
    }
]

result = posts.insert_many(new_posts)

# pprint.pprint(db.posts.find_one({'author': 'Camila'}))

for post in posts.find():
    pprint.pprint(post)