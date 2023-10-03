class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        out = []
        for num in range(left, right+1):
            ok = True
            if '0' in list(str(num)):
                ok = False
                continue
            for i in str(num):
                if num % int(i) != 0:
                    ok = False
            if ok:
                out.append(num)
                ok = False
        return out