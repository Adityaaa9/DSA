from typing import List

class Solution:
    #Function to rotate the given matrix by 90 degrees clockwise
    
    def rotateMatrix(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Initialize new matrix to store rotated values
        rotated = [[0] * n for _ in range(n)]
        
        # Perform rotation logic
        for i in range(n):
            for j in range(n):
                rotated[j][n - i - 1] = matrix[i][j]
        
        # Copy rotated elements back to original matrix
        for i in range(n):
            matrix[i] = rotated[i]

if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Create an instance of the Solution class
    sol = Solution()
    
    # Rotate the matrix
    sol.rotate(arr)
    
    # Print the rotated matrix
    print("Rotated Image:")
    for row in arr:
        print(" ".join(map(str, row)))

# https://app.notion.com/p/Brute-41bf79cdb3f98021a810d4797b1abd4f