class account:
    def __init__(self):
        print("constructor method")
    def m1(self):
        print("instance method")
    @classmethod
    def m2(cls):
        print("class method")
    @staticmethod
    def m3():
        print("static method")
a1=account()#constructor method (in the first object creation)it will invoke automatically.
a2=account()#constructor method
a3=account()#constructor method