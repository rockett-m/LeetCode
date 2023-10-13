class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = -1
        for t in s.split(' '):
            if t.isnumeric():
                if int(t) > prev:
                    prev = int(t)
                else:
                    return False

        return True