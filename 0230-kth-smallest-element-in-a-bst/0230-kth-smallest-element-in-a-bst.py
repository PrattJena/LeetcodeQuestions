# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val_arr = []
        def inorder(node):
            
            if node is None:
                return None
            
            inorder(node.left)
            val_arr.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        return (val_arr[k-1])