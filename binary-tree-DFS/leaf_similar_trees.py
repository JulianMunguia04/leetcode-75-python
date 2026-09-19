# 872 Leaf-Similar Trees, Binary Tree DFS, Easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :type root3: Optional[TreeNode]
        :rtype: bool
        """
        # Helper function to collect leaves from left to right using Depth-First Search (DFS)
        def get_leaves(root):
            leaves = []
            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    # If it's a leaf node, add its value to the list
                    if not node.left and not node.right:
                        leaves.append(node.val)
                    # Push right first so left is processed first (LIFO order)
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
            return leaves
        
        # Compare the leaf value sequences of both trees
        return get_leaves(root1) == get_leaves(root2)