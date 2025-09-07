#https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Time:O(1)
# 
# # Space:O(n)
class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [ n * (1 - n) // 2] + list(range(1, n))