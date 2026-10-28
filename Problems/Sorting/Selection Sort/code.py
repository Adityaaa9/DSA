class Solution:
    def selectionSort(self, nums):
        # Loop through unsorted part 
        # of the array (0 to n-2)
        for i in range(len(nums) - 1):
            ''' Assume current 
            element is minimum '''
            min_index = i

            '''Find actual minimum in 
            unsorted part (i+1 to n-1) '''
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j

            ''' Swap only if minIndex 
            changed (optimization) '''
            if min_index != i:
                nums[i], nums[min_index] = nums[min_index], nums[i]

        return nums

# Main function to test the selection sort
if __name__ == "__main__":
    solution = Solution()
    nums = [64, 25, 12, 22, 11]
    sorted_nums = solution.selectionSort(nums)
    print("Sorted array:", sorted_nums)


# https://app.notion.com/p/Selection-Sort-407f79cdb3f980ebbbf3da4f6e31abb0