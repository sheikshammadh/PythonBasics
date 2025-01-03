#read the employees in the cvs and print htose belongs to bangalore
import csv
fp1=open('emp.csv','r')
csv_data=csv.reader(fp1)
employees=list(csv_data)

for employee_list in employees:
    if employee_list[3]=='Bangalore':
        print(employee_list[1])
fp1.close()

