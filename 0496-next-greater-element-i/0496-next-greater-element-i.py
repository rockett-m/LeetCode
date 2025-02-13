class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = [-1]*len(nums1)
        for i in range(len(nums1)):

            found = False
            for j in range(nums2.index(nums1[i]), len(nums2)):
                if nums1[i] == nums2[j]:
                    found = True
                    continue

                if found and nums2[j] > nums1[i]:
                    out[i] = nums2[j]
                    break

        return out