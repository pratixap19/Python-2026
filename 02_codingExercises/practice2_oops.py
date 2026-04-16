#create account class with 2 attributes-balance&account no.
#Create methods for debit, credit and printing the balance.

class Account:
    
    def __init__(self, bal, accId):
        self.balance=bal
        self.account_no=accId
        
    def debit(self, amount):
        self.balance -= amount
        print("$", amount, "was debited")
        print("Total balance = ", self.get_balance())
        
    def credit(self, amount):
        self.balance += amount
        print("$" , amount, "was added")
        print("Total balance = ", self.get_balance())
        
    def get_balance(self):
        return self.balance
        
acc1 = Account(10000,12345)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
print("Balance is = ", acc1.get_balance())
