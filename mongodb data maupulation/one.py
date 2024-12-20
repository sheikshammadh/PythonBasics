#
class account:
    def __init__(self,id,name,amount):
        self.id=id
        self.acc_name=name
        self.acc_balance=amount
    def deposit_amount(self,amount):
        print()
    def update_min_bal(cls,amount):
        print()
    def calc_intrst():
        print()

a1=account(1,"shyam",50000)
a1.deposit_amount(5000)
a1.deposit_amount(5000)
print(a1.__dict__)

a2= account(2,"nandu",100000)
a2.deposit_amount(5000)
a2.deposit_amount(6000)
print(a2.__dict__)
