class Solution:
    def fib(self, n: int) -> int:
        
        one = 0
        two = 1
        
        if n == 0:
            return 0
        
        for i in range(n-1):
            temp = one
            one = two
            two = temp + two
            
        return two     
            
            