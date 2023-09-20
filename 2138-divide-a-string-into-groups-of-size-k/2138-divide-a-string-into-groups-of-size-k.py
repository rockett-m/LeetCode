class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        out = []
        rem = len(s) % k
        if rem != 0:
            s += fill*(k-rem) # append any filler letters

        for idx, val in enumerate(s):
            if idx+k-1 < len(s) and idx % k == 0:
                out.append(s[idx:idx+k])
        return out