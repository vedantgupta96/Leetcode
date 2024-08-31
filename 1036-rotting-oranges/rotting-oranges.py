class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        m = len(grid)
        n = len(grid[0])
        ROTTEN = 2
        FRESH = 1
        EMPTY = 0
        numFresh = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    q.append((i,j))
                if grid[i][j] == FRESH:
                    numFresh+=1
            
        if numFresh == 0:
            return 0
        
        while q:
            size = len(q)
            minute += 1

            for _ in range(size):
                i,j = q.popleft()

                for r,c in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
                    if 0<=r<m and 0<=c<n and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        numFresh -= 1
                        q.append((r,c))
        if numFresh == 0:
            return minute-1
        return -1


        