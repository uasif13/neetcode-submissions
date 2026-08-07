class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combo = []
        def dfs(i):
            if sum(combo) == target:
                result.append(combo.copy())
                return
            elif i == len(nums) or sum(combo) > target:
                return

            combo.append(nums[i])
            dfs(i)

            combo.pop()
            dfs(i+1)

        dfs(0)
        return result 