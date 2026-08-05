# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        maxHeap = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node: continue
            heapq.heappush_max(maxHeap, node.val)
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
            stack.append(node.left)
            stack.append(node.right)
        return maxHeap[0]
            