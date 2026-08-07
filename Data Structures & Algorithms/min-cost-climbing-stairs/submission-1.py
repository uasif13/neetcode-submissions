class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = 0
        second = 0
        for i in range(2,len(cost)+1):
            temp = min(second+cost[i-1], first+cost[i-2])
            first = second
            second = temp
        return second