class Solution:
    def partitionString(self, s: str) -> int:

        my_dict = Counter(s)
        single = True
        for k,v in my_dict.items():
            if v > 1:
                single = False; break
        
        if single: return 1
        
        temp = []
        sub = ''
        for i in range(len(s)):
            if i == 0:
                sub = s[i]; continue
            if s[i] not in sub:
                sub += s[i]
            else:
                temp.append(sub)
                sub = s[i]
            if i == len(s) - 1:
                temp.append(sub)

        print(temp)
        return len(temp)
            