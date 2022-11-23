# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        ans = []
        queue = deque([root])
        
        while queue:
            temp_arr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                
                temp_arr.append(node.val)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            ans.append(max(temp_arr))
        
        return (ans)
        