class Solution:
    def reverseNumber(self, n):
        sign = -1 if n < 0 else 1
        n = abs(n)

        reverse = 0

        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n //= 10

        return sign * reverse

# n = 25
# Output: 52
# https://app.notion.com/p/Reverse-a-number-3e9f79cdb3f980108519c1549d78efa1