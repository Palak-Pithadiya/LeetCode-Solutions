# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxi = 0

        def check_diameter(node):
            if not node:
                return 0
    
            lh = check_diameter(node.left)
            rh = check_diameter(node.right)
            self.maxi = max(self.maxi, lh + rh)
    
            return 1 + max(lh, rh)

        check_diameter(root)
        return self.maxi 
