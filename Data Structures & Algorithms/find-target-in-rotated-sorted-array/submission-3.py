class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
        while (lo <= hi):
            mid = lo + (hi-lo)//2
            #print(lo, mid, hi)
            if nums[mid] == target: return mid
            elif nums[lo] < nums[hi] and target < nums[mid]:
                hi = mid - 1
            elif nums[lo] < nums[hi]:
                lo = mid + 1
            elif nums[mid] >= nums[lo] and target > nums[mid]:
                lo = mid + 1
            elif nums[mid] >= nums[lo] and target <= nums[hi]:
                lo = mid + 1
            elif nums[mid] >= nums[lo] and target >= nums[lo]:
                hi = mid - 1
            elif nums[mid] < nums[lo] and target < nums[mid]:
                hi = mid - 1
            elif nums[mid] < nums[lo] and target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
                

        