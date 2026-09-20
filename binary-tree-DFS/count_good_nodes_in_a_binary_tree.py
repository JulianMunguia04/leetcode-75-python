# 1448 Count Good Nodes in Binary Tree, DFS BT, Medium

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_val):
            if not node:
                return 0
            
            # Check if current node is a "good node"
            good = 1 if node.val >= max_val else 0
            
            # Update the maximum value seen so far on this path
            max_val = max(max_val, node.val)
            
            # Traverse left and right subtrees
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)
            
            return good
            
        # Start DFS with the root value as the initial maximum path value
        return dfs(root, root.val) if root else 0