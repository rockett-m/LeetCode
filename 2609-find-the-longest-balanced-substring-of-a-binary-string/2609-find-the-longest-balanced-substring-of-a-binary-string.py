class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        if '0' not in s:
            return 0

        longest = 0
        zero_streak = 0
        one_streak = 0
        for idx, i in enumerate(s):
            if i == '0':
                if one_streak > 0:
                    zero_streak = 0
                    one_streak = 0
                zero_streak += 1
            else:
                one_streak += 1
                if zero_streak >= one_streak and 2*one_streak > longest:
                    longest = 2*one_streak
                
        return longest
            