eids={101,102,103,104,105,106,107}
eids.pop()
print(eids)


eids={101,102,103,104,105,106,107}
eids.remove(101)# removes 
print(eids)

eids={101,102,103,104,105,106,107}
eids.discard(101)# removes specified vlue from set.
print(eids)


eids={101,102,103,104,105,106,107}
eids.discard(104)
print(eids)


eids={'rahul','sonia','modi','priyanka'}
eids.pop()
print(eids)

eids={'rahul','sonia','modi','priyanka'}
eids.remove('modi')
print(eids)

enames={'rahul','sonia','modi','priyanka'}
enames.remove('amit')
print(enames)

# update and add:
enames={'rahul','sonia','modi','priyanka'}
enames.add('amit')
print(enames)

s1={10,20,30,40,50}
s2={10,20,30,40,50,60}
s1.intersection(s2)
print(s2)

s1={10,20,30,40,50}
s2={10,20,30,40,50,60}
s1.difference(s2)
print(s2)

s1={10,20,30,40,50}
s2={10,20,30,40,50,60}
s1.sysytematicdiffrence(s2)
print(s2)

s1={10,20,30,40,50}
s2={10,20,30,40,50,60}
s1.difference(s2)
print(s2)


d1={}
d2={1:'one',2:'two',3:'three'}
print(d1)
print(d2)

d1={}
d2={1:'one',2:'two',3:'three'}
d3={'name':'shyam',
    'name':'shyam',
    'name':'nandu'
   }
print(d1)
print(d2)
print(d3)


emp={
    'eid':'101',
    'ename':'rahul',
    'esal':'45000'
}
user=dict
print(type('eid')
print(type('ename')
print(type('esal')
      
emp=[
    {'id':101,'ename':'rahul'},
    {'id':102,'ename':'soniya'},
    {'id':103,'ename':'priya'}
     ]
for employee in emp: # Correct iteration over the emp list 
    print(employee['ename'])


    employee=[
    {'id':101,'ename':'rahul','gender':'male'},
    {'id':102,'ename':'soniya','gender':'female'},
    {'id':103,'ename':'priya','gender':'female'}
     ]
for emp in employee: # Use 'emp' or 'e' to avoid overwriting the original 'employee' list name
    print(emp.get('ename'))