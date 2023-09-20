class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row = len(grid)
        column = len(grid[0])
        visited = set()
        island = 0
        
        
        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            direct = [[0,1],[0,-1],[-1,0],[1,0]]
            
            while q:
                r1, c1 = q.popleft()
                for r2,c2 in direct:
                    r= r1+r2
                    c= c1+c2
                    if r < row and c< column and ((r,c)) not in visited and r>=0 and c>=0 and grid[r][c]=="1":
                        visited.add((r,c))
                        q.append((r,c))
                        
        for r in range(row):
            for c in range(column):
                if (r,c) not in visited and grid[r][c] =="1":
                    bfs(r,c)
                    island+=1
    
        return island