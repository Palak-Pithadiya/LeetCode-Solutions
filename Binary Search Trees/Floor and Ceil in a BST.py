# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def floorCeilOfBST(self, root, key):
        #your code goes here
        floor = -1
        ceil = -1

        # for ceil
        curr = root
        while curr:
            if curr.data == key:
                ceil = curr.data
                break
            elif curr.data < key:
                curr = curr.right
            else:
                ceil = curr.data
                curr = curr.left

        # for floor
        curr = root
        while curr:
            if curr.data == key:
                floor = curr.data
                break
            elif curr.data > key:
                curr = curr.left
            else:
                floor = curr.data
                curr = curr.right

        return [floor, ceil]


`
