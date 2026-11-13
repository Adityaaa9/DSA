# Create a class to replicate the structure
class Solution:
    # Function to print the element in rth row and cth column 
    def pascalTriangleI(self, r, c):
        return self.nCr(r - 1, c - 1)
    
    # Function to calculate nCr
    def nCr(self, n, r):
        # Choose the smaller value for lesser iterations
        if r > n - r:
            r = n - r
        
        # base case
        if r == 1:
            return n
        
        res = 1  # to store the result 
        
        # Calculate nCr using iterative method avoiding overflow 
        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1)
        
        return res  # return the result 

# row number
r = 5 
# col number
c = 3

# Create an instance of the Solution class
sol = Solution()

# Function call to print the element in rth row and cth column 
ans = sol.pascalTriangleI(r, c)

print("The element in the rth row and cth column in pascal's triangle is:", ans)

# https://app.notion.com/p/Pascal-s-Triangle-I-417f79cdb3f980199506f4208f77a684