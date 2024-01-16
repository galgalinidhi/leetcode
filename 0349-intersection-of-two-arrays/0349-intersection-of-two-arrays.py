class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums2)):
            if nums2[i] in nums1 and nums2[i] not in res:
                res.append(nums2[i])
                
        return res  
                