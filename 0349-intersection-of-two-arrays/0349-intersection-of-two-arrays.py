class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = set()
        if len(nums1) >= len(nums2):
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    out.add(nums1[i])
        else:
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    out.add(nums2[i])         
        return out