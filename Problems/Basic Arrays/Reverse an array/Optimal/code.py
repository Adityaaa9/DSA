class Solution:
    # Function to reverse array using two pointers
    def reverse(self, arr, n):
        p1 = 0
        p2 = n - 1
        # Swap elements pointed by p1 and 
        # p2 until they meet in the middle
        while p1 < p2:
            tmp = arr[p1]
            arr[p1] = arr[p2]
            arr[p2] = tmp
            p1 += 1
            p2 -= 1
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

# https://app.notion.com/p/Optimal-3edf79cdb3f98017accfc6777355287d