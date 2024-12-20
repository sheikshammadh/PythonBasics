def cal(a,b):
    print(a-b)


cal(a=100,b=50)  #50
cal(b=50,a=100)  #50  (keyword arguments)
#cal(b=-50,a=100)  #150  100-(-50)
#cal()      #TypeError: cal() missing 2 required positional arguments: 'a' and 'b'
