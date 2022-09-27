"""
You are given an integer array nums. 
The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.
"""


"""
Example 1:
Input: nums = [1,2,3]
Output :4
Explaination: The 6 subarrays of nums are following:
[1], range = largest - smallest = 1 - 1 =0
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1, 2], range = 1 - 2 = 1
[2, 3], range = 2 - 3 = 1
[1, 3], range = 1 - 3 = 2
So the sum of all ranges is 4
"""

#  Time : O(n^2), Space: O(1)

def sub_array_ranegs(nums: list[int]) -> int:
    result = 0 
    n = len(nums)
    for i in range(n):
        Min, Max = nums[i], nums[i]
        for j in range(i, n, 1):
            Min = min(Min, nums[j])
            Max = max(Max, nums[j])
            result += Max - Min
    return abs(result)


class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        n = len(nums)
        
        # the answer will be sum{ Max(subarray) - Min(subarray) } over all possible subarray
        # which decomposes to sum{Max(subarray)} - sum{Min(subarray)} over all possible subarray
        # so totalsum = maxsum - minsum
        # we calculate minsum and maxsum in two different loops
        minsum = maxsum = 0
        
        # first calculate sum{ Min(subarray) } over all subarrays
        # sum{ Min(subarray) } = sum(f(i) * nums[i]) ; i=0..n-1
        # where f(i) is number of subarrays where nums[i] is the minimum value
        # f(i) = (i - index of the previous smaller value) * (index of the next smaller value - i) * nums[i]
        # we can claculate these indices in linear time using a monotonically increasing stack.
        stack = []
        for next_smaller in range(n + 1):
			# we pop from the stack in order to satisfy the monotonically increasing order property
			# if we reach the end of the iteration and there are elements present in the stack, we pop all of them
            while stack and (next_smaller == n or nums[stack[-1]] > nums[next_smaller]):
                i = stack.pop()
                prev_smaller = stack[-1] if stack else -1
                minsum += nums[i] * (next_smaller - i) * (i - prev_smaller)
            stack.append(next_smaller)
            
        # then calculate sum{ Max(subarray) } over all subarrays
        # sum{ Max(subarray) } = sum(f'(i) * nums[i]) ; i=0..n-1
        # where f'(i) is number of subarrays where nums[i] is the maximum value
        # f'(i) = (i - index of the previous larger value) - (index of the next larger value - i) * nums[i]
        # this time we use a monotonically decreasing stack.
        stack = []
        for next_larger in range(n + 1):
			# we pop from the stack in order to satisfy the monotonically decreasing order property
			# if we reach the end of the iteration and there are elements present in the stack, we pop all of them
            while stack and (next_larger == n or nums[stack[-1]] < nums[next_larger]):
                i = stack.pop()
                prev_larger = stack[-1] if stack else -1
                maxsum += nums[i] * (next_larger - i) * (i - prev_larger)
            stack.append(next_larger)
        
        return maxsum - minsum
