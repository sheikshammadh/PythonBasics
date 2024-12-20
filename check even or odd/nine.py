#printing list of even numbers from the list.
numbers=[10,23,404,343,5435,2,432,34,34]
def check(numbers):
   return numbers%2==0
even=list(filter(check,numbers))
print(even)#[10, 404, 2, 432, 34, 34]

#
numbers=[10,23,404,343,5435,2,432,34,34]
def check(numbers):
   return numbers%2 !=0
odd=list(filter(check,numbers))
print(odd)#[23, 343, 5435]