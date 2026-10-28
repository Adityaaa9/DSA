class Solution:
    def fib(self, n):
        # Base cases: F(0) = 0, F(1) = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return self.fib(n - 1) + self.fib(n - 2)

if __name__ == "__main__":
    solution = Solution()
    n = 5  # Example input
    print(f"Fibonacci number at position {n} is {solution.fibonacci(n)}")


# https://app.notion.com/p/Fibonacci-Number-407f79cdb3f98047a5e3d3487bb848f7