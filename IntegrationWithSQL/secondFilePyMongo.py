import pprint

import pymongo as pym

cliente = pym.MongoClient("mongodb+srv://kevinsplourenco:6mAodUlzCrOY5mWz@cluster0.hopz2us.mongodb.net/?retryWrites"
                          "=true&w=majority")
db = cliente.test
posts = db.posts

# for post in posts.find():
#     pprint.pprint(post)

print(posts.count_documents({}))