class bank:
    def __init__(self):
        self.bal=0

    def deposit(self,amt):
        self.bal+=amt
        return self.bal

    def withdraw(self,amt):
        self.bal-=amt
        return self.bal

a=bank()

a.deposit(int(input("Enter the amount:")))
print(a.bal,"is deposited")
a.withdraw(int(input("Enter the withdraw amount:")))
print(a.bal,"is withdraw")
