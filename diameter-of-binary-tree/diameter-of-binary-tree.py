# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        arr = []
        def maxDepth(node):
            nonlocal arr
            if node is None:
                return 0
            
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            
            arr.append(left+right)
            return 1 + max(left, right)
        
        
        
        leftheight = maxDepth(root.left)
        rightheight = maxDepth(root.right)
        
        if len(arr) != 0:
            return max((leftheight + rightheight),  max(arr))
        
        else:
            return leftheight + rightheight
        