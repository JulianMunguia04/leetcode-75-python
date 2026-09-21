# 437 Path Sum III, DFS BF, Medium

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        # Dictionary to store the frequency of prefix sums encountered
        # Base case: a prefix sum of 0 is seen exactly once (before tracking any nodes)
        prefix_sums = {0: 1}
        
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Update the running prefix sum
            current_sum += node.val
            
            # If (current_sum - targetSum) exists in our map, it means we found
            # a valid sub-path that sums up exactly to targetSum
            count = prefix_sums.get(current_sum - targetSum, 0)
            
            # Add the current prefix sum to the map to make it available for child nodes
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
            # Recursively count valid paths in the left and right subtrees
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            # Backtrack: remove the current prefix sum before moving back up the tree
            prefix_sums[current_sum] -= 1
            
            return count

        return dfs(root, 0)