#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (35.73%)
# Total Accepted:    247.1K
# Total Submissions: 691.6K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false # 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        org = head
        rev = None
        tmp = None

        while org:
            tmp = rev
            rev = ListNode(org.val)  
            rev.next = tmp
            org = org.next

        org = head
        while org:
            if org.val != rev.val: return False
            org = org.next
            rev = rev.next

        return True
