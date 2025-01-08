from pymongo import MongoClient
cleint=MongoClient('mongodb://localhost:27017')
db=cleint['6pm']
user_col=db['users']
users=user_col.find()
for user in users:
    print(user['gender'], user['first_name'])