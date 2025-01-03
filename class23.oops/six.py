class Account:
    account_min_bal=500
    branch_name="marathalli"

    def despoit_amount(self,amount):
        self.account_min_bal=amount
a1=Account()
a1.despoit_amount(15000)

a2=Account()
a2.despoit_amount(20000)

print(a1.__dict__)
print(a2.__dict__)