class Solution:
    # approach 1
    def fib_approach1(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        fib = [-1 for _ in range(n + 1)]
        fib[0] = 0
        fib[1] = 1
        for i in range(2, n+1):
            if fib[i] == -1:
                fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]

    # approach 2
    def fib_approach2(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib_approach2(n - 1) + self.fib_approach2(n - 2)
