class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False

        word = word.lower()
        vmatch = False
        for v in 'aeiou':
            if v in word:
                vmatch = True
                break

        if not vmatch: return False

        cons_match = False
        for w in word:
            if w in 'bcdfghjklmnpqrstvwxyz':
                cons_match = True
                break

        if not cons_match: return False

        # digits 48-57 ascii, lowercase lets 97-122
        for l in word:
            asciil = ord(l)
            if not ((48 <= asciil <= 57) or (97 <= asciil <= 122)):
                return False

        return True