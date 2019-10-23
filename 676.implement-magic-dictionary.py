#
# @lc app=leetcode id=676 lang=python
#
# [676] Implement Magic Dictionary
#
# https://leetcode.com/problems/implement-magic-dictionary/description/
#
# algorithms
# Medium (51.34%)
# Likes:    420
# Dislikes: 106
# Total Accepted:    29.7K
# Total Submissions: 56.6K
# Testcase Example:  '["MagicDictionary", "buildDict", "search", "search", "search", "search"]\n' +
  '[[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]'
#
# 
# Implement a magic directory with buildDict, and search methods.
# 
# 
# 
# For the method buildDict, you'll be given a list of non-repetitive words to
# build a dictionary.
# 
# 
# 
# For the method search, you'll be given a word, and judge whether if you
# modify exactly one character into another character in this word, the
# modified word is in the dictionary you just built.
# 
# 
# Example 1:
# 
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
# 
# 
# 
# Note:
# 
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now. You could think
# about highly efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class
# MagicDictionary, as static/class variables are persisted across multiple test
# cases. Please see here for more details.
# 
# 
#

# @lc code=start
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = []
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        self.dictionary.extend(dict)
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """

        length_matched_words = filter(lambda x: len(x) == len(word), self.dictionary)

        for w in length_matched_words:
            diff_alpha = 0

            for i in range(len(w)):
                if word[i] != w[i]:
                    diff_alpha += 1

            if diff_alpha == 1: return True

        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
# @lc code=end
