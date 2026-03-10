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
        
        if head is None or k == 1:
            return head

        dummy = ListNode(0, head)
        prev_group_tail = dummy

        while True:
            # 1) Check if there are at least k nodes left
            kth = prev_group_tail
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            # 2) Identify group boundaries
            group_head = prev_group_tail.next
            next_group_head = kth.next

            # 3) Reverse current group
            prev = next_group_head
            curr = group_head

            while curr != next_group_head:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # 4) Reconnect reversed group
            prev_group_tail.next = kth
            prev_group_tail = group_head
        
       

    




        

        