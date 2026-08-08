class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        memo = {}
        def wordBreakRecursive(s, i):
            if s == "": return True
            if i >= len(s): return False
            update = False
            if s in memo:
                return memo[s] 
            if s[0:i+1] in wordDictSet: 
                update = update or wordBreakRecursive(s[i+1:],0)
            update = update or wordBreakRecursive(s,i+1)
            memo[s] = update
            return update
        return wordBreakRecursive(s,0)