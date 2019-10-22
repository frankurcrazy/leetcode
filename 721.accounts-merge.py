#
# @lc app=leetcode id=721 lang=python
#
# [721] Accounts Merge
#
# https://leetcode.com/problems/accounts-merge/description/
#
# algorithms
# Medium (39.67%)
# Likes:    818
# Dislikes: 217
# Total Accepted:    47.7K
# Total Submissions: 109.9K
# Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
#
# Given a list accounts, each element accounts[i] is a list of strings, where
# the first element accounts[i][0] is a name, and the rest of the elements are
# emails representing emails of the account.
# 
# Now, we would like to merge these accounts.  Two accounts definitely belong
# to the same person if there is some email that is common to both accounts.
# Note that even if two accounts have the same name, they may belong to
# different people as people could have the same name.  A person can have any
# number of accounts initially, but all of their accounts definitely have the
# same name.
# 
# After merging the accounts, return the accounts in the following format: the
# first element of each account is the name, and the rest of the elements are
# emails in sorted order.  The accounts themselves can be returned in any
# order.
# 
# Example 1:
# 
# Input: 
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
# "johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
# "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com',
# 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary",
# "mary@mail.com"]]
# Explanation: 
# The first and third John's are the same person as they have the common email
# "johnsmith@mail.com".
# The second John and Mary are different people as none of their email
# addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary',
# 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
# would still be accepted.
# 
# 
# 
# Note:
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].
# 
#

# @lc code=start
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        result = {}
        group_name = {}

        def merge_group(group1, group2):
            mingroup = min(group1, group2)
            for k, v in result.items():
                if v == group1 or v == group2:
                    result[k] = mingroup

        for account in accounts:
            name, emails = account[0], account[1:]
            group = None 

            # find group id
            for email in emails:
                if email in result:
                    group = result[email]
                    break

            if group is not None:
                for email in emails:
                    if email in result and result[email] != group:
                        # Need to merge two group
                        merge_group(group, result[email])
                        group = min(group, result[email])

                    result[email] = group

            else:
                group_id = len(group_name.keys())
                group_name.update({group_id: name})
                for email in emails:
                    result.update({
                        email: group_id
                    })

        res_list = []
        for v, k in group_name.items():
            res_sublist = [k]
            emails = []

            for email, group_id in result.items():
                if v == group_id:
                    emails.append(email)

            if len(emails) == 0: continue
            res_sublist.extend(sorted(emails))


            res_list.append(res_sublist)

        return res_list 
        
# @lc code=end

if __name__ == "__main__":
    sol = Solution()

    print(sol.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
