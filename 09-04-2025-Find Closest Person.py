#https://leetcode.com/problems/find-closest-person/description/
# Time:O(1)
# 
# # Space:O(n)
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x-z)==abs(y-z):
            return 0
        elif abs(x-z)<abs(y-z):
            return 1
        else:
            return 2