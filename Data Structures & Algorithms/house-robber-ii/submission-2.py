class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 3: return max(nums)
        dpFirst = [0]*(len(nums)-1)
        dpLast = [0]*(len(nums)-1)
        dpFirst[0] = nums[0]
        dpFirst[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            dpFirst[i] = max(dpFirst[i-1], nums[i]+dpFirst[i-2])
        dpLast[0] = nums[1]
        dpLast[1] = max(nums[1], nums[2])
        for i in range(2, len(nums)-1):
            dpLast[i] = max(dpLast[i-1], nums[i+1]+dpLast[i-2])
        return max(dpFirst[-1], dpLast[-1])