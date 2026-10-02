class Solution:
    # Function to reverse array using an auxiliary array
    def reverse(self, arr, n):
        ans = [0] * n
        
        # Fill new array with elements of 
        # original array in reverse order
        for i in range(n - 1, -1, -1):
            ans[n - i - 1] = arr[i]
        
        # Copy the elements back to the original array
        for i in range(n):
            arr[i] = ans[i]
        
        # Return
        return
 
# Function to print array
def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()
 
if __name__ == "__main__":
    n = 5
    arr = [5, 4, 3, 2, 1]
    
    # Creating instance of Solution class
    solution = Solution()
    print("Original array: ", end="")
    printArray(arr, n)
    
    # Function call to reverse the array 
    solution.reverse(arr, n) 
    print("Reversed array: ", end="")
    printArray(arr, n)

# https://app.notion.com/p/Brute-3edf79cdb3f980c89895cc09c5b15b3e