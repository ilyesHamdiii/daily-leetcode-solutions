#https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
# Time:O(M+N)
# Easy
# # Space:O(n)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alpha = {}
        for i in range(len(magazine)):
            alpha[magazine[i]] = alpha.get(magazine[i], 0) + 1
         
        for i in range(len(ransomNote)):
            if ransomNote[i] not in alpha or alpha[ransomNote[i]] == 0:
                return False
            alpha[ransomNote[i]] -= 1
            print(alpha)
        return True