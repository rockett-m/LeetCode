class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        out = ''
        for w in words:
            out += w[0]
        if out == s:
            return True
        return False