# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def searchBST(self, root, data):
        if not root:
            return []

        curr = root

        while curr:
            if curr.val == data:
                return curr
            elif curr.val > data:
                curr = curr.left
            else:
                curr = curr.right

        return None                
