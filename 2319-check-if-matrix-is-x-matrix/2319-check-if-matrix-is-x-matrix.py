class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                
                if r == c or ((r+c)==len(grid)-1):
                    if grid[r][c] == 0:
                        return False
                    continue
                if grid[r][c]!=0:
                    return False
        return True