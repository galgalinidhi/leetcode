class Solution:
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0
        visited = set()
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) \
            or grid[i][j] == 0:
                return 1
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            peri= dfs(i+1,j)
            peri+= dfs(i-1,j)
            peri+= dfs(i,j+1)
            peri+= dfs(i,j-1)
            return peri
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j)