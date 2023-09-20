class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            mid = len(w) // 2 # floor div
            if len(w) % 2 == 0: # even
                if w[0:mid] == w[mid:][::-1]:
                    return w
            else:
                if w[0:mid] == w[mid+1:][::-1]:
                    return w
        return ''