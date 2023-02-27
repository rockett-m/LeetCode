class Solution:
    def minPartitions(self, n: str) -> int:
        # print(sorted(list(n))[0])
        return int(sorted(list(n))[-1])
        # return max([int(x) for x in n])
