class Solution:
    
    # Function to reverse the given string
    def reverseString(self, s):
        
        # Recursive function to reverse the 
        # string character by character 
        def reverse(s, left, right):
            # Base case
            if left >= right:
                return 
            
            # Swap characters at left and right positions
            s[left], s[right] = s[right], s[left]
            
            # Recursive call with updated indices
            reverse(s, left + 1, right - 1)
        
        reverse(s, 0, len(s) - 1)
        return s

# Main function to test the solution
if __name__ == "__main__":
    solution = Solution()
    s = ['h', 'e', 'l', 'l', 'o']
    
    # Function call to reverse the given string
    reversed_s = solution.reverseString(s)
    print(reversed_s)


# https://app.notion.com/p/Reverse-a-String-I-405f79cdb3f9808893d2ef59a5d0ca88