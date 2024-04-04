class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       
        nums1copy = nums1[:m]
        ptr1 = 0
        ptr2 = 0
        for i in range(m+n):
            if ptr1>=len(nums1copy):
                nums1[i:] = nums2[ptr2:]
                break
            elif ptr2>=len(nums2):
                nums1[i:] = nums1copy[ptr1:]
                break
            else:
                if nums1copy[ptr1]<nums2[ptr2]:
                    nums1[i] = nums1copy[ptr1]
                    ptr1+=1
                else:
                    nums1[i] = nums2[ptr2]
                    ptr2+=1
                