class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                ptr1 = i
                ptr2 = 0
                while ptr2<len(needle) and ptr1<len(haystack):
                    if haystack[ptr1] == needle[ptr2]:
                        ptr1+=1
                        ptr2+=1
                    else:
                        break
                if ptr2 == len(needle):
                    return i
                else:
                    continue
        return -1             
                    
                
                