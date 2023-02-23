class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(list(str(num)))

        num1 = str(digits[0])
        num2 = str(digits[1])
        
        num1 = int(num1 + str(digits[3]))
        num2 = int(num2 + str(digits[2]))
        
        return num1 + num2
