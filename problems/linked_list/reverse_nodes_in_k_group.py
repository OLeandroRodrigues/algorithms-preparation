"""
Problem: Reverse Nodes in k-Group

Description:
Given the head of a singly linked list and an integer k,
reverse the nodes of the list k at a time and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k, then the remaining nodes at the end
should remain in the same order.

Input:
- head (ListNode): head of the singly linked list
- k (int): group size for reversing

Output:
- ListNode: head of the modified linked list

Constraints:
- The number of nodes is in the range [0, 5000]
- 0 <= Node.val <= 1000
- 1 <= k <= number of nodes

Examples:
Input:
    head = [1, 2, 3, 4, 5], k = 2
Output:
    [2, 1, 4, 3, 5]

Input:
    head = [1, 2, 3, 4, 5], k = 3
Output:
    [3, 2, 1, 4, 5]

Approach:
Use pointer manipulation with a dummy node:
1) Use a dummy node pointing to head.
2) For each group:
   - Check if there are at least k nodes ahead. If not, stop.
   - Reverse the k nodes in-place.
   - Connect the reversed group back to the previous part of the list.
3) Return dummy.next as the new head.

Key idea:
You must reconnect pointers correctly:
- prevGroupTail -> newGroupHead
- oldGroupHead (becomes tail) -> nextGroupHead

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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Implement your solution here
        pass