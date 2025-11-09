        #Class of bak

class bank:
    def __init__(self, name, acno, actype, address, balance):
        self.name = name1
        self.acno = acno1
        self.actype = actype1
        self.address = address1
        self.balance = balance1

        #Display Details

    def display(self):
        print("NAME:", self.name,"\nACCOUNT NUMBER:", self.acno,"\nACCOUNT TYPE:", self.actype,"\nADDRESS:", self.address,"\nBALANCE:", self.balance)

        #Object deposite

    def deposte(self, balance, amount):
        self.balance += amount
        print("YOU DEPOSITED:", amount, ". CURRENT BALANCE:", self.balance)

        #Object withdraw

    def withdraw(self, balance, amount):
        if amount > self.balance:
            print("INSUFFICIENT AMOUNT!!")
        else:
            self.balance -= amount
            print("YOU WITHDRAWED:", amount, ".CURRENT BALANCE:", self.balance)

        #Main Program

name1 = input("Enter your name: ")
acno1 = int(input("Enter your account number: "))
actype1 = input("Enter account type: ")
address1 = input("Enter your address: ")
balance1 = 1000
print("YOUR CURRENT BALANCE: 1000")

user = bank(name1, acno1, actype1, address1, balance1)

while True:
    n = int(input("\nDISPLAY YOUR DETAILS: 1 / DEPOSITE: 2 / WITHDRAW: 3 / EXIT: 4\n"))

    if n == 1:
        user.display()
    elif n == 2:
        amount1 = int(input("Enter the amount to deposte: "))
        user.deposte(balance1, amount1)
    elif n == 3:
        amount1 = int(input("Enter the amount to withdraw: "))
        user.withdraw(balance1, amount1)
    elif n == 4:
        break
    else:
        print("INVALID INPUT")
