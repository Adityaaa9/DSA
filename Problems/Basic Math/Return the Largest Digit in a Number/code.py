class Solution:
    def largestDigit(self, n):
        n = abs(n)

        largest = 0

        while n > 0:
            digit = n % 10
            largest = max(largest, digit)
            n //= 10

        return largest

# n = 25
# Output: 5

# n = 99
# Output: 9

# https://app.notion.com/p/Return-the-Largest-Digit-in-a-Number-3e9f79cdb3f980eba41ec94508a67668