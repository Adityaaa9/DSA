class Solution:
    def isPalindrome(self, n):
        if n < 0:
            return False

        original = n
        reverse = 0

        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n //= 10

        return original == reverse

# Input number
n = 12321
 
# Creating an instance of Solution class
sol = Solution()
 
# Function call to check if n is a palindrome
ans = sol.isPalindrome(n)
 
if ans:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")

# https://app.notion.com/p/Palindrome-Number-3e9f79cdb3f98085a182d1a118e5eb4f