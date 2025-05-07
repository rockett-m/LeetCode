class Solution:
    def doesAliceWin(self, s: str) -> bool:

        return False if s.count('a') + \
                        s.count('e') + \
                        s.count('i') + \
                        s.count('o') + \
                        s.count('u') == 0 \
        else True

        # Alice can't move
        # if count == 0: return False
        # leaves Bob no letters left - delete entire string
        # if count % 2 == 1: return True

        # return True
        # 2+ even count of vowels
        # let Alice delete all vowels and cons after up until final vowel
        # forces Bob to delete 1 vowel which he isn't allowed to do - loses
        