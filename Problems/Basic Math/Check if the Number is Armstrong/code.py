import math

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

# Main function
if __name__ == "__main__":
    n = 153
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to find whether the
    # given number is Armstrong or not
    ans = sol.isArmstrong(n)
    
    if ans:
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is not an Armstrong number.")
        
# https://app.notion.com/p/Check-if-the-Number-is-Armstrong-3e9f79cdb3f9809abcc0c54dd5374ccf