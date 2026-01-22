"""
Problem: Remove Nth Node From End of List

Description:
You are given the head of a singly linked list.
Remove the nth node from the end of the list and return the new head.

Input:
- head (ListNode): head of the singly linked list
- n (int): position from the end of the list to remove

Output:
- ListNode: head of the updated linked list

Constraints:
- The number of nodes in the list is in the range [1, 10^4]
- 1 <= n <= length of the list
- The list is singly linked

Examples:
Input:
    head = [1,2,3,4,5], n = 2
Output:
    [1,2,3,5]

Explanation:
The 2nd node from the end is the node with value 4, which is removed.

Approach:
Use the two-pointer technique:
- Initialize two pointers (fast and slow) at the head
- Move the fast pointer n steps ahead
- Move both pointers together until fast reaches the end
- The slow pointer will be just before the node to remove
- Adjust pointers to remove the target node

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        fast = slow = dummy

        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # remove the target node
        slow.next = slow.next.next

        return dummy.next
        
