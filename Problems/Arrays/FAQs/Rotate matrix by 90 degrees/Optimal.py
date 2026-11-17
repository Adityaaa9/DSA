from typing import List

class Solution:
    # Rotate the given matrix by 90 degrees clockwise.
    def rotateMatrix(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Transpose the matrix
        for i in range(n):
            for j in range(i):
                # Swap elements across the diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row of the matrix
        for i in range(n):
            for j in range(n // 2):
                # Swap elements symmetrically
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Create an instance of the Solution class
    sol = Solution()
    
    # Rotate the matrix
    sol.rotate(arr)
    
    # Output the rotated matrix
    print("Rotated Image:")
    for row in arr:
        print(" ".join(map(str, row)))

# https://app.notion.com/p/Optimal-41bf79cdb3f9800ebbfbe6dc27731116