class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        res = set()
        for i in range(len(nums1)):
            freq[nums1[i]] = 1+ freq.get(nums1[i], 0)
        
        for j in range(len(nums2)):
            if freq.get(nums2[j], 0)>0:
                res.add(nums2[j])
        
        return list(res)        