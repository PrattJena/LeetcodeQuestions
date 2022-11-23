# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        ans = []
        queue = deque([root])
        added = False
        while queue:
            ans.append(queue[0].val)
            for i in range(len(queue)):
                node = queue.popleft()
                
                # print(f"{queue} - {added}")
                
                if node.right:
                    queue.append(node.right)
                
                if node.left:
                    queue.append(node.left)
                    

        
        return (ans)