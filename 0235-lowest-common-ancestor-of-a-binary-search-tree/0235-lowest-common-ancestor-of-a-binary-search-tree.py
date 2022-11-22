# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_node_vals = []
        def search_p(node, p):
            if node is None:
                return False
            elif p.val == node.val:
                p_node_vals.append(node)
                return True
            elif (p.val < node.val):
                p_node_vals.append(node)
                search_p(node.left, p)
            else:
                p_node_vals.append(node)
                search_p(node.right, p)
        
        q_node_vals = []
        def search_q(node, q):
            if node is None:
                return False
            elif q.val == node.val:
                q_node_vals.append(node)
                return True
            elif (q.val < node.val):
                q_node_vals.append(node)
                search_q(node.left, q)
            else:
                q_node_vals.append(node)
                search_q(node.right, q)
        
        search_p(root, p)
        search_q(root, q)
        common_nodes = [nodes for nodes in q_node_vals if nodes in p_node_vals]
        return (common_nodes[-1])