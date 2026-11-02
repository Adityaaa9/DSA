from typing import List

class Solution:
    # Function to move zeroes to the end
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)

        """Create a temporary array 
        to store non-zero elements"""
        temp = [0] * n
        count = 0

        # Copy non-zero elements to temp
        for i in range(n):
            if nums[i] != 0:
                temp[count] = nums[i]
                count += 1

        # Copy non-zero elements back to nums
        for i in range(count):
            nums[i] = temp[i]

        # Fill the rest with zeroes
        for i in range(count, n):
            nums[i] = 0

if __name__ == "__main__":
    nums = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

    # Create an instance of Solution class
    sol = Solution()
    sol.moveZeroes(nums)

    print("Array after moving zeroes:", nums)


#  https://app.notion.com/p/Brute-40cf79cdb3f980aab2c2f4681534020f