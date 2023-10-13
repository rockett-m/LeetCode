class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = []
        for t in s.split(' '):
            if t.isalpha():
                continue
            if len(nums) == 0:
                nums.append(int(t))
            else:
                if nums[-1] < int(t):
                    nums.append(int(t))
                else:
                    return False

        return True