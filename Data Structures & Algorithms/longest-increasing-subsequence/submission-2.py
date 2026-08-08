class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[] for _ in range(len(nums))]
        dp[0] = [nums[0]]
        maximum = 1
        for i in range(1, len(nums)):
            for j in range(0,i):
                if dp[j][-1] < nums[i] and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
            if dp[i] == []: dp[i] = [nums[i]]
            maximum = max(len(dp[i]),maximum)
        return maximum
        