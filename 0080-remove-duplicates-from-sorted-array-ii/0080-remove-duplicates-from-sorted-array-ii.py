class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = {}
      
        k = 0
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
            
        for key,value in hashmap.items():
            if hashmap[key]>=2:
                nums[k] = nums[k+1] = key
                k+=2
                
            else:
                nums[k] = key
                k+=1
        return k    