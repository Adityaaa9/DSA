class Solution:
     # Bubble Sort Function
    def bubbleSort(self, nums):
        n = len(nums)
        # Traverse through the array
        for i in range(n - 1, -1, -1):
            # Track if swaps are made
            isSwapped = False
            for j in range(i):
                # Swap if next element is smaller
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    isSwapped = True
            ''' Break out of loop
             if no swaps done'''
            if not isSwapped:
                break
        return nums

# Main function
if __name__ == "__main__":
    # Create an instance of solution class
    solution = Solution()

    nums = [7, 4, 1, 5, 3]

    print("Array Before Using Bubble Sort:", nums)

    # Function call for Bubble Sort
    sorted_nums = solution.bubbleSort(nums)

    print("Array After Using Bubble Sort:", sorted_nums)


# https://app.notion.com/p/Bubble-sort-407f79cdb3f9807b8406e05800027813