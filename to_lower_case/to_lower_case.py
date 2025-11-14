# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

# Example 1:

# Input: s = "Hello"
# Output: "hello"
# Example 2:

# Input: s = "here"
# Output: "here"
# Example 3:

# Input: s = "LOVELY"
# Output: "lovely"
 

# Constraints:

# 1 <= s.length <= 100
# s consists of printable ASCII characters.











class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []
        for c in s:
            if 'A' <= c <= 'Z':  
                res.append(chr(ord(c) + 32))
            else:
                res.append(c)
        return ''.join(res)
    
# test
sol = Solution()
test = "Hello"
print(sol.toLowerCase(test))