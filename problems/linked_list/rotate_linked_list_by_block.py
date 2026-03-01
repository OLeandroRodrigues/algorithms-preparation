"""
Problem: Rotate Linked List by Block

Description:
Given the head of a singly linked list and an integer k,
rotate the list to the right by k positions, but only within blocks of size k.

More precisely:
- Divide the list into consecutive blocks of size k.
- For each complete block, rotate the nodes within that block to the right by one position.
- If the last block has fewer than k nodes, leave it unchanged.

Input:
- head (ListNode): head of the singly linked list
- k (int): block size

Output:
- ListNode: head of the modified linked list

Constraints:
- The number of nodes is in the range [1, 5000]
- 0 <= Node.val <= 1000
- 1 <= k <= length of list

Examples:
Input:
    head = [1, 2, 3, 4, 5, 6], k = 3
Output:
    [3, 1, 2, 6, 4, 5]

Explanation:
Block 1: [1,2,3] → rotate right → [3,1,2]
Block 2: [4,5,6] → rotate right → [6,4,5]

Input:
    head = [1, 2, 3, 4, 5], k = 3
Output:
    [3, 1, 2, 4, 5]

Explanation:
Block 1: [1,2,3] → [3,1,2]
Block 2: [4,5] → unchanged (less than k)

Approach:
- Use a dummy node to simplify reconnections.
- For each block:
    1) Check if there are at least k nodes.
    2) Find the last node of the block.
    3) Detach the block temporarily.
    4) Move the last node of the block to the front.
    5) Reconnect the modified block to the main list.
- Continue until no full block remains.

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
    def rotateBlock(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Implement your solution here
        pass