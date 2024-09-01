class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        ROOM, GATE, WALL = 2**31-1,0,-1
        q = deque()

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == GATE:
                    q.append((r,c,0))
        
        while q:
            x,y,d = q.popleft()
            print(x,y,d)

            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                r,c = x+i,y+j
                print(r,c)
                if 0<=r<m and 0<=c<n and rooms[r][c] == ROOM:
                    q.append((r,c,d+1))
                    rooms[r][c] = d+1
        

        