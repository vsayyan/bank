class InsufficientFundsError(Exception):
    """Raised when an account does not have enough money."""

class Account:
    bank_name = "Python Bank"

    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise InsufficientFundsError("Not enough money on the account")
        self._balance -= amount
    def __str__(self):
        return f"{self.owner}: {self.balance}"

    def transfer(self,other,amount):
        self.withdraw(amount)
        other.deposit(amount)

class SavingsAccount(Account):
    def __init__(self, owner, balance=0,interest_rate=0.05):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        if interest > 0:
            self.deposit(interest)


        