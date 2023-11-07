class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        if len(set(arr)) < k: return ''
        
        dist = Counter(arr)
        uniq = []
        count = 0
        for idx, a in enumerate(arr):
            if dist[a] == 1:
                uniq.append(a)
                count += 1

        if len(set(uniq)) < k: return ''

        return uniq[k-1]