# class Solution:
#     def fib(self,n:int) -> int:
#         if n < 2:
#             return n
#         p,q,r = 0,0,1
#         for i in range(2,n+1):
#             p,q = q,r
#             r = p + q
#
#         return r

class Solution:
    def fib(self, n: int) -> int:
        sqrt5 = 5**0.5
        fibN = ((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n
        return round(fibN / sqrt5)

