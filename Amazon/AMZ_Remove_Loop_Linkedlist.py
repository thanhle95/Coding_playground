# Given a linked list. If the linked list contains a loop, return True and remove the loop.
# A linked list contains a cycle if it consists of a node that can be reached again by continuously following the next pointer.

# Examples:
# Input:
# 1 -> 2 -> 3 -> 4 -> 5 -> 3

# Output: 1 -> 2 -> 3 -> 4 -> 5
# Explanation: The linked list consists of a loop, where the last node connects to the second node. Hence, remove the loop



# Approach: Using HashSet

# The simplest approach to solve this problem is to check whether a node in the linked list has been visited before. To perform this operation, a hashmap can be used. If a node has already occurred before, simply set the current pointer to NULL.

# Algorithm

# Initialise a hashmap.
# Traverse the linked list till the head pointer isn’t NULL:
# If the current node is already present in the hashmap, it ensures that the linked list contains a loop. Hence, set the node to NULL.
# Else, continue traversing and continue inserting the node into the hashset.
# If no node satisfy the above conditions, then the linked list does not contain any cycle.

# Time Complexity:O(N) where N is the number of nodes of the linked list.
# Space Complexity:O(N), as HashSet is used

def removeLoop(head):
        mp = set()
        prev = None
        while head is not None:
            if head in mp:
                prev.next = None
                return True
            else:
                mp.add(head)
                prev = head
                head = head.next
        return False



# Efficient Approach: Using Floyd’s Cycle Detection Algorithm
# This approach uses a two-pointer – a fast pointer and a slow pointer to determine if there exists a cycle in the loop. 
# The slow pointer moves one node ahead at a time, while the fast pointer moves two nodes ahead at a time.
# If a loop exists in the linked list, the fast and slow pointers are bound to meet at some point.

# Algorithm

# Initialise two pointers, fast and slow to the head of the linked list.
# Traverse through the linked list until the fast pointer doesn’t reach the end of the linked list.
# If the fast pointer reaches the end, it means that the linked list doesn’t contain any cycle. Hence, return False.
# Else, move the slow pointer by one node i.e. slow = slow -> next and fast pointer by two nodes i.e. fast = fast -> next -> next.
# At any point, if the fast and the slow pointers point to the same node, set node-> next = NULL and return True as a loop has been detected.


# Time Complexity:O(N), where N is the number of nodes of the linked list.
# Space Complexity:O(1), as a map is used.

def removeCycle(slow, head):
    curr = head
    while curr:
        ptr = slow
        while ptr.next is not slow and ptr.next is not curr:
            ptr = ptr.next
 
        if ptr.next == curr:
            ptr.next = None
            return
 
        curr = curr.next
 
 
def identifyCycle(head):
    slow = fast = head
 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
 
    return None