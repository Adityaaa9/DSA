class Solution:

    # Method to compute the sum of digits of given number
    def addDigits(self, num):
        # Base case: if the number is a single digit, return it
        if num < 10:
            return num

        # Recursive case: sum the digits and continue
        sum_digits = self.sumDigits(num)

        return self.addDigits(sum_digits)
    
    # Helper function to add the sum of digits recursively
    def sumDigits(self, num):
        # Base case: If the number is 0, return 0
        if num == 0:
            return 0

        # Recursive case
        return self.sumDigits(num // 10) + (num % 10)


# Driver code
if __name__ == "__main__":
    solution = Solution()

    # Example number
    num = 529

    # Call the addDigits method and print the result
    result = solution.addDigits(num)
    print("Sum of digits:", result)

# https://app.notion.com/p/Sum-of-Digits-in-a-Given-Number-407f79cdb3f980b0bf2ce2e4eda4a3ab