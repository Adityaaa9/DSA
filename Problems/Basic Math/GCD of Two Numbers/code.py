class Solution:
    def GCD(self, n1, n2):
        while n2 != 0:
            n1, n2 = n2, n1 % n2

        return abs(n1)

# Input numbers
n1 = 4
n2 = 6
 
# Creating an instance of 
# Solution class
sol = Solution()
 
# Function call to find the
# gcd of two numbers
ans = sol.GCD(n1, n2)
 
print(f"GCD of {n1} and {n2} is: {ans}")

# https://app.notion.com/p/GCD-of-Two-Numbers-3eaf79cdb3f980078425c8d5ed2d6784