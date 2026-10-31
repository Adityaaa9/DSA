class Solution:
    # Method to sort the array using recursive bubble sort
    def bubbleSort(self, nums):
        # Start the recursive sorting
        self.bubbleSortHelper(nums, len(nums))
        return nums

    # Helper function for recursive bubble sort
    def bubbleSortHelper(self, nums, n):
        # Base case: If the array size is 1 or less, it's already sorted
        if n == 1:
            return

        # Perform one pass of bubble sort
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                # Swap if the current element is greater than the next
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        # Recursively call to sort the first n-1 elements
        self.bubbleSortHelper(nums, n - 1)


# Driver code
if __name__ == "__main__":
    sol = Solution()
    nums = [5, 2, 9, 1, 5, 6]  # Example input array

    # Output the sorted result
    sortedArray = sol.bubbleSort(nums)
    print("Sorted array:", sortedArray)


# https://app.notion.com/p/Recursive-Bubble-Sort-40af79cdb3f980fab018c4b2cd7e848e