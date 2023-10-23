class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        out = []
        count = 0
        for i in range(0, len(s), k):
            if count % 2 == 0:
                out.append(s[i:i+k][::-1])
            else:
                out.append(s[i:i+k])
            count += 1
        return ''.join(out)
            