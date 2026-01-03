from problems.linked_list.add_two_numbers import ListNode, Solution


def build_linked_list(values):
    """Helper to build a linked list from a Python list."""
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def linked_list_to_list(node):
    """Helper to convert a linked list back to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class TestAddTwoNumbers:

    def setup_method(self):
        self.sol = Solution()

    def test_example_1(self):
        l1 = build_linked_list([2, 4, 3])
        l2 = build_linked_list([5, 6, 4])

        result = self.sol.addTwoNumbers(l1, l2)

        assert linked_list_to_list(result) == [7, 0, 8]

    def test_example_2(self):
        l1 = build_linked_list([0])
        l2 = build_linked_list([0])

        result = self.sol.addTwoNumbers(l1, l2)

        assert linked_list_to_list(result) == [0]

    def test_example_3(self):
        l1 = build_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = build_linked_list([9, 9, 9, 9])

        result = self.sol.addTwoNumbers(l1, l2)

        assert linked_list_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]

    def test_different_lengths(self):
        l1 = build_linked_list([1, 8])
        l2 = build_linked_list([0])

        result = self.sol.addTwoNumbers(l1, l2)

        assert linked_list_to_list(result) == [1, 8]

    def test_carry_at_end(self):
        l1 = build_linked_list([5])
        l2 = build_linked_list([5])

        result = self.sol.addTwoNumbers(l1, l2)

        assert linked_list_to_list(result) == [0, 1]
