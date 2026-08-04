class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = {}
        maxConsec = 0
        for i, n in enumerate(nums): 
            table[n] = i
        visited = set()
        for n in nums:
            if n in visited: continue
            top = n
            while top in table:
                visited.add(top)
                top += 1
            bottom = n
            while bottom in table:
                visited.add(bottom)
                bottom -= 1
            maxConsec = max(maxConsec, top - bottom-1)
        return maxConsec
            

        
        