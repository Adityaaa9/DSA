class Solution:
    def factorial(self, n):
        result = 1

        for i in range(1, n + 1):
            result *= i

        return result

# Input number
n = 4
 
# Creating an instance of Solution class
sol = Solution()
 
# Function call to find the factorial of n
ans = sol.factorial(n)
 
print("The factorial of given number is:", ans)

# https://app.notion.com/p/Factorial-of-a-given-number-3e9f79cdb3f98038a1dcc4414e3ba43e