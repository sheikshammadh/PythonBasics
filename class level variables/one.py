class employee:
    c=300
    def m1(self):
        self.a=100
    def m2(self):
        self.b=200
e1=employee()
e1.m1()#instance level variable   {a:100}
e2=employee()
e2.m2()#instance level variable   {b:200}
e1.m2()#instance level variable   {a:100,b:200}
print(e1.__dict__)#{}
print(e2.__dict__)#{}
print(employee.__dict__)#gives the class level variables in the form of dictionary