class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        def dfs(i, combo, total):
            if total == target:
                result.append(combo.copy())
                return
            elif i == len(nums) or total > target:
                return

            combo.append(nums[i])
            dfs(i, combo, total+nums[i])

            combo.pop()
            dfs(i+1, combo, total)

        dfs(0, [], 0)
        return result 