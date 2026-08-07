class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        smallestPrefix = 0
        sum = nums[0]
        currSum = 0
        for n in nums:
            currSum += n
            sum = max(sum,currSum-smallestPrefix)
            smallestPrefix = min(smallestPrefix, currSum)
        return sum
