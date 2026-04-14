from problems.linked_list.rotate_linked_list_by_block import ListNode, Solution


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


class TestRotateLinkedListByBlock:

    def setup_method(self):
        self.sol = Solution()

    def test_rotate_blocks_of_three_exact_multiple(self):
        head = build_linked_list([1, 2, 3, 4, 5, 6])

        result = self.sol.rotateBlock(head, 3)

        assert linked_list_to_list(result) == [3, 1, 2, 6, 4, 5]

    def test_rotate_first_block_only_last_incomplete(self):
        head = build_linked_list([1, 2, 3, 4, 5])

        result = self.sol.rotateBlock(head, 3)

        assert linked_list_to_list(result) == [3, 1, 2, 4, 5]

    def test_k_equals_one(self):
        head = build_linked_list([1, 2, 3])

        result = self.sol.rotateBlock(head, 1)

        assert linked_list_to_list(result) == [1, 2, 3]

    def test_single_node(self):
        head = build_linked_list([1])

        result = self.sol.rotateBlock(head, 1)

        assert linked_list_to_list(result) == [1]

    def test_block_size_equals_list_length(self):
        head = build_linked_list([1, 2, 3, 4])

        result = self.sol.rotateBlock(head, 4)

        assert linked_list_to_list(result) == [4, 1, 2, 3]

    def test_two_node_blocks(self):
        head = build_linked_list([1, 2, 3, 4, 5, 6])

        result = self.sol.rotateBlock(head, 2)

        assert linked_list_to_list(result) == [2, 1, 4, 3, 6, 5]

    def test_last_block_unchanged(self):
        head = build_linked_list([1, 2, 3, 4, 5, 6, 7])

        result = self.sol.rotateBlock(head, 3)

        assert linked_list_to_list(result) == [3, 1, 2, 6, 4, 5, 7]

    def test_empty_list(self):
        result = self.sol.rotateBlock(None, 3)

        assert result is None