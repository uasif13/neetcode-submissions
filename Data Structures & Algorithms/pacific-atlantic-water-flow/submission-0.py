class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        ROWS = len(heights)
        COLS = len(heights[0])
        print(ROWS, COLS)
        def dfs(r,c,visited,height,side):
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] > height or (r,c) in visited:
                return False
            if ((r == 0 or c == 0) and side == "p"): return True
            if ((r == ROWS-1 or c == COLS-1) and side == "a"): return True
            visited.add((r,c))
            # print(r,c,visited,height,side)
            return dfs(r+1,c,visited,heights[r][c],side) or dfs(r-1,c,visited,heights[r][c],side) or dfs(r,c+1,visited,heights[r][c],side) or dfs(r,c-1,visited,heights[r][c],side)

        for i in range(ROWS):
            for j in range(COLS):
                # print(i, j, dfs(i,j, set(), heights[i][j], "p"), dfs(i,j,set(),heights[i][j],"a"))
                if dfs(i,j, set(), heights[i][j], "p") and dfs(i,j,set(),heights[i][j],"a"): result.append([i,j])
        return result
