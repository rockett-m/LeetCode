class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
        self.count = 0
        self.num1 = num1
        self.num2 = num2
        
        while (self.num1 != 0) and (self.num2 != 0):
            if self.num1 >= self.num2:
                self.num1 -= self.num2
            else:
                self.num2 -= self.num1
            self.count += 1

        return self.count
