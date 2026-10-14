class Solution:
    # Function to reverse a string
    def reverseString(self, s):
        n = len(s)
        
        # Create a temporary list to store reversed elements
        temp = [None] * n
        
        # Copy elements from original list to temp in reverse order
        for i in range(n):
            temp[i] = s[n - i - 1]
        
        # Copy back the reversed string to original list
        for i in range(n):
            s[i] = temp[i]
        
        return

# Main function
if __name__ == "__main__":
    str_list = ['h', 'e', 'l', 'l', 'o']

    # Creating an instance of Solution class
    sol = Solution()

    # Function call to reverse the string
    sol.reverseString(str_list)

    print("".join(str_list))
    print("The string has been reversed.")

# https://app.notion.com/p/Brute-3f9f79cdb3f98037bf60ef54af6a45e5