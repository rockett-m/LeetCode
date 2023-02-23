class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        streak = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                streak += 1
            else:
                streak = 0
            if streak >= 3:
                return True
        return False