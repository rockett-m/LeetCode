class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        lp, rp = 0, len(arr)-1
        while lp < rp:
            if arr[lp] == 0:
                arr.insert(lp, 0)
                lp += 1
                arr[lp+1:] = arr[lp+1:-1]
            lp += 1