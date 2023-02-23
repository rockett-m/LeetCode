class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest = 0
        for i in range(len(accounts)):
            sum = 0
            for j in range(len(accounts[i])):
                sum += accounts[i][j]
            if sum > highest:
                highest = sum
        return highest