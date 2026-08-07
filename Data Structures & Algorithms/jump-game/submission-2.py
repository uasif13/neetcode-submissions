class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0]*len(nums)
        dp[0] = 1
        for i, n in enumerate(nums):
            for j in range(i+1,i+n+1):
                if j < len(nums): dp[j] = dp[i] 
        #     print(i,n,dp)
        # print(dp)       
        return True if dp[-1] == 1 else False