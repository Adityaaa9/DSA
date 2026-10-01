class Solution:
    # Function to find LCM of n1 and n2
    def LCM(self, n1, n2):
        # Variable to store lcm
        lcm = 0
        
        # Variable to store max of n1 & n2
        n = max(n1, n2)
        i = 1
        
        while True:
            # Variable to store multiple
            mul = n * i
            
            # Checking if multiple is common
            # common for both n1 and n2
            if mul % n1 == 0 and mul % n2 == 0:
                lcm = mul
                break
            i += 1
        
        # Return the stored LCM
        return lcm

# Input values
n1 = 4
n2 = 12

# Creating an instance of Solution class
sol = Solution()

# Function call to get LCM of n1 and n2
ans = sol.LCM(n1, n2)
print("The LCM of", n1, "and", n2, "is:", ans)

# https://app.notion.com/p/Brute-3ecf79cdb3f980fb81e4df39855b70f3