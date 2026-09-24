# 236 Lowest Common Ancestor of a Binary Tree, DFS BT, Medium

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Base Case: if root is null or matches either target node, return root
        if not root or root == p or root == q:
            return root
        
        # Look for LCA in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both subtrees return a non-null node, the current root is the LCA
        if left and right:
            return root
            
        # Otherwise, return whichever subtree returned a non-null node
        return left if left else right