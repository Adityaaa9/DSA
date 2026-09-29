class Solution:
    # Function to find the GCD of two numbers
    def GCD(self, n1, n2):
        
        # Variable to store the gcd
        gcd = 1
        
        # Iterate from 1 to min(n1, n2)
        for i in range(min(n1, n2), 0, -1):
            
            # Check if i is a common divisor 
            # of both n1 and n2
            if n1 % i == 0 and n2 % i == 0:
                
                # Update gcd
                gcd = i
                # Break to skip unnecessary iterations
                break
        
        # Return stored GCD
        return gcd

# Input numbers
n1, n2 = 4, 6

# Creating an instance of Solution class
sol = Solution()

# Function call to find the gcd of two numbers
ans = sol.GCD(n1, n2)

print(f"GCD of {n1} and {n2} is: {ans}")

# https://app.notion.com/p/Better-3eaf79cdb3f9802ba1e7cafdee281e5e