class Solution:
    # Function to return the rth row of Pascal's triangle
    def pascalTriangleII(self, r):
        ans = [0] * r  # to store the answer
        
        # Set the first element of the row as 1
        ans[0] = 1 
        
        # Compute each element in the rth row
        for i in range(1, r):
            ans[i] = (ans[i-1] * (r - i)) // i
        
        return ans  # return the result

# row number
r = 5  

# Create an instance of the Solution class
sol = Solution()  

# Function call to return the rth row of Pascal's triangle
ans = sol.pascalTriangleII(r)

# Output
print(f"Row {r}: ", end="")
print(*ans)

# https://app.notion.com/p/Pascal-s-Triangle-II-418f79cdb3f9803f851acbd926f6f819