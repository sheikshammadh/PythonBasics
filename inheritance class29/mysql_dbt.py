import requests
import pymongo
data = requests.get('https://dummyjson.com/products')
products=data.json()['products']

new_products=[]
for prod in products:
    new_products.append({
        'pid':prod['id'],
        'pname':prod['title'],
        'category':prod['category'],
        'price':prod['price'],
        'rating':prod['rating']
    })
try:
    cleint=pymongo.MongoClient('mongodb://localhost:27017')
    db=cleint['6pm']
    product_collection=db['products']
    product_collection.insert_many(new_products)
    print('products written successfully')
except:
    pass
finally:
    pass