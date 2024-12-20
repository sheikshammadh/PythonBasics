# numbers=[10,23,404,343,5435,2,432,34,34]
# def check(numbers):
#     if numbers %2==0: no need to write aal there if st.
#         return True
#     else:
#         return False
# even=filter(check,numbers)
# print(list(even))


numbers=[10,23,404,343,5435,2,432,34,34]
def check(numbers):
   return numbers%2==0
   return True
even=filter(check,numbers)
print(list(even))