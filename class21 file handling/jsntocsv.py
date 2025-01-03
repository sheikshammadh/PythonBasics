import json
import csv
fp1 = open('json.csv','r')
fp2 = open('json.json','w')
emp_data =json.load(fp1)
print(emp_data)
json.dump(emp_data,fp2)
fp1.close()
fp2.close()
