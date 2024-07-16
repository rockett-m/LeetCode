class ATM:

    def __init__(self):
        self.balance = 0
        self.atm_bill_denoms = [20, 50, 100, 200, 500]
        self.atm_bill_counts = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount: List[int]) -> None:
        if sum(banknotesCount) == 0: return
        
        for denom, dep_count in enumerate(banknotesCount):
            self.atm_bill_counts[denom] += dep_count
        
        self.balance = sum([i*j for i, j in \
                            zip(self.atm_bill_denoms, self.atm_bill_counts)])
        print(self.balance)

    def withdraw(self, amount: int) -> List[int]:
        if amount == 0: return bills
        if amount > self.balance: return [-1]
        
        orig_balance = self.balance
        desired_amount = amount
        
        withdraw_bills = [0,0,0,0,0]

        for idx in range(len(withdraw_bills)):
            rev_idx = len(withdraw_bills) - 1 - idx

            denomination = self.atm_bill_denoms[rev_idx]
            if denomination > amount: continue

            num_bills_wanted = amount // denomination
            num_bills_withdrawn = min(num_bills_wanted, self.atm_bill_counts[rev_idx])
            self.atm_bill_counts[rev_idx] -= num_bills_withdrawn

            amount -= num_bills_withdrawn * denomination
            withdraw_bills[rev_idx] = num_bills_withdrawn

            # success
            if amount == 0: 
                self.balance -= desired_amount
                return withdraw_bills

        # failure - restore state
        if amount > 0:
            for idx, failed_wth_count in enumerate(withdraw_bills):
                self.atm_bill_counts[idx] += failed_wth_count
            self.balance = orig_balance

        return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)