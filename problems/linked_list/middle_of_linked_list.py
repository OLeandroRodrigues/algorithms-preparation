"""
Problem: Middle of the Linked List

Description:
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Input:
- head (ListNode): head of the singly linked list

Output:
- ListNode: the middle node of the linked list

Constraints:
- The number of nodes is in the range [1, 100]
- 1 <= Node.val <= 100

Examples:
Input:
    head = [1, 2, 3, 4, 5]
Output:
    [3, 4, 5]

Input:
    head = [1, 2, 3, 4, 5, 6]
Output:
    [4, 5, 6]

Approach:
Use the two-pointer (slow & fast) technique:
- slow moves one step at a time
- fast moves two steps at a time
When fast reaches the end, slow is at the middle.
If the list has even length, slow naturally points to the second middle node.

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
