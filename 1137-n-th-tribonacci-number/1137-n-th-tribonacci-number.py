class Solution:
    def tribonacci(self, n: int) -> int:
        zero = 0
        one = 1
        two = 1
        
        if n == 0:
            return 0
        for i in range(n-2):
            temp1 = zero
            temp2 = one
            zero = one
            one = two
            two = temp1+ temp2 + two
            
        return two    