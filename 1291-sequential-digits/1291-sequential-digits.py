class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
#         res = []
        
#         def checkdigits(n):
#             num = n
#             curr = n%10
#             n = n//10
#             while (n!=0):
#                 d = n%10
#                 if curr-d == 1:
#                     curr = d
#                     n = n//10
#                     continue
#                 else:
#                     return 0
#             return num
            
            
#         for i in range(low, high+1):
#             num = checkdigits(i)
#             if num!=0:
#                 res.append(num)
#         return res        

        sample = "123456789"
        n = 10
        nums = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(n - length):
                num = int(sample[start: start + length])
                if num >= low and num <= high:
                    nums.append(num)
        
        return nums