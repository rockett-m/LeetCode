class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        re = ''.join(s.split('-'))[::-1]
        rest = []
        for i in range(0, len(re), k):
            rest.append(re[i:i+k][::-1])
        
        return '-'.join(rest[::-1]).upper()
        