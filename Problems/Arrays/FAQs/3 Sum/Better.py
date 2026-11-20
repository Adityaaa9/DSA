from typing import List

class Solution:
    # Function to find triplets having sum equals to 0
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Set to store unique triplets
        triplet_set = set()

        n = len(nums)

        # Check all possible triplets
        for i in range(n):
            # Set to store elements seen so far in the loop
            hashset = set()

            for j in range(i + 1, n):
                # Calculate the 3rd element needed to reach target
                third =  - (nums[i] + nums[j])

                """ Find if third element exists in
                 hashset (complements seen so far)"""
                if third in hashset:
                    # Found a triplet that sums up to target
                    temp = [nums[i], nums[j], third]

                    """ Sort the triplet to ensure
                    uniqueness when storing in set"""
                    temp.sort()
                    triplet_set.add(tuple(temp))

                """ Insert the current element 
                into hashset for future checks"""
                hashset.add(nums[j])

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


# https://app.notion.com/p/Better-41ef79cdb3f9800da9f9f89e4f6dc1cc