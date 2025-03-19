# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # if neither
        if not p and not q:
            return True
        # uneven count
        elif (not p and q) or (p and not q):
            return False
        # val mismatch
        elif p.val != q.val:
            return False
        # recursion
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 
        