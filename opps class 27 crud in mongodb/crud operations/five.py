from pymongo import MongoClient
cleint=MongoClient('mongodb://localhost:27017')
db=cleint['6pm']
user_col=db['users']
status=user_col.delete_many({'gender':'Female'})
print(status)
print("deleted siccesfully")