class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        out = ''
        for idx, val in enumerate(word):
            if val == ch:
                out = word[:idx+1][::-1] + word[idx+1:]
                return out
        return word