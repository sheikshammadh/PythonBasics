#write data into mongoDB
import pymongo #third party module.
#help(pymongo)

client=pymongo.MongoClient('mongodb://localhost:27017')
db=client['6pm']
col_name=db['users']
col_name.insert_one({'eid':1,"ename":"shyam"})
col_name.insert_one({'eid':2,"ename":"nandu"})
print("inserted successfully")
