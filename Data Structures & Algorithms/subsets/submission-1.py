import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for n in nums:
            temp = copy.deepcopy(result)
            for subset in temp:
                subset += [n]
            result += temp
        return result
        