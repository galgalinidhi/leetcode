class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        nums = set(i for i in range(1,len(matrix)+1))
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                rows[r].add(matrix[r][c])
                cols[c].add(matrix[r][c])
       
        for i in range(len(matrix)):
            if rows[i] != nums or cols[i]!=nums:
                return False
        return True    
                