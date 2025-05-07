class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']

        for idx, val in enumerate(s):
            if val in vowels:
                count += 1

        return False if count == 0 else True

        # Alice can't move
        # if count == 0: return False
        # leaves Bob no letters left - delete entire string
        # if count % 2 == 1: return True

        # return True
        # 2+ even count of vowels
        # let Alice delete all vowels and cons after up until final vowel
        # forces Bob to delete 1 vowel which he isn't allowed to do - loses
        