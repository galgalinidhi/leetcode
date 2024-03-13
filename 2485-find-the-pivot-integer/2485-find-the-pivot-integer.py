class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = 0
        left_sum = 0
        for i in range(1,n+1):
            total_sum+=i
        right_sum = total_sum
        
        for i in range(1,n+1):
            left_sum+=i
            right_sum-=i
            if left_sum >=right_sum:
                if left_sum == right_sum+i:
                    return i
        return -1    
            