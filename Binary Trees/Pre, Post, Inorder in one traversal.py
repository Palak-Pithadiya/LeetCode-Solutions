# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree_traversal(self, root):
        if not root:
            return [], [], []

        in_order = []
        pre_order = []
        post_order = []

        stack = [[root, 1]]

        while stack:
            pair = stack[-1]
            node, state = pair[0], pair[1]

            if state == 1:
                pre_order.append(node.val)
                pair[1] += 1 
                if node.left:
                    stack.append([node.left, 1])

            elif state == 2:
                in_order.append(node.val)
                pair[1] += 1 
                if node.right:
                    stack.append([node.right, 1])

            else:
                post_order.append(node.val)
                stack.pop()

        return pre_order, in_order, post_order
