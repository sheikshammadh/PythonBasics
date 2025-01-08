from pymongo import MongoClient
cleint=MongoClient('mongodb://localhost:27017')
db=cleint['6pm']
user_col=db['users']
male_users=user_col.find({'gender':'Male'})

for user in male_users:
    print(user['id'], user['first_name'], user['gender'])