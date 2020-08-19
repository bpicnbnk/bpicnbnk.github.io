class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        if n == 0:
            return 1
        if n % 2 == 1:
            product = x * self.myPow(x, n-1)
            return product
        return self.myPow(x*x, n/2)


s = Solution()
x = 2.0
x = 0.00001

n = 10
n = -2
n = 2147483647
result = s.myPow(x, n)
print(result)
