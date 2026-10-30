import random

class Solution:
    # Function to partition the array
    def partition(self, arr, low, high):
        # Choosing a random index between low and high
        randomIndex = low + random.randint(0, high - low)
        # Swap the random element with the first element
        arr[low], arr[randomIndex] = arr[randomIndex], arr[low]

        # Now choosing arr[low] as the pivot after the swap
        pivot = arr[low]
        # Starting index for left subarray
        i = low
        # Starting index for right subarray
        j = high

        while i < j:
            # Move i to the right until we find an element greater than the pivot
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            # Move j to the left until we find an element smaller than the pivot
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            # Swap elements at i and j if i is still less than j
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # Pivot placed in correct position
        arr[low], arr[j] = arr[j], arr[low]
        return j

    # Helper Function to perform the recursive quick sort
    def quickSortHelper(self, arr, low, high):
        # Base case: If the array has one or no elements, it's already sorted
        if low < high:
            # Get the partition index
            pIndex = self.partition(arr, low, high)
            # Sort the left subarray
            self.quickSortHelper(arr, low, pIndex - 1)
            # Sort the right subarray
            self.quickSortHelper(arr, pIndex + 1, high)

    # Function to perform quick sort on given array
    def quickSort(self, nums):
        # Get the size of array
        n = len(nums)

        # Perform quick sort
        self.quickSortHelper(nums, 0, n - 1)

        # Return sorted array
        return nums


if __name__ == "__main__":
    arr = [4, 6, 2, 5, 7, 9, 1, 3]
    n = len(arr)

    print("Before Sorting Array: ")
    for i in range(n):
        print(arr[i], end=" ")
    print()

    # Create an instance of Solution class
    solution = Solution()

    # Function call to sort the array using quick sort
    sortedArr = solution.quickSort(arr)

    print("After Sorting Array: ")
    for i in range(n):
        print(sortedArr[i], end=" ")
    print()

# https://app.notion.com/p/Quick-Sorting-409f79cdb3f980f2a9fafeaf2cff91ac