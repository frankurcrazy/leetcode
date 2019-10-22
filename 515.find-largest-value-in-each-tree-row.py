# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = {}
        rlist = []

        def traverse(root, row):
            if root is None:
                return

            result.setdefault(row, [])
            result[row].append(root.val)

            traverse(root.left, row+1)
            traverse(root.right, row+1)

        traverse(root, 0)
        for k, v in result.items():
            rlist.append(max(v))

        return rlist


