import requests
import csv
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
fp=open('product.csv','w')
csvwriter=csvwriter()
csvwriter.writerow(['pid','pname','category','price','rating'])
for product in new_products:
    csvwriter.write([product['id'],product['pname'],product['category'],product['price'],product['rating']])
    print('new csv file is created succed=sfully')