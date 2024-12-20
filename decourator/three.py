def smart_div(func):
    def inner(a,b):
        if b==0:
            print("cannot devide by zero")
        else:
            func(a,b)
        return inner

def calc(a,b):
    print(a/b)
calc(50,5)#10.0
calc(50,2)#25.0
calc(50,1)#50.0
calc(50,0)#ZeroDivisionError: division by zero