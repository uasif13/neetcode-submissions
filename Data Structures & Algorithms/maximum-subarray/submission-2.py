class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        smallestPrefix = [0]
        sum = float("-inf")
        currSum = 0
        for n in nums:
            currSum += n
            sum = max(sum,currSum-smallestPrefix[0])
            heapq.heappush(smallestPrefix, currSum)
        return sum
