    #CLASS FOR BANK

class bank:
    def __init__(self,name,acno,actype,address,balance):
        self.name = name
        self.acno = acno
        self.actype = actype
        self.address = address
        self.balance = balance

    #OBJECT DEPOSITE

    def deposite(self,balance,amount):
        self.balance += amount
        print('YOU DEPOSITED {self.amount}. CURRENT BALANCE: {self.balance}')

    #OBJECT WITHDRAW

    def withdraw(self,balance,amount):
        if amount > self.balance:
            print('INSUFFICIENT AMOUNT!!!')
        else:
            self.balance -= amount
            print('YOU WITHDRAWED {self.amount}. CURRENT BALANCE: {self.balance}')

    #MAIN PROGRAM
user = [ name, acno, actype, address, balance]
user.name = input('Enter your name: ')
user.acno = int(input('Enter your account number'))
user.actype = input('Enter account type')
user.address = int(input('Enter your address'))
user.balance = int(1000)
print('YOUR CURRENT BALANCE: 1000')

user = bank(name,acno,actype,address,balance)
n = int(input('DEPOSIT: 1 OR WITHDRAW: 2 ?'))
if n == 1:
    amount = int(input('Enter the amount to deposite: '))
    user.deposite(balance,amount)
elif n == 2:
    amount = int(input('Enter the amount to withdraw: '))
    user.withdraw(balance,amount)
else:
    print('IVALID INPUT!!')
    
    

