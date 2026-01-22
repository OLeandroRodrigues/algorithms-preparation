from problems.linked_list.remove_nth_node_from_end_of_list import ListNode, Solution


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


class TestRemoveNthFromEnd:

    def setup_method(self):
        self.sol = Solution()

    def test_remove_middle_node(self):
        head = build_linked_list([1, 2, 3, 4, 5])

        result = self.sol.removeNthFromEnd(head, 2)

        assert linked_list_to_list(result) == [1, 2, 3, 5]

    def test_remove_last_node(self):
        head = build_linked_list([1, 2, 3])

        result = self.sol.removeNthFromEnd(head, 1)

        assert linked_list_to_list(result) == [1, 2]

    def test_remove_first_node(self):
        head = build_linked_list([1, 2, 3])

        result = self.sol.removeNthFromEnd(head, 3)

        assert linked_list_to_list(result) == [2, 3]

    def test_single_element_list(self):
        head = build_linked_list([10])

        result = self.sol.removeNthFromEnd(head, 1)

        assert result is None

    def test_two_elements_remove_first(self):
        head = build_linked_list([10, 20])

        result = self.sol.removeNthFromEnd(head, 2)

        assert linked_list_to_list(result) == [20]

    def test_two_elements_remove_last(self):
        head = build_linked_list([10, 20])

        result = self.sol.removeNthFromEnd(head, 1)

        assert linked_list_to_list(result) == [10]
