class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ''
        prev = ''
        for idx, val in enumerate(num):
            if 0 < idx < len(num)-1:
                ss = num[idx-1:idx+2]
                if len(set(ss)) == 1:
                    if ans == '':
                        ans = ss
                    elif int(ss) > int(ans):
                        ans = ss
        return ans