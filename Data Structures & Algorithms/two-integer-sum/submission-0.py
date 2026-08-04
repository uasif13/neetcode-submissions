class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, n in enumerate(nums):
            if target - n in table: return sorted([i, table[target-n]])
            table[n] = i