import copy
class Solution:
    def check(self, board: List[List[str]], word: str, i: int, j: int, visited:set) -> bool:
        #print(word, i, j, visited)
        if word == "": return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in visited or board[i][j] != word[0]: return False
        top_visited = copy.deepcopy(visited)
        right_visited = copy.deepcopy(visited)
        left_visited = copy.deepcopy(visited)
        visited.add((i,j))
        bottom = self.check(board,word[1:], i+1, j, visited)
        top_visited.add((i,j))
        top = self.check(board,word[1:], i-1, j, top_visited)
        right_visited.add((i,j))
        right = self.check(board,word[1:], i, j+1, right_visited)
        left_visited.add((i,j))
        left = self.check(board,word[1:], i, j-1, left_visited)
        return bottom or top or right or left 

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.check(board, word, i, j, set()): return True
        return False
        