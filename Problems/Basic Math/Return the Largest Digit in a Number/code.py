class Solution:
    def largestDigit(self, n):
        n = abs(n)

        largest = 0

        while n > 0:
            digit = n % 10
            largest = max(largest, digit)
            n //= 10

        return largest

if __name__ == "__main__":
    n = 348
 
    # Creating an instance of 
    # Solution class
    sol = Solution()
 
    # Function call to find the largest digit in n
    ans = sol.largestDigit(n)
 
    print("The largest digit in the number is:", ans)

# https://app.notion.com/p/Return-the-Largest-Digit-in-a-Number-3e9f79cdb3f980eba41ec94508a67668