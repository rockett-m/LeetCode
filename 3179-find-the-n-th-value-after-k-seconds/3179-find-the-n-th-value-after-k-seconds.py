class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        m = [1]*n
        count = 1
        while count <= k:
            total = m[0]
            for i in range(1, len(m)):
                total += m[i]
                m[i] = total

            count += 1

        return m[-1] % (10**9 + 7)