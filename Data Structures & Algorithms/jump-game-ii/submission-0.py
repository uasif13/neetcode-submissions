class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [1000]*len(nums)
        dp[0] = 0
        for i, n in enumerate(nums):
            for j in range(i+1,i+n+1):
                if j < len(nums): dp[j] = min(dp[j],dp[i] + 1)
        return dp[-1]