#python to json data type
import json
emp={
    'eid':101,
    'ename':'Rahul',
    'esal':45000.45,
    'avail':True,
    'loc':None
}
emp_str=json.dumps(emp)
print(emp_str)#{"eid": 101, "ename": "Rahul", "esal": 45000.45, "avail": true, "loc": null}