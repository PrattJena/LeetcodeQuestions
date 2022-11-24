# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        x = 0
        arr = []
        def inorder(node):
            nonlocal x
            if node is None:
                return None
            
            inorder(node.left)
            x+=1
            # print(f"{x} - {node.val}")
            if x == k:
                arr.append(node.val)
            inorder(node.right)

        
        inorder(root)
        return arr[0]