# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?



from collections import Counter

# The current window is s[i:j] and the result window is s[I:J]. 
# In need[c] I store how many times I need character c (can be negative) and missing tells how many characters are still missing. 
# In the loop, first add the new character to the window. 
# Then, if nothing is missing, remove as much as possible from the window start and then update the result.


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, missing = Counter(t), len(t)
        windows_start = result_start = result_end = 0
        for windows_end, c in enumerate(s, 1):
            print(windows_start, windows_end, result_start, result_end)
            print(c, missing, need)
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while need[s[windows_start]] < 0: 
                    need[s[windows_start]] += 1; windows_start += 1
                if not result_end or windows_end - windows_start <= result_end - result_start: 
                    result_start, result_end = windows_start, windows_end
                need[s[windows_start]] += 1; windows_start += 1; missing += 1       # SPEEEEEEEED UP!

        return s[result_start : result_end]


print(Solution().minWindow("ADOBECODEBANC", "ABC"))