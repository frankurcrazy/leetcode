#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#

# @lc code=start
class Solution(object):
    def __init__(self):
        self._duplicates = {}

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n < 1: return False

        str_n = str(n)
        rv = sum([int(x) * int(x) for x in str_n])

        if rv == 1: return True

        elif rv in self._duplicates:
            return False
        else:
            self._duplicates.update({rv: True})
            return self.isHappy(rv)
        
# @lc code=end
