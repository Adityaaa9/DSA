class Solution:
    """ Function to get the sum of highest
    and lowest frequency in array """
    def sumHighestAndLowestFrequency(self, nums):
        
        # Variable to store the size of array
        n = len(nums)
        
        """ Variable to store maximum 
        and minimum frequency """
        max_freq = 0
        min_freq = n

        # Visited array
        visited = [False] * n
        
        # First loop
        for i in range(n):
            # Skip second loop if already visited
            if visited[i]:
                continue
            
            """ Variable to store frequency
            of current element """
            freq = 0
            
            # Second loop
            for j in range(i, n):
                if nums[i] == nums[j]:
                    freq += 1
                    visited[j] = True
            
            """ Update maximum and 
            minimum frequencies """
            max_freq = max(max_freq, freq)
            min_freq = min(min_freq, freq)
            
        # Return the required sum
        return max_freq + min_freq

# Example usage
nums = [1, 2, 2, 3, 3, 3]

""" Creating an instance of 
Solution class """
sol = Solution()

""" Function call to get the sum of highest
and lowest frequency in array """
ans = sol.sumHighestAndLowestFrequency(nums)

print("The sum of highest and lowest frequency in the array is:", ans)

# https://app.notion.com/p/Brute-3f8f79cdb3f9800fbeddffae51fc7e64