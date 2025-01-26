class Solution:
    def isBalanced(self, num: str) -> bool:
        even = 0
        odd = 0
        for i in range(len(num)):
            # odd
            if i % 2 == 1:
                odd += int(num[i])
            # even
            else:
                even += int(num[i])

        return True if even == odd else False