class Solution:
    # Function to find all
    # divisors of n
    def divisors(self, n):
        
        # To store the divisors
        ans = []
        
        # Iterate from 1 to n
        for i in range(1, n + 1):
            
            # If a divisor is found
            if n % i == 0:
                # Add it to the answer
                ans.append(i)
        
        # Return the result
        return ans

# Input number
n = 6

# Creating an instance of 
# Solution class
sol = Solution()

# Function call to find 
# all divisors of n
ans = sol.divisors(n)

print(f"The divisors of {n} are: ", end="")
for i in range(len(ans)):
    print(ans[i], end=" ")

# https://app.notion.com/p/Brute-3ecf79cdb3f980c99432cbe728b3d951