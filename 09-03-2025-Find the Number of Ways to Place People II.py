#https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/?envType=daily-question&envId=2025-09-03
# Time:O(n + k log n)
# 
# # Space:O(n^2)
# Python:O(1)
class Solution:
    def numberOfPairs(self, P: List[List[int]]) -> int:
        P.sort(key=lambda p:(-p[0], p[1]))
        ans, n=0, len(P)
        for i in range(n-1):
            y, yi=1<<31, P[i][1]
            for j in range(i+1, n):
                yj=P[j][1]
                if y>yj>=yi:
                    ans+=1
                    y=yj
                    if yi==yj: break
        return ans
        