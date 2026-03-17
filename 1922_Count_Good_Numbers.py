# leetcode
class Solution:
    def myPow(self, x: float, n: int) -> float:
        r = 1
        mod = 10**9 + 7
        x %= mod
        while n > 0:
            if n % 2:
                r = (r * x) % mod
            x = (x*x) % mod
            n //= 2
        
        return r
    
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        even = (n+1)//2
        odd = n//2
        return (self.myPow(5,even) * self.myPow(4, odd)) % mod