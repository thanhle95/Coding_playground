# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:
# 1 -> 2 -> 3 -> 4 -> 5
#      -----------
# 1 -> 4 -> 3 -> 2 -> 5

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n



#COMPLEXITY

# Very similar to problem 25. We keep three pointers as with any other reverse linked lists problems: pre, curr, next. 
# We can split all algorithm into 3 steps:

# Do m-1 steps to reach the first point of range we need to reverse.
# Reverse range [n - m], using 3 pointers approach.
# Finally we need to fix connections for the start and for the end of reversed list, using saved pointer to pre element.
# Complexity

# Time complexity is O(n), because we need to traverse elements upto n-th. Space complexity is O(1).






# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next
        
        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next




print(Solution().reverseBetween([1,2,3,4,5], 2, 4))
print(Solution().reverseBetween([5], 1, 1))
