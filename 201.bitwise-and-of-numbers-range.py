#
# @lc app=leetcode id=201 lang=python
#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (35.72%)
# Total Accepted:    79.9K
# Total Submissions: 223.5K
# Testcase Example:  '5\n7'
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
# of all numbers in this range, inclusive.
# 
# Example 1:
# 
# 
# Input: [5,7]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: [0,1]
# Output: 0
#
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        mask = 2**32-1

        while m & mask != n & mask:
            mask = mask << 1

        return m & mask
        
