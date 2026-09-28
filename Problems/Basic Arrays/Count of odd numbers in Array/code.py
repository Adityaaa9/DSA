class Solution:
    def countOdd(self, arr):
        count = 0
        for num in arr:
            if num % 2 != 0:
                count += 1
        return count

# arr = [1, 2, 3, 4, 5]
# Output: 3

# arr = [1, 2, 1, 1, 5, 1]
# Output: 5

# 