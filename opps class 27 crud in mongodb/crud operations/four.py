from pymongo import MongoClient
cleint=MongoClient('mongodb://localhost:27017')
db=cleint['6pm']
user_col=db['users']
Female_users=user_col.find({'gender':'Female'})

for user in Female_users:
    print(user['id'], user['first_name'], user['gender'])