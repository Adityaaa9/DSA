class Solution:
    def checkPrime(self, num):
        if num <= 1:
            return False  # 0 and 1 are not prime numbers
        return self.prime(num, 2)  # Call the helper function to check for primality
    
    def prime(self, num, x):
       # Base case: x > sqrt(num), so the number is prime
        if x > num ** 0.5:
            return True  
        if num % x == 0:
        # Found a divisor, so the number is not prime
            return False  
         # Recursive call with the next divisor
        return self.prime(num, x + 1)  

# Main method for testing the checkPrime function
if __name__ == "__main__":
    solution = Solution()
    num = 41  
    result = solution.checkPrime(num)  
    print(result)


# https://app.notion.com/p/Check-if-a-Number-is-Prime-or-Not-407f79cdb3f980f197a6f6d4ab471874