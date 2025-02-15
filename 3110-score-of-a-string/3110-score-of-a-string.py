class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        if len(s) < 2:
            return 0

        slist = list(s)
        for j in range(1, len(slist)):
            x, y = ord(slist[j-1]), ord(slist[j])
            ans += abs(x - y)

        return ans