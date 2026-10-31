class Solution:
    # Method to sort the array using recursive insertion sort
    def insertionSort(self, nums):
        # Start the recursive sorting
        self.insertionSortHelper(nums, len(nums))
        return nums

    # Helper function for recursive insertion sort
    def insertionSortHelper(self, nums, n):
        # Base case: If the size is 1, it's already sorted
        if n <= 1:
            return

        # Recursively sort the first n-1 elements
        self.insertionSortHelper(nums, n - 1)

        # Insert the nth element into its correct position in the sorted part
        last = nums[n - 1]
        j = n - 2
        
        # Step 1: Shift elements to the right to make room for the last element
        while j >= 0 and nums[j] > last:
            nums[j + 1] = nums[j]
            j -= 1
        
        # Step 2: Place the last element at its correct position
        nums[j + 1] = last


# Driver code
if __name__ == "__main__":
    sol = Solution()
    nums = [5, 2, 9, 1, 5, 6]  # Example input array

    # Output the sorted result
    sortedArray = sol.insertionSort(nums)
    print(sortedArray)


# https://app.notion.com/p/Brute-40af79cdb3f98019969bcdc8d2407ef8