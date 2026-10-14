class Solution:
    # Function to reverse a string
    def reverseString(self, s):
        start, end = 0, len(s) - 1

        # Until the string is reversed
        while start < end:
            # Swap the characters at start and end
            s[start], s[end] = s[end], s[start]

            # Move the pointers towards the center
            start += 1
            end -= 1

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

# https://app.notion.com/p/Optimal-3f9f79cdb3f980eebc29e5cdec012a09