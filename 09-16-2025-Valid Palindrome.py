#https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
# Time:O(n)
# 
# # Space:O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_s = [letter for letter in s.lower() if letter.isalnum()]
        left = 0
        right = len(formatted_s) - 1

        while left < right:
            if formatted_s[left] != formatted_s[right]:
                return False
            left += 1
            right -= 1
        
        return True