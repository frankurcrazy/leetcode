#
# @lc app=leetcode id=415 lang=python
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (43.43%)
# Likes:    531
# Dislikes: 179
# Total Accepted:    119.7K
# Total Submissions: 266.3K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#

# @lc code=start
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        num1_rev = num1[::-1]
        num2_rev = num2[::-1]
        result = ""

        carry = 0
        for idx in range(max(len(num1_rev), len(num2_rev))):
            s = 0

            if idx < len(num1_rev):
                s += ord(num1_rev[idx]) - ord('0')

            if idx < len(num2_rev):
                s += ord(num2_rev[idx]) - ord('0')

            s, carry = (s+carry)%10, (s+carry)/10 

        
            result = str(s) + result

        if carry:
            result = str(carry) + result
            
        return result
        
# @lc code=end
