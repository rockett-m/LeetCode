class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        sp = s.split('-')
        
        # rem = s.split('-')[1:]
        re = ''.join(sp)[::-1]
        print(f'{re = }')
        rest = []
        for i in range(0, len(re), k):
            rest.append(re[i:i+k][::-1])
        
        out = rest[::-1]
        return '-'.join(out).upper()
        