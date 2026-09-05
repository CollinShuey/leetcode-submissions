from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visited = set()
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visited or grid[r][c] == "0":
                    continue
                visited.add((r,c))
                q.append((r,c))
                while q:
                    nr, nc = q.popleft()
                    if (nr+1,nc) not in visited and nr+1 >= 0 and nr+1 < ROWS and grid[nr+1][nc] == "1":
                        visited.add((nr+1,nc))
                        q.append((nr+1,nc))
                    if (nr-1,nc) not in visited and nr-1 >= 0 and nr-1 < ROWS and grid[nr-1][nc] == "1":
                        visited.add((nr-1,nc))
                        q.append((nr-1,nc))
                    if (nr,nc+1) not in visited and nc+1 >= 0 and nc+1 < COLS and grid[nr][nc+1] == "1":
                        visited.add((nr,nc+1))
                        q.append((nr,nc+1))
                    if (nr,nc-1) not in visited and nc-1 >= 0 and nc-1 < COLS and grid[nr][nc-1] == "1":
                        visited.add((nr,nc-1))
                        q.append((nr,nc-1))
                count += 1
                
        return count
                    




        