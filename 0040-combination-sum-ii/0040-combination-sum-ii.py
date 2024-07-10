class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []
        candidates.sort()
        
        if sum(candidates) < target: return combos

        def backtrack(li: list, total: int, idx: int):
            if total > target:
                return
            elif total == target:
                if li not in combos:
                    combos.append(li.copy())
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                li.append(candidates[i])
                backtrack(li, total + candidates[i], i+1)
                li.pop()

        backtrack([], 0, 0)
        
        return combos
