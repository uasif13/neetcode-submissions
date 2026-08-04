class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]: continue
            lo = i + 1
            hi = len(nums)-1
            while (lo < hi):
                s = n + nums[lo] + nums[hi]
                if s < 0:
                    lo += 1
                elif s > 0:
                    hi -= 1
                else:
                    result.append([n, nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while (lo < hi and nums[lo] == nums[lo-1]):
                        lo += 1
        return result
        