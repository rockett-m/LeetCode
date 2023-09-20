class Solution:
    def repeatedCharacter(self, s: str) -> str: 
        my_dict = dict()
        for c in s:
            if c not in my_dict.keys():
                my_dict[c] = 1
            else:
                return c
        