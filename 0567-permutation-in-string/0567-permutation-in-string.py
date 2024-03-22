class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = l+len(s1) - 1
        def freqarray(start,end,s):
            s2_freq = [0]*26
            for i in range(start,end+1):
                s2_freq[ord(s[i]) - ord('a')]+=1
            return s2_freq    
        s1_freq = freqarray(0,len(s1)-1,s1)
        
        while l<=r and r<len(s2):
            s2_freq = freqarray(l,r,s2)
            if s2_freq == s1_freq:
                return True
            else:
                l+=1
                r = l + len(s1) - 1
            
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         freq1= {}
#         freq2= {}
#         l=r=0
#         count = 0
        
#         for i in range(len(s1)):
#             freq1[s1[i]] = 1 + freq1.get(s1[i],0)
        
#         while l<=r and r<len(s2):
#             if freq1.get(s2[r],0)> 0:
#                 freq2[s2[r]] = 1+ freq2.get(s2[r],0)
#                 if (r-l+1) == len(s1):
#                     print(freq1)
#                     print(freq2)
#                     for k,v in freq1.items():
#                         if freq1[k]!= freq2.get(k,0):
#                             break
#                         count+=1    
#                     print(count)
#                     if count == len(freq1):
#                         return True
#                     else:
#                         l+=1
#                         r=l
#                         freq={}
#                 r+=1
        
#             l+=1
#             r=l
#             freq={}
#         return False    