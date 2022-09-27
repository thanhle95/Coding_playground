

# Kindle Diẻct Publishing, AMZ's e-book self-publishing platform, is working on a new feature to help authors track the use of text strings in different ways.
# A substring is a group of contiguous characters in a string. For instance, all sub string of abc are [a, b, c, ab, bc, abc]

# Given a binary representation of a number, determine the total number of substring present that match the following condition:

# 1. The 0s and 1s are grouped consecutively (e.g, 01, 10, 0011, 1100, 000111, etc.).
# 2. The number of 0s in the substring is equal to the number of 1s in the substring.


#### INPUT
#   s: a string representation of a binary integer

#### OUTPUT
#   the number of substring of s that satisfy the two conditions.


# Examples:
# Input: s = 001101
# Output: 4

# Explaination:
# The 4 substirng matching the two conditions include [0011, 01, 10, 01]. 
# Note that 01 appears twice, from indices 1-2 and 4-5.
# There are other substring, e.g 001 and 011 that match the first condition but not the second.

### CONSTRAINTS
# 5 <= |s| <= 5*10^5
# each s[i] is either '0' or '1'


#SOLUTION 1

# 1. 0011
# In this string, consecutive count of binary characters are [2, 2]. We can form a total of 2 substrings.

# 2. 00011
# In this string, consecutive count of binary characters are [3, 2]. Still, we can only form 2 substrings.

# 3. 000111
# Here, consecutive count of binary characters are as - [3,3]. Now, we can form 3 substrings.

# 4. 00011100
# Consecutive count of binary characters are - [3,3,2]. We can form 3 substrings with the first 2 groups of zeros and ones. 
# Then we can form 2 substrings with the latter 2 groups. So, a total of 5 substrings.

# 5. 00011100111
# Consecutive count - [3,3,2,3]. Substrings formed - 3 + 2 + 2 = 7

# We can observe from the above examples that our final count will only depend on the consecutive counts of binary characters. 
# With each two groups of consecutive characters, the number of substrings that can be formed will be minimum of count among the two groups


def countBinarySubstrings(s: str) -> int:
	ans, prev, cur = 0, 0, 1
	for i in range(1, len(s)):
		if s[i] != s[i - 1]:
			ans += min(prev, cur)
			prev = cur
			cur = 1
		else:
			cur += 1
	ans += min(prev, cur)
	return ans

# Time complexity: 0(N), where N is the length of given string.
# Space complexity: 0(1), since only constant space is being used.


print(countBinarySubstrings("00011100111"))