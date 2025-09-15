#https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/?envType=daily-question&envId=2025-09-15
# Time:O(n*2)
# 
# # Space:O(n)
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res=0
        p=text.split()
        for i in p:
            for x in brokenLetters:
                if x in i:
                    res+=1
                    break
        return len(p)-res


        