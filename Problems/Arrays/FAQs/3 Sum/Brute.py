from typing import List

class Solution:
    #Function to find triplets having sum equals to target
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Set to store unique triplets
        triplet_set = set()

        n = len(nums)

        # Check all possible triplets
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        # Found a triplet that sums up to target
                        temp = [nums[i], nums[j], nums[k]]
                        
                        """ Sort the triplet to ensure 
                        uniqueness when storing in set"""
                        temp.sort()
                        triplet_set.add(tuple(temp))
        
        # Convert set to list of lists (unique triplets)
        ans = [list(triplet) for triplet in triplet_set]

        #Return the ans
        return ans

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]

    # Create an instance of Solution class
    sol = Solution()


    ans = sol.threeSum(nums)

    # Print the result
    for triplet in ans:
        print(f"[{', '.join(map(str, triplet))}]")


# https://app.notion.com/p/Brute-41ef79cdb3f98065b5b9c48df914d7c0