# custs=[
#     {'eid':101,'name':'rahul','mob':9490061300},
#     {'eid':102,'name':'sonia','mob':9490061300}
# ]
# mobile_numbers=[]
# for cust in custs:
#     mobile_numbers.append(cust['mob'])

# print(mobile_numbers)

custs=[
    {'eid':101,'name':'rahul','mob':9490061300},
    {'eid':102,'name':'sonia','mob':9490061384},
    {'eid':103,'name':'shyam','mob':9490061300},
    {'eid':104,'name':'nandu','mob':9490061384},
    {'eid':105,'name':'somu','mob':9490061300},
    {'eid':106,'name':'nehru','mob':9490061384},
    {'eid':107,'name':'gandhi','mob':9490061300}
]
mobile_numbers=set()
for cust in custs:
     mobile_numbers.add(cust['mob'])
print(mobile_numbers)
