# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBSTRecursive(self, node: Optional[TreeNode], left_end: int, right_end:int) -> bool:
        if not node: return True
        if node.val <= left_end or node.val >= right_end: return False
        return self.isValidBSTRecursive(node.left, left_end, node.val) and self.isValidBSTRecursive(node.right, node.val, right_end)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        return self.isValidBSTRecursive(root.left, float("-inf"), root.val) and self.isValidBSTRecursive(root.right, root.val, float("inf"))
        