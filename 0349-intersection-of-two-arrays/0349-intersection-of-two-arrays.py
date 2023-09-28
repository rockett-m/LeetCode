class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # out = []
        # if len(nums1) >= len(nums2):
        #     for i in range(len(nums1)):
        #         if nums1[i] in nums2 and nums1[i] not in out:
        #             out.append(nums1[i])
        # else:
        #     for i in range(len(nums2)):
        #         if nums2[i] in nums1 and nums2[i] not in out:
        #             out.append(nums2[i])
        # return out
    
        return list(set(nums1) & set(nums2))