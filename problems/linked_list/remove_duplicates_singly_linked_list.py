"""Problem: Remove Duplicates from Unsorted Singly Linked List

Description:
Given the head of an unsorted singly linked list, remove all duplicate values
so that each value appears only once. The first occurrence of each value
must be preserved.

You are NOT allowed to use:
- arrays
- sets
- dictionaries
- any auxiliary data structures

The solution must manipulate only the pointers of the linked list itself.

Input:
- head (ListNode): head of the singly linked list

Output:
- ListNode: head of the linked list with duplicates removed

Constraints:
- The number of nodes is in the range [0, 100]
- 0 <= Node.val <= 100
- The linked list is NOT sorted

Examples:
Input:
    head = [1, 3, 2, 3, 4, 1, 2]
Output:
    [1, 3, 2, 4]

Explanation:
    The first occurrences of each value are kept:
    - 1 (keeps)
    - 3 (keeps)
    - 2 (keeps)
    - 3 (removed)
    - 4 (keeps)
    - 1 (removed)
    - 2 (removed)

Approach:
Use two pointers:
- The outer pointer (current) traverses each node in the list
- The inner pointer (runner) checks all subsequent nodes
If runner.next has the same value as current, remove it by skipping the node

This approach avoids extra memory usage and relies purely on pointer manipulation.

Time Complexity:
- O(n²)

Space Complexity:
- O(1)"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeDuplicates(
        self,
        head: Optional[ListNode]
    ) -> Optional[ListNode]:

        current = head

        while current:
            runner = current

            while runner.next:
                if runner.next.val == current.val:
                    # remove duplicate node
                    runner.next = runner.next.next
                else:
                    runner = runner.next

            current = current.next

        return head