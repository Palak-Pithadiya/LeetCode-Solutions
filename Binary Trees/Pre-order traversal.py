class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
  def pre_order_tree_traversal(self, root):
    if not root:
      return []

    res = []
    stack = [root]

    while stack:
      node = stack.pop()
      res.append(node.data)

      # Push right first so left is on top
      if node.right:
        stack.append(node.right)
      if node.left:
        stack.append(node.left)

    return res

# 1. Manually build the tree [1, 3, 4, 5, 2, 7, 6]
# Structure:
#      1
#     / \
#    3   4
#   / \ / \
#  5  2 7  6

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(4)
root.left.left = TreeNode(5)
root.left.right = TreeNode(2)
root.right.left = TreeNode(7)
root.right.right = TreeNode(6)

obj = Solution()
# root =  [1, 3, 4, 5, 2, 7, 6 ]
print(obj.pre_order_tree_traversal(root))

