class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        valid = []
        for i in range(len(nums)):
            if nums[i] !=val:
                valid.append(nums[i])
                k+=1
        for i in range(0,k):
            nums[i]=valid[i]
        return k 