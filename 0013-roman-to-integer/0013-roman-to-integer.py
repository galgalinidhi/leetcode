class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {'I': 1, 'V': 5, 'X' : 10, 'L':50, 'C':100, 'D':500, 'M':1000}
        integer = 0
        i = 0
        while i< len(s):
            # print(integer)
            if i+1 < len(s) and s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                integer+= hashmap[s[i+1]] - hashmap[s[i]]
                i +=2
            elif i+1 <len(s) and s[i] == 'X' and (s[i+1]=='L' or s[i+1] == 'C'):
                integer+= hashmap[s[i+1]] - hashmap[s[i]]
                i+=2
            elif i+1 <len(s) and s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                integer+= hashmap[s[i+1]] - hashmap[s[i]]
                i+= 2
                
            else:
                integer+= hashmap[s[i]]
                i+=1
        return integer        
                
                