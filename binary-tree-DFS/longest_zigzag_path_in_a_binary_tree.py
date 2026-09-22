# 1372 Longest ZigZag Path in a Binary Tree, DFS BT, Medium

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :type root: TreeNode
        :rtype: int
        """
        self.max_length = 0
        
        def dfs(node, go_left, current_length):
            if not node:
                return
            
            # Update the global maximum length found so far
            self.max_length = max(self.max_length, current_length)
            
            if go_left:
                # If we need to go left to continue the current zigzag:
                # 1. Move left and increase the step count by 1 (direction switches to right)
                dfs(node.left, False, current_length + 1)
                # 2. We can also reset/start a fresh zigzag path going right
                dfs(node.right, True, 1)
            else:
                # If we need to go right to continue the current zigzag:
                # 1. Move right and increase the step count by 1 (direction switches to left)
                dfs(node.right, True, current_length + 1)
                # 2. We can also reset/start a fresh zigzag path going left
                dfs(node.left, False, 1)
                
        # Start DFS from the root node in both directions with an initial length of 0
        dfs(root, True, 0)
        dfs(root, False, 0)
        
        return self.max_length