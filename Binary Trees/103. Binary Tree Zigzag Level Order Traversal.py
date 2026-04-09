# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res = []
        
        if not root:
            return res
        left_to_right = True
        queue = deque([root])

        while queue:
            len_size = len(queue)
            curr_level = deque()

            for _ in range(len_size):
                node = queue.popleft()

                if left_to_right:
                    curr_level.append(node.val)
                else:
                    curr_level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(list(curr_level))
            left_to_right = not left_to_right

        return res
