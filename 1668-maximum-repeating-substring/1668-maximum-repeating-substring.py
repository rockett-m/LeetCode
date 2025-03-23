class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        pattern = word
        while pattern in sequence:
            count += 1
            pattern += word

        return count