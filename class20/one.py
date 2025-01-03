import csv 
fp=open('data.csv','r')
csv_data=csv.reader(fp1)
users=list(csv_data)

for user in users:
    for user_data in user_list:
        print(user_data,end=' ')
    
    print()

