class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []
        
        def backtrack(li: list, total: int, idx: int):
            if total == target:
                combos.append(li.copy())
                return
            
            elif total > target:
                return

            for idx in range(len(candidates)):
                if not li or li and candidates[idx] >= li[-1]:
                    li.append(candidates[idx])
                    backtrack(li, total + candidates[idx], idx)
                    li.pop()

        backtrack([], 0, 0)

        return combos