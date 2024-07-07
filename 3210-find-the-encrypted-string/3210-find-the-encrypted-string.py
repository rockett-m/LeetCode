class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ans = ''
        for idx, c in enumerate(s):
            ans += s[(idx+k)%len(s)]

        return ans