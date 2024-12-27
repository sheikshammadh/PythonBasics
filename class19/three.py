import json
fp=open('employees.json','r')
employees=json.load(fp)
# print(type(employees))
# print(len(employees))


for emp in employees:
    if emp['gender']=='male':
        print(emp[ename])