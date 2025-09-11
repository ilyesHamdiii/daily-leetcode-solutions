#https://leetcode.com/problems/sort-vowels-in-a-string/submissions/1767602275/?envType=daily-question&envId=2025-09-11
# Time:O(n*log n)
# 
# # Space:O(n)
#approach
class Solution:
    def sortVowels(self, s: str) -> str:
        voy=[]
        for i in range(len(s)):
            if s[i].lower() in ["e","y","a","o","u","i"]:
                voy.append(s[i])
        voy.sort()
        k=0
        res=""
        for i in range(len(s)):
            if s[i].lower() in ["e","y","a","o","u","i"]:
                res+=voy[k]
                k+=1
            else:
                res+=s[i]
        return res


        