class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(TreeNode):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if root.left:
                return self.isUnivalTree(root.left)
            if root.right:
                return self.isUnivalTree(root.right)
            return root.val
                
        return self.isUnivalTree(root.left) == self.isUnivalTree(root.right)

