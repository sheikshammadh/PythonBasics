# class account:
#     def __init__(self,eid,ename,amount):
#         self.eid=eid
#         self.ename=ename
#         self.amount=amount
#          
# a1=account(101,"shyam",1000)
# print(a1.__dict__)#{eid:101,ename:shyam,amount:1000}
# a2=account(102,"nandu",2000)
# print(a2.__dict__)#{eid:102,ename:nandu,amount:2000}

class account:
    def __init__(self,eid,ename,amount):
        self.eid=eid
        self.ename=ename
        self.amount=amount
    def deposit_amount(self,amount):
        self.amount+=amount
        print("total amount after depositing:",self.amount)
        
a1=account(101,"shyam",1000)
print(a1.__dict__)
a2=account(102,"nandu",2000)
print(a2.__dict__)


a1.deposit_amount(4000)
a2.deposit_amount(1000)
print(a1.__dict__)
print(a2.__dict__)