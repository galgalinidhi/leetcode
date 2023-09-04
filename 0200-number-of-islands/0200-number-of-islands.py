class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows= len(grid)
        columns = len(grid[0])
        islands = 0
        visited = set()
     
        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                r1,c1 = q.popleft()
                directions =[[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    if(r1+dr) in range(rows) and (c1+dc) in range(columns) and (r1+dr,c1+dc) not in visited and grid[r1+dr][c1+dc]=='1':
                        q.append((r1+dr,c1+dc))
                        visited.add((r1+dr,c1+dc))
                    
            
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] =="1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands