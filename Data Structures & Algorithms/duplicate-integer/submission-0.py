class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for n in nums:
            if n in table: return True
            else: table[n] = 1
        return False