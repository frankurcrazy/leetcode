#coding: utf-8
#
# @lc app=leetcode id=299 lang=python
#
# [299] Bulls and Cows
#
# https://leetcode.com/problems/bulls-and-cows/description/
#
# algorithms
# Medium (39.06%)
# Total Accepted:    93.6K
# Total Submissions: 239.3K
# Testcase Example:  '"1807"\n"7810"'
#
# You are playing the following Bulls and Cows game with your friend: You write
# down a number and ask your friend to guess what the number is. Each time your
# friend makes a guess, you provide a hint that indicates how many digits in
# said guess match your secret number exactly in both digit and position
# (called "bulls") and how many digits match the secret number but locate in
# the wrong position (called "cows"). Your friend will use successive guesses
# and hints to eventually derive the secret number.
# 
# Write a function to return a hint according to the secret number and friend's
# guess, use A to indicate the bulls and B to indicate the cows. 
# 
# Please note that both secret number and friend's guess may contain duplicate
# digits.
# 
# Example 1:
# 
# 
# Input: secret = "1807", guess = "7810"
# 
# Output: "1A3B"
# 
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
# 
# Example 2:
# 
# 
# Input: secret = "1123", guess = "0111"
# 
# Output: "1A1B"
# 
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a
# cow.
# 
# Note: You may assume that the secret number and your friend's guess only
# contain digits, and their lengths are always equal.
#
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        bulls = cows = 0

        # First round: find bulls
        for idx, val in enumerate(secret):
            if guess[idx] == val:
                bulls = bulls + 1
                guess = guess[:idx] + '-' + guess[idx+1:]
                secret = secret[:idx] + '-' + secret[idx+1:]

        # Second round: find cows
        for idx, val in enumerate(secret):
            if val == '-': continue
            try:
                pos = guess.index(val)
                #print(val, pos, guess)
                cows = cows + 1 
                guess = guess[:pos] + '-' + guess[pos+1:]

            except Exception:
                continue

        return "{bulls}A{cows}B".format(bulls=bulls, cows=cows)

#sol = Solution()
#print(sol.getHint("1123", "0111"))
