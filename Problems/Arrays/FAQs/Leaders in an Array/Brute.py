class Solution:
    # Function to find leaders in an array.
    def leaders(self, nums):
        ans = []

        # Iterate through each element in nums
        for i in range(len(nums)):
            leader = True

            '''Check whether nums[i] is greater
            than all elements to its right'''
            for j in range(i + 1, len(nums)):
                if nums[j] >= nums[i]:
                    '''If any element to the right is greater 
                    or equal, nums[i] is not a leader'''
                    leader = False
                    break

            # If nums[i] is a leader, add it to the ans list
            if leader:
                ans.append(nums[i])

        # Return the leaders
        return ans


# Main method
nums = [1, 2, 5, 3, 1, 2]

# Create an instance of the Solution class
finder = Solution()

# Get leaders using class method
ans = finder.leaders(nums)

print("Leaders in the array are: ", end="")
for leader in ans:
    print(leader, end=" ")
print()


# https://app.notion.com/p/Brute-413f79cdb3f98021ad0dfaa176b0b31f