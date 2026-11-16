class Solution:
    # Function to generate a single row of Pascal's Triangle
    def generateRow(self, row):
        ans = 1
        ansRow = []
        
        # Inserting the 1st element
        ansRow.append(1)

        # Calculate the rest of the elements
        for col in range(1, row):
            ans = ans * (row - col)
            ans = ans // col
            ansRow.append(ans)
        
        return ansRow  # Return the computed row

    # Function to generate Pascal's Triangle up to n rows
    def pascalTriangleIII(self, n):
        pascalTriangle = []

        # Compute the entire Pascal's Triangle
        for row in range(1, n + 1):
            pascalTriangle.append(self.generateRow(row))
        
        #return the pascalTriangle
        return pascalTriangle


if __name__ == "__main__":
    n = 5
    sol = Solution()

    # Generate Pascal's Triangle with n rows
    pascalTriangle = sol.pascalTriangleIII(n)

    # Output the Pascal's Triangle
    for row in pascalTriangle:
        for element in row:
            print(element, end=" ")
        print()

# https://app.notion.com/p/Pascal-s-Triangle-III-41af79cdb3f9804bba89dec7b037e4d5