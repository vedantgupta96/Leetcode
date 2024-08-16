class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False for i in range(len(board[0]))] for _ in range(len(board))]
        print(visited)
        def searchWord(r,c,i):
            if i == len(word):
                return True
            if 0>r or r>=len(board) or 0>c or c>=len(board[0]) or board[r][c] != word[i] or visited[r][c]:
                return False
            visited[r][c] = True
            if searchWord(r+1,c,i+1) or searchWord(r-1,c,i+1) or searchWord(r,c+1,i+1) or searchWord(r,c-1,i+1):
                return True
            visited[r][c] = False
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and searchWord(r,c,0):
                    return True
        return False
        
        
            
            


