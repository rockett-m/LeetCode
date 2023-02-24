class Solution:
    def isPerfectSquare(self, num: int) -> bool:
    
        for i in range(2**31):
            if i*i == num:
                return True
            elif i*i > num:
                return False