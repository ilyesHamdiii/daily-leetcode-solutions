#https://leetcode.com/problems/vowels-game-in-a-string/description/
# Time:O(n)
# 
# # Space:O(n)
#approach
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = 0
        for ch in s:
            if ch in 'aeiou':
                count += 1
        if count == 0:
            return False
        return True