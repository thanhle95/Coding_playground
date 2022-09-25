
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
# return the area of the largest rectangle in the histogram.

# input: heights = [2,1,5,6,2,3]
#           -
#        - |-|
#       |\||\|
#       |\||\|    -
#  -    |\||\| - | |
# | | - |\||\|| || |
# | || ||\||\|| || |
#----------------------------------------
#
# Output is the block with |\| = 10

###
# SOLUTION EXPLAINATION

    #   def largestRectangleArea(self, heights):
    #       heights.append(0)
    #       stack = [-1]
    #       ans = 0

# We add a zero at the end because we want to always ensure a condition in which the current considered height is less than the height's stored in the stack.
# If this doesn't make sense, skip it then come back, more on this later
# 
# We instantiate the stack with -1 as a reference to the 0 that we added to height. The zero serves a couple functions:
#       It always adds the first height to the stack so it's not empty
#       In the case where the given heights are all in ascending order, it creates an ending point that breaks this trend, allowing us to calculate the areas

    # for i in range(len(heights)):
    #    while heights[i] < heights[stack[-1]]:

# I think it's more intuitive to think about this in terms of the inverse condition.
# The inverse condition is, if we run into height[i]'s >= what we currently see in the stack, just keep stacking!
# This creates a condition where the height's stored in the stack are always in ascending order as you approach the top of the stack

    # h = heights[stack.pop()]
    # w = i - 1 - stack[-1]
    # ans = max(ans, h * w)

# the while condition is true when we see a height that's smaller than height stored at the top of the stack.
# the current h is guaranteed to the be the limiting height (remember the stack is ascending so everything to its right was >= h)
    #  h = height[stack.pop()] 

# key thing to remember here is stack is always ascending, soi-1 represents the right boundary of the considered rectangle and stack[-1] represents the left boundary. 
# So subtracting the them gets you the width!
    #  w = i - 1 - stack[-1]
    
# only record the largest area you see. 
    # ans = max(ans, h * w) 

###



class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans


print(Solution().largestRectangleArea([2,1,5,6,2,3]))