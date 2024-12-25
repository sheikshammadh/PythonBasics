def smart_div(func):
    def inner(a,b):
        if b==0:
            print("cannot devide by zero")
        else:
            func(a,b)
        return inner

@smart_div
def calc(a,b):
    print(a/b)
    
calc(50,2)
calc(50,2)
calc(50,5)
calc(50,0)