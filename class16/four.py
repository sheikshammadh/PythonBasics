from functools import reduce
prices=[100,200,300,400,500]
total=reduce(lambda a,b:a+b,prices)# with lambda
print(total)
#
#
prices=[100,200,300,400,500]
result=0
def sumof(a,b):
    return a+b
total=reduce(sumof,prices)# without lambda