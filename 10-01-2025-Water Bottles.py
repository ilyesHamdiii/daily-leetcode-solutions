#https://leetcode.com/problems/water-bottles/?envType=daily-question&envId=2025-10-01
# Time:O(1)
# 
# # Space:O(n)

class Solution:
    def numWaterBottles(self, b: int, n: int) -> int:
        return b + (b - 1) // (n - 1)