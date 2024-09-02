class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        q = deque()
        m,n = len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                # if board[i][j] == 'O' and (m-1>i>0) and (n-1>j>0):
                if board[i][j] == 'O' and (i==0 or j==0 or i==m-1 or j==n-1):
                    q.append((i,j))  

        while q:
            x,y = q.popleft()
            board[x][y] = '1'
            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                r,c = x+i,y+j
                if 0<=r<m and 0<=c<n and board[r][c] =='O':
                    q.append((r,c))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == '1':
                    board[i][j] = 'O'
                   
                    
        