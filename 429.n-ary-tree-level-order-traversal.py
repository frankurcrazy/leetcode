#
# @lc app=leetcode id=429 lang=python
#
# [429] N-ary Tree Level Order Traversal
#
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Easy (58.99%)
# Total Accepted:    28.6K
# Total Submissions: 48.5K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given an n-ary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# For example, given a 3-ary tree:
# 
# 
# 
# 
# 
# 
# 
# We should return its level order traversal:
# 
# 
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
# 
# 
# 
# 
# Note:
# 
# 
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.
# 
# 
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        
        node_q = deque()
        result = list() 
        level = 0

        node = root

        while node is not None:
            for child in node.children:
                node_q.appendleft((level+1, child))

            if len(result) < level + 1:
                result.append([node.val])
            else:
                result[level].append(node.val)

            try:
                level, node = node_q.pop()
            except Exception:
                break

        return result
