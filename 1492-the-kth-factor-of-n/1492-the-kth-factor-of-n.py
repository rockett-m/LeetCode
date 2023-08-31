class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        my_li = []
        for i in range(1, n+1):
            if n % i == 0:
                my_li.append(i)
        
        if len(my_li) < k: return -1
        
        return my_li[k-1]