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

def create_linkedlist(point_list):
    head = ListNode()
    return_value = head
    for i in range(len(point_list)):
        head.val = point_list[i]
        head.next = ListNode()

        head = head.next
    return return_value
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
linked_list = create_linkedlist([1,2,3,4,5])
linked_list2 = create_linkedlist([5])
print(Solution().reverseBetween(linked_list, 2, 4))
print(Solution().reverseBetween(linked_list2, 1, 1))


## Recruise solution

## COMPLEXITY

# For List with [1, 2, 3, 4, 5], supposed m == 2 and n == 4

# Step1:
# The part I need to reversed is node 2 to node 4, which has n - m + 1 = 3 nodes.
# Therefore, I would like to maintain a window with n - m + 1 nodes with the window's head whead and window's tail wtail, 
# then if whead is head, wtail would be the next n-m node from head.
# [123]45 => whead is 1 and wtail is 3

# Step2:
# And to get to the right reversed portion we want, we need to shift the window m-1 times
# 1[234]5 => whead is 2 and wtail is 4

# Step3: Isolate the nodes inside the window, reverse the window as Reverse Linked List

# Step4: combine the outside node with reversed node.
# To do so, I need to record the head outside the window ohead, and the tail outside the window otail

# ohead is 1, otail is 5
# 1-[432]-5
# Implementation detail: Since in step 4, you need to let ohead.next = reversed_headIf you create a dummy node, 
# you can save some lines for m == 1 cases, where ohead would be None and ohead.next would fail the program.



class Solution2():
    def reverseBetween(self, head, m, n):
        if m >= n:
            return head
        #Step 1#    
        ohead = dummy = ListNode(0)
        whead = wtail = head
        dummy.next = head
        for i in range(n-m):
            wtail = wtail.next
        #Step 2#  
        for i in range(m-1):
            ohead, whead, wtail = whead, whead.next, wtail.next
        #Step 3#  
        otail, wtail.next = wtail.next, None
        revhead, revtail = self.reverse(whead)
        #Step 4#  
        ohead.next, revtail.next = revhead, otail
        return dummy.next
            
    def reverse(self, head):
        pre, cur, tail = None, head, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre, tail

print(Solution2().reverseBetween(linked_list, 2, 4))
print(Solution2().reverseBetween(linked_list2, 1, 1))