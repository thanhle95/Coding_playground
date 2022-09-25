# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:
# 1 -> 2 -> 3 -> 4 -> 5
# ------    ------
# 2 -> 1 -> 4 -> 3 -> 5


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:
# 1 -> 2 -> 3 -> 4 ->5
# -----------
# 3 -> 2 -> 1 -> 4 -> 5

# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]



# Solution

# This problem is a standard follow up to
# LC 206 Reverse Linked List

# A lot of the solutions implemented the reversing logic from scratch
# I am going to pretend that I just finish writing the standard reverse method, and reuse the method on the follow up.

# LC 206 Reverse Linked List

class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        
        prev, cur, nxt = None, head, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev    

# Follow up: Please reverse the list into K Group

class Solution():
    def reverseKGroup(self, head, k):
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev
    
    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)



# This is quite classical linked list problem and it is quite nasty in my opinion. 
# It can be a bit problematic to imagine all this in your head, do it on paper. 
# The idea is to add dummy variable, then calculate number of nodes. 
# We need this, because we do not need to reverse last group. 
# Then we use idea similar to problem 0206 Reverse Linked List: 
# but here we need to reverse k elements, and then reconnect first and last nodes in each group and update cnt.

# Complexity

# Time complexity is O(n), space complexity is O(1).

from AMZ_Reverse_Linked_List_2 import ListNode

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        cur, nxt, pre = dummy, dummy, dummy
        cnt = 0
        while cur.next:
            cnt += 1
            cur = cur.next
            
        while cnt >= k:
            cur = new = pre.next
            nxt = cur.next
            for _ in range(k-1):
                tmp = nxt.next
                nxt.next = cur
                cur = nxt
                nxt = tmp
            
            pre.next = cur
            new.next = nxt
            pre = new
            cnt -= k
            
        return dummy.next