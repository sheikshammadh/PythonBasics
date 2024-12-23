
numbers=[10,23,404,343,5435,2,432,34,34]
def check(numbers):
   return numbers%2==0
even=list(filter(lambda num:num%2==0,numbers))
print(even)
#
#numbers=[10,23,404,343,5435,2,432,34,34]
def check(numbers):
   return numbers%2 !=0
odd=list(filter(lambda num:num%2 !=0,numbers))
print(odd)