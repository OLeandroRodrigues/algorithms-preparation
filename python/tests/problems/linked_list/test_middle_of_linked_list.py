from problems.linked_list.middle_of_linked_list import ListNode, Solution


def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class TestMiddleOfLinkedList:

    def setup_method(self):
        self.sol = Solution()

    def test_odd_length_list(self):
        head = build_linked_list([1, 2, 3, 4, 5])

        result = self.sol.middleNode(head)

        assert linked_list_to_list(result) == [3, 4, 5]

    def test_even_length_list(self):
        head = build_linked_list([1, 2, 3, 4, 5, 6])

        result = self.sol.middleNode(head)

        assert linked_list_to_list(result) == [4, 5, 6]

    def test_single_node(self):
        head = build_linked_list([42])

        result = self.sol.middleNode(head)

        assert linked_list_to_list(result) == [42]

    def test_two_nodes(self):
        head = build_linked_list([10, 20])

        result = self.sol.middleNode(head)

        assert linked_list_to_list(result) == [20]

    def test_longer_list(self):
        head = build_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])

        result = self.sol.middleNode(head)

        assert linked_list_to_list(result) == [5, 6, 7, 8, 9]
