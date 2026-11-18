class Solution:
    # Method to set entire rows and columns to 0 if a 0 is found in the matrix
    def setZeroes(self, matrix):
        m = len(matrix)  # Number of rows
        n = len(matrix[0])  # Number of columns
        
        rows = [False] * m  # To mark rows to be set to 0
        cols = [False] * n  # To mark columns to be set to 0
        
        # Step 1: Identify rows and columns to be set to 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        
        # Step 2: Set the corresponding rows and columns to 0
        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0


# Driver code
if __name__ == "__main__":
    sol = Solution()
    
    # Example matrix: 
    # 1 2 3
    # 4 0 6
    # 7 8 9
    matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    
    # Output the matrix before and after setting zeroes
    sol.setZeroes(matrix)
    
    for row in matrix:
        print(row)


# https://app.notion.com/p/Brute-41cf79cdb3f980b088b6e400c54627d6