#https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/
# Time:O(n)
# 
# # Space:O(n)
class Solution:
    def maxFreqSum(self, s: str) -> int:
        con = 0
        vow = 0
        d_set = set(s)
        for i in d_set:
            if i in "aeiou":
                vow = max(vow, s.count(i))
            else:
                con = max(con, s.count(i))
        return con+vow 