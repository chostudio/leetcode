# Last updated: 10/26/2025, 4:49:31 PM
from collections import defaultdict

class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = defaultdict(int)
        self.n = len(balance) # like the max possible account numebr value

        # initial balance of each account is stored in a 0-indexed integer array balance, with the (i + 1)th account having an initial balance of balance[i].
        for i in range(len(balance)):
            self.accounts[i + 1] = balance[i]
        print(self.accounts)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account1 > self.n or account2 < 1 or account2 > self.n:
            return False
        if self.accounts[account1] - money < 0:
            return False
        self.accounts[account1] -= money
        self.accounts[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n:
            return False
        self.accounts[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n:
            return False
        if self.accounts[account] - money < 0:
            return False
        self.accounts[account] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)