class test:
    def __init__(self,a,b):
        print(a,b)
    def m1(self):# if adding an another arguments in the method then it will give an error(type error)
        print("instance method")
    @classmethod
    def m2(self):
        print("class method")
t1=test(10,20)
t2=test(100,200)
t1.m1()
t2.m2()
t1.m2()
t2.m1()