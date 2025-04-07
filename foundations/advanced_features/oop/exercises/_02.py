"""
Implement a Bank Account System:

- Create a class called BankAccount with attributes for account number, balance, and owner.
- Implement methods for depositing, withdrawing, and checking the balance.
- Create a subclass called SavingsAccount that inherits from BankAccount and adds an interest rate attribute.
"""


class BankAccount:
    def __init__(self, account: str, number: str, balance: float, owner: str) -> None:
        self.__account = account
        self.__number = number
        self.__balance = balance
        self.__owner = owner

    # Attributes
    @property
    def account(self) -> str:
        return self.__account

    @property
    def number(self) -> str:
        return self.__number

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def owner(self) -> str:
        return self.__owner

    @account.setter
    def account(self, account: str) -> None:
        self.__account = account

    @number.setter
    def number(self, number: str) -> None:
        self.__number = number

    @balance.setter
    def balance(self, balance: float) -> None:
        self.__balance = balance

    @owner.setter
    def owner(self, owner: str) -> None:
        self.__owner = owner

    # Methods
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError('Amount to deposit must be greater than 0')
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if not (0 < amount <= self.balance):
            raise ValueError('Cannot withdraw more than your balance')

        self.balance -= amount

    def check_balance(self):
        print(f'Your balance is {self.balance}')


class SavingsAccount(BankAccount):
    def __init__(self, account: str, number: str, balance: float, owner: str, interest: float) -> None:
        super().__init__(account, number, balance, owner)
        self.__interest = interest

    @property
    def interest(self) -> float:
        return self.__interest

    @interest.setter
    def interest(self, interest: float) -> None:
        self.__interest = interest

    def apply_interest(self) -> None:
        interest_amount = (self.balance) * (self.interest)
        self.balance += float(interest_amount)


if __name__ == '__main__':
    # Create a bank account
    account = BankAccount('Checking', '123456789', 1000.0, 'John Doe')
    print(
        f'Account: {account.account}, Number: {account.number}, Balance: {account.balance}, Owner: {account.owner}')

    # Deposit money
    account.deposit(500.0)
    print(f'New balance after deposit: {account.balance}')

    # Withdraw money
    account.withdraw(200.0)
    print(f'New balance after withdrawal: {account.balance}')

    # Check balance
    account.check_balance()

    # Create a savings account
    savings_account = SavingsAccount(
        'Savings', '987654321', 2000.0, 'Jane Doe', 0.05)
    print(f'Account: {savings_account.account}, Number: {savings_account.number}, Balance: {savings_account.balance}, Owner: {savings_account.owner}, Interest Rate: {savings_account.interest}')
