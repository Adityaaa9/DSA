class Solution:
    def countOddDigit(self, n):
        n = abs(n)
        count = 0
        while n > 0:
            digit = n % 10
            if digit % 2 == 1:
                count += 1
            n //= 10
        return count
# Input number
n = 6678
 
# Creating an instance of 
# Solution class
sol = Solution()
 
# Function call to get count of odd digits in n
ans = sol.countOddDigit(n)
print("The count of odd digits in the given number is:", ans)

# https://app.notion.com/p/Count-number-of-odd-digits-in-a-number-3e9f79cdb3f980fc9eabec05dd84a68b