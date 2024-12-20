import csv
fp1=open('emp.csv','r')
csv_data=csv.reader(fp1)
users=list(csv_data)
#print(users)#[['1', 'Rahul', 'Male', 'Wayanad', '45000'], ['2', 'Sonia', 'Female', 'New Delhi', '55000'], .....
for user_list in users:
    for user_data in user_list:
       print(user_data,end="  ")
   # print()#1  Rahul  Male  Wayanad  45000