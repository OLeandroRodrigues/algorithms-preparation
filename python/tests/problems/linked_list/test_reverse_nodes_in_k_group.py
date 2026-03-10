from problems.linked_list.reverse_nodes_in_k_group import ListNode, Solution


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


class TestReverseNodesInKGroup:

    def setup_method(self):
        self.sol = Solution()

    def test_reverse_pairs(self):
        head = build_linked_list([1, 2, 3, 4, 5])

        result = self.sol.reverseKGroup(head, 2)

        assert linked_list_to_list(result) == [2, 1, 4, 3, 5]

    def test_reverse_triplets(self):
        head = build_linked_list([1, 2, 3, 4, 5])

        result = self.sol.reverseKGroup(head, 3)

        assert linked_list_to_list(result) == [3, 2, 1, 4, 5]

    def test_exact_multiple_groups(self):
        head = build_linked_list([1, 2, 3, 4, 5, 6])

        result = self.sol.reverseKGroup(head, 3)

        assert linked_list_to_list(result) == [3, 2, 1, 6, 5, 4]

    def test_k_equals_one(self):
        head = build_linked_list([1, 2, 3])

        result = self.sol.reverseKGroup(head, 1)

        assert linked_list_to_list(result) == [1, 2, 3]

    def test_single_node(self):
        head = build_linked_list([1])

        result = self.sol.reverseKGroup(head, 2)

        assert linked_list_to_list(result) == [1]

    def test_last_group_not_reversed(self):
        head = build_linked_list([1, 2, 3, 4, 5])

        result = self.sol.reverseKGroup(head, 4)

        assert linked_list_to_list(result) == [4, 3, 2, 1, 5]

    def test_empty_list(self):
        result = self.sol.reverseKGroup(None, 3)

        assert result is None