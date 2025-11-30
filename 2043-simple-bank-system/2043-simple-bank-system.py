class Bank:

    def __init__(self, balance: List[int]):
        self.balance: List[int] = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # a1, a2 = account1, account2
        # Lack of coverage - an the account number can be the same for account1 and account2
        # if not (1 <= min(a1, a2) and max(a1, a2) <= len(self.balance) and a1 != a2):
        if not (1 <= min(account1, account2) and max(account1, account2) <= len(self.balance)):
            # del a1, a2
            return False

        if self.balance[account1-1] - money < 0:
            return False

        self.balance[account1-1] -= money
        self.balance[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not (1 <= account <= len(self.balance)):
            return False

        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not (1 <= account <= len(self.balance)) or \
            self.balance[account-1] - money < 0:
            return False

        self.balance[account-1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)