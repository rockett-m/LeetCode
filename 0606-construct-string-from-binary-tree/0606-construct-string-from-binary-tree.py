# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def solve(node):
            if not node: return ''
            
            out = f"{node.val}"
            
            if node.left or node.right:
                out += f"({solve(node.left)})"
                
            if node.right:
                out += f"({solve(node.right)})"

            print(out)
            return out

        print(solve(root))
        return solve(root)
        