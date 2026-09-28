class Solution:
    def isArmstrong(self, n):
        original = n
        n = abs(n)
        digits = len(str(n))
        total = 0
        while n > 0:
            digit = n % 10
            total += digit ** digits
            n //= 10
        return total == original

# n = 153
# Output: true

# n = 12
# Output: false

# https://app.notion.com/p/Check-if-the-Number-is-Armstrong-3e9f79cdb3f9809abcc0c54dd5374ccf