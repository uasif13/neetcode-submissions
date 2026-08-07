class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(i, combo, closedLeft):
            if closedLeft < 0 or i > n:
                return
            if i == n and closedLeft == 0:
                res.append(combo)
                return

            dfs(i+1, combo + "(", closedLeft+1)
            dfs(i,combo + ")",closedLeft-1)
            

        dfs(0,"", 0)
        return res