# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = []
        def preorder(node, num):
            if node is None:
                return ""
            # print(f"num - {num}")
            if node.left is None and node.right is None:
                prev_num = num
                prev_num+= f"{node.val}"
                arr.append(int(prev_num))
                return num
                
            num = f"{num}{node.val}"
            preorder(node.left, num)
            preorder(node.right, num)

            
        
        preorder(root, "")
        
        return sum(arr)
        # print(arr)
    
        