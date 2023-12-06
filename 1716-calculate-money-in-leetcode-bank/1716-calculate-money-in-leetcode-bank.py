class Solution:
    def totalMoney(self, n: int) -> int:
        base = 0
        total = 0
        for i in range(1, n+1):
            days_left = n-1
            if (i-1) % 7 == 0:
                base += 1
            total += base+(i-1)%7
        
        return total