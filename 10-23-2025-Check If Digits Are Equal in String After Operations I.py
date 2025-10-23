#https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/?envType=daily-question&envId=2025-10-23
# Time:O(n)
# Easy
# Space:O(n)
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(c) for c in s]
        n = len(digits)
        while n > 2:
            for i in range(n - 1):
                digits[i] = (digits[i] + digits[i + 1]) % 10
            n -= 1
        return digits[0] == digits[1]