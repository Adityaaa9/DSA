class Solution:
    # Function to find the GCD of two numbers
    def GCD(self, n1, n2):
        
        # Continue loop as long as both 
        # n1 and n2 are greater than zero
        while n1 > 0 and n2 > 0:
            
            # If n1 is greater than n2, perform
            # modulo operation - n1 % n2
            if n1 > n2:
                n1 = n1 % n2
            
            # Else perform modulo
            # operation - n2 % n1
            else:
                n2 = n2 % n1
        
        # If n1 is zero, GCD is stored in n2
        if n1 == 0:
            return n2
        
        # else GCD is stored in n1
        return n1
    
    # Function to find LCM of n1 and n2
    def LCM(self, n1, n2):
        # Function call to find gcd
        gcd = self.GCD(n1, n2)
        
        lcm = (n1 * n2) // gcd
        
        # Return the LCM
        return lcm

# Input numbers
n1, n2 = 3, 5

# Creating an instance of Solution class
sol = Solution()

# Function call to get LCM of n1 and n2
ans = sol.LCM(n1, n2)
print(f"The LCM of {n1} and {n2} is: {ans}")

# https://app.notion.com/p/Optimal-3ecf79cdb3f9801cb019dd28d05cbf06