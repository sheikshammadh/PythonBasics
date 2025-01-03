import csv
import json
fp1 = open('oyees.csv','r')
fp2 = open('emp.json','w')
employees=list(csv.reader(fp1))
print(len(employees))
new_male_employees_filter_data=(lambda employee_list:emp_list[2]=='Male')
json.dump(
print("new file created")

fp1.close()
fp2.close()