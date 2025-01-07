class account:
    min_bal=500
    def __init__(self,id,name,amount):
        self.id=id
        self.acc_name=name
        self.acc_balance=amount
    def  get_balance(self):
        bal=self.acc_balance-self.min_bal
        return bal
    def deposit_amount(self,amount):
        self.acc_balance=self.acc_balance+amount
    def update_min_bal(cls,amount):
        pass
    def calc_intrst():
        pass
a1=account(1,"shyam",5000)
a1.deposit_amount(500)
print(a1.__dict__)
print("account holder name",a1.get_balance())
a2=account(2,"nandu",5000)
a2.deposit_amount(500)
print(a1.__dict__)
print("account holder name",a2.get_balance())