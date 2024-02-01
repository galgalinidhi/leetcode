class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        l = 0
        c = 1
        r = 1
        index = 0
        number_of_subarrays = len(nums)//3
        res = [[]*3 for i in range (number_of_subarrays)]
        
        while l< r and l<len(nums) and r< l+3:
            
            if nums[r]-nums[l]>k:
                return []
    
            c+=1 
            r+=1
          
            if c == 3:
                res[index] = nums[l:r]
                l = r 
                r = l+1
                c = 1
                index+=1
                
        return res         