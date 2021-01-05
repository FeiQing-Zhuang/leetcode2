from typing import List
# class Solution:
#     def largeGroupPositions(self,s:str) -> List[List[int]]:
#         ret = list()
#         n,num = len(s),1
#         for i in range(n):
#             if i == n -1 or s[i] != s[i+1]:
#                 if num >= 3:
#                     ret.append([i-num+1,i])
#                 num = 1
#             else:
#                 num += 1
#         return ret

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res=[]
        i=0
        length=len(s)
        while i<length:
            j=i+1
            while j<length and s[j]==s[i]:
                j+=1
            #此时的j指向了一个不同的字母
            if j-1-i>=2:
                res.append([i,j-1])
            i=j
        return res
