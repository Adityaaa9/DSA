class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            # Check s -> t mapping
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t
            
            # Check t -> s mapping
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s
        
        return True

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = "egg"
    t1 = "add"
    result1 = solution.isIsomorphic(s1, t1)
    print(f"Input: s = \"{s1}\", t = \"{t1}\"")
    print(f"Output: {result1}")  # Expected: True
    
    # Test case 2
    s2 = "foo"
    t2 = "bar"
    result2 = solution.isIsomorphic(s2, t2)
    print(f"\nInput: s = \"{s2}\", t = \"{t2}\"")
    print(f"Output: {result2}")  # Expected: False
    
    # Test case 3
    s3 = "paper"
    t3 = "title"
    result3 = solution.isIsomorphic(s3, t3)
    print(f"\nInput: s = \"{s3}\", t = \"{t3}\"")
    print(f"Output: {result3}")  # Expected: True

# https://app.notion.com/p/Isomorphic-Strings-3fbf79cdb3f980179c77d3fd838d8c7e