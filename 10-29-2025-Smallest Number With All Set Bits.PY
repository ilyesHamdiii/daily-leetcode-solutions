#https://leetcode.com/problems/smallest-number-with-all-set-bits/description/?envType=daily-question&envId=2025-10-29
# Time:O(n)
# Easy
# Space:O(n)


class Solution:
    def smallestNumber(self, n: int) -> int:
        while n & (n + 1):
            n |= n + 1
        return n