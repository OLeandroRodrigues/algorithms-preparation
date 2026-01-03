"""
Problem: 2. Add Two Numbers (leetcode)

Description:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.
Add the two numbers and return the sum as a linked list.

Input:
- l1 (ListNode): head of the first linked list
- l2 (ListNode): head of the second linked list

Output:
- ListNode: head of the resulting linked list

Constraints:
- The number of nodes in each linked list is in the range [1, 100]
- 0 <= Node.val <= 9
- No leading zeros, except for the number 0 itself

Examples:
Input:
    l1 = [2,4,3], l2 = [5,6,4]
Output:
    [7,0,8]

Explanation:
    342 + 465 = 807

Approach:
Simulate elementary addition digit by digit:
- Traverse both lists simultaneously
- Keep track of carry
- Create a new node for each digit of the result

Time Complexity:
- O(max(n, m))

Space Complexity:
- O(max(n, m))
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]) -> Optional[ListNode]:
    
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next
            

