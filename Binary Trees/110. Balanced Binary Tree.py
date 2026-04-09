# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check_height(self, root):
        if not root:
            return 0

        left_root = self.check_height(root.left)
        if left_root == -1:
            return -1
        right_root = self.check_height(root.right)
        if right_root == -1:
            return -1
        
        if abs(left_root - right_root) > 1:
            return -1

        return max(left_root, right_root) + 1

    def isBalanced(self, root):
        if root == None:
            return True
        return self.check_height(root) != -1
