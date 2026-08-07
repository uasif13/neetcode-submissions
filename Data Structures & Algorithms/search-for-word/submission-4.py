class Solution:
    def check(self, board: List[List[str]], word: str, i: int, j: int, visited:set) -> bool:
        if word == "": return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in visited or board[i][j] != word[0]: return False
        visited.add((i,j))

        bottom = self.check(board,word[1:], i+1, j, visited)
        top = self.check(board,word[1:], i-1, j, visited)
        right = self.check(board,word[1:], i, j+1, visited)
        left = self.check(board,word[1:], i, j-1, visited)
        visited.remove((i,j))
        return bottom or top or right or left 

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.check(board, word, i, j, set()): return True
        return False
        