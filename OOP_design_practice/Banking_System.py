"""
Create a banking system that allow to withdraw, deposit, transfer

Get cashback 3% after 24h after despoit
"""


class BankAccount:
    def __init__(self, account_number: int, balance: int = 0) -> None:
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance = self.balance + amount

    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            print("FUCK OFF you broke AF!!!")
        else:
            self.balance = self.balance - amount

    def cash_back(self, amount: int) -> None:
        self.balance = self.balance + int(amount * 0.02)

    def transfer(self, amount: int, direction_account):
        if amount > self.balance:
            print("FUCK OFF you broke AF!!!")
        else:
            self.withdraw(amount=amount)
            direction_account.deposit(amount=amount)

    def display(self):
        print("Account Number : ", self.account_number)
        print("Account Balance : ", self.balance, " $")


if __name__ == '__main__':
    init = [1000, 1500]
    transactions = [
        "withdraw 1613327630 2 480",
        "withdraw 1613327644 2 800",
        "withdraw 1614105244 1 100",
        "deposit 1614108844 2 200",
        "withdraw 1614108845 2 150"
    ]

    # Create Account
    account = [BankAccount(idx, value) for idx, value in enumerate(init)]

    transactions = [trans.split(" ") for trans in transactions]

    last_trans = int(transactions[-1][1])

    for trans in transactions:
        if trans[0] == "withdraw":
            account[int(trans[2]) - 1].withdraw(int(trans[-1]))
            if (int(trans[1]) + 86400) < last_trans:
                account[int(trans[2]) - 1].cash_back(int(trans[-1]))
        elif trans[0] == "deposit":
            account[int(trans[2]) - 1].deposit(int(trans[-1]))

    for acc in account:
        acc.display()