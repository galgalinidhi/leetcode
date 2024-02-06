class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
         
        for s in strs:
            k = [0]*26
            for ch in s:
                k[ord(ch)-ord('a')]+=1
               
            res[tuple(k)].append(s)
            
            
        return (res.values()) 