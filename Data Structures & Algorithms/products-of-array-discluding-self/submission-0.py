class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*(len(nums))
        multiply = 1
        for i in range(1, len(nums)):
            result[i] = nums[i-1]*result[i-1]
        for j in range(len(nums)-2, -1, -1):
            multiply *=  nums[j+1]
            result[j] *= multiply
        return result