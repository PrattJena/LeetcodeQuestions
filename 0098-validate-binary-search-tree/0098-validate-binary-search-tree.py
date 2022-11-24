# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        val_arr = []
        
        def inorder(node):
            nonlocal val_arr
            if node is None:
                return None
            
            inorder(node.left)
            val_arr.append(node.val)
            inorder(node.right)
        
        inorder(root)
        print(val_arr)
        
        left = 0
        right = 1
        
        while right < len(val_arr):
            if val_arr[right] > val_arr[left]:
                left += 1
                right += 1
            else:
                return False
        return True
        
        # return val_arr == sorted(val_arr)