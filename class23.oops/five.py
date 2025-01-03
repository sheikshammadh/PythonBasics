class Account:
    account_min_bal=500
    branch_name="marathalli"
    def open_acc(self):
        print("Account opened sucessfully")
    def despoit_amount(self):
        print("amount despoited")
    def withdrawl(self):
        print("amount withdrawl")
    def close_accont(self):
        print("account closed sucessfully")
a1=Account()
a1.open_acc()
a1.despoit_amount()
a1.withdrawl()
a1.close_accont()
