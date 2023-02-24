class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0: return t
        my_list = list(t)
        for i in range(len(s)):
            if s[i] in my_list:
                idx = my_list.index(s[i])
                my_list.pop(idx)                
        
        return my_list[0]