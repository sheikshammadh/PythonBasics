# write python scirpt to read employees.json file
# and write only male/female employees into
# new file ie male.json or female.json file
file=open('employees.json','r')
print(file.read())
file.close()

