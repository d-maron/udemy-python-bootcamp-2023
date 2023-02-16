class Account:

    def __int__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Withdrawal cannot exceed current balance ({self.balance})')
        else:
            self.balance -= amount
