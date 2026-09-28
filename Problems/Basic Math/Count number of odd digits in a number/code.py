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
# n = 5
# Output 1
# Expected: 1
# https://app.notion.com/p/Count-number-of-odd-digits-in-a-number-3e9f79cdb3f980fc9eabec05dd84a68b