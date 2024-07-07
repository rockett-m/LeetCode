class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ans = ''
        for idx in range(len(s)):
            ans += s[(idx+k)%len(s)]

        return ans