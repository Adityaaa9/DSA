import math

class Solution:
    # Function to find all 
    # divisors of n
    def divisors(self, n):
        
        # To store the divisors
        ans = []
        
        sqrtN = int(math.sqrt(n))
        
        # Iterate from 1 to sqrtN
        for i in range(1, sqrtN + 1):
            
            # If a divisor is found
            if n % i == 0:
                # Add it to the answer
                ans.append(i)
                
                # Add the counterpart divisor
                # if it's different from i
                if i != n // i:
                    ans.append(n // i)
        
        # Sorting the result 
        ans.sort()
        
        # Return the result
        return ans

# Creating an instance of 
# Solution class 
sol = Solution()

n = 6

# Function call to find 
# all divisors of n
ans = sol.divisors(n)

print("The divisors of", n, "are:", " ".join(map(str, ans)))

# https://app.notion.com/p/Optimal-3ecf79cdb3f980489d11ea4523ba03fa