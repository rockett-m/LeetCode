from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0: return t
        # my_list = list(t)
        # for i in range(len(s)):
        #     if s[i] in my_list:
        #         my_list.pop(my_list.index(s[i]))                
        #     else:
        #         return s[i]
        # return my_list[0]
        res = Counter(t) - Counter(s)
        for k,v in res.items():
            if v == 1:
                return k
        return -1