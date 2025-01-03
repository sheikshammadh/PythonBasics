
class account:
    def __init__(self,eid,ename,balance):
        self.eid=eid
        self.ename=ename
        self.account_balance=balance
    def deposit_amount(self,amount):
        self.account_balance=self.account_balance+amount
    def withdraw_amount(self,amount):
        self.account_balance=self.account_balance-amount

        
a1=account(101,"shyam",1000)
a2=account(102,"nandu",2000)

a1.withdraw_amount(500)
#print(a1.__dict__)#{eid:101,ename:shyam,account_balance:500}
a2.deposit_amount(3000)
#print(a2.__dict__)#{eid:102,ename:nandu,account_balance:5000}
a1.deposit_amount(200)
a2.withdraw_amount(500)
print(a1.__dict__)
print(a2.__dict__)