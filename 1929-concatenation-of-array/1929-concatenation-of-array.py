class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        c = 0 
        ans = [] 
        while(c!=2):
            for i in range (len(nums)):
                ans.append(nums[i])
            c+=1
        return ans   