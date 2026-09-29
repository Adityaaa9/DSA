class Solution:
    # Function to count all digits in n
    def countDigit(self, n):
        # Edge case
        if n == 0:
            return 1

        # Set counter to 0
        cnt = 0

        # Iterate until n is greater than zero
        while n > 0:
            # Increment count of digits
            cnt = cnt + 1
            n = n // 10

        return cnt

# Input number
n = 6678

# Creating an instance of Solution class
sol = Solution()

# Function call to get count of digits in n
ans = sol.countDigit(n)
print(f"The count of digits in the given number is: {ans}")

# https://app.notion.com/p/Count-all-Digits-of-a-Number-3e9f79cdb3f98014a448dc62e98aeeab