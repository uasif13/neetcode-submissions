class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while (lo <= hi):
            mid = lo + (hi-lo)//2
            if nums[mid] < nums[lo]:
                hi = mid
            elif nums[lo] < nums[hi]:
                return nums[lo]
            else:
                lo = mid + 1
        return nums[hi]


        '''
        3,4,5,6,1,2
        lo - 3
        hi - 4
        mid - 3
        '''

