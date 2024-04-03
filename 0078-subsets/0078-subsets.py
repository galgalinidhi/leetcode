class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
          
    
        def backtrack(first = 0, curr = []):
            if len(curr) == k:
                res.append(curr[:])
                return
            # Len is not equal so I need to add more elements to it.
            
            for i in range(first,n):
                curr.append(nums[i])
                backtrack(i+1,curr)
                
                curr.pop()
        
        
        
        
        
        
        
        
        
        
        res = []
        n = len(nums)
        for k in range(n+1):
            backtrack()
            
        return res    