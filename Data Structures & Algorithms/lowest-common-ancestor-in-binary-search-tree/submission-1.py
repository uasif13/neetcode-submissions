# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def contains(self, root: TreeNode, node: TreeNode) -> bool:
        if not root: return False
        return root.val == node.val or self.contains(root.left, node) or self.contains(root.right, node)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = collections.deque()
        queue.append(root)
        lowest = None
        while (len(queue) > 0):
            curr = queue.popleft()
            if self.contains(curr, p) and self.contains(curr,q):
                lowest = curr
                queue.append(curr.left)
                queue.append(curr.right)
        return lowest

        