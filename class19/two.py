file1=open('employees.json','r')
data=file1.read()
file2=open('list.json','w')
file2.write(data)
print("file created")