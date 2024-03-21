class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        visited = set()
        diag_sum = 0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if (r == c or (r+c)==len(mat)-1) and (r,c) not in visited:
                    diag_sum+= mat[r][c]
                    visited.add((r,c))
                    
        return diag_sum       
                    