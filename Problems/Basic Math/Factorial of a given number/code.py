class Solution:
    def factorial(self, n):
        result = 1

        for i in range(1, n + 1):
            result *= i

        return result

# n = 2
# Output: 2

# n = 0
# Output: 1

# https://app.notion.com/p/Factorial-of-a-given-number-3e9f79cdb3f98038a1dcc4414e3ba43e