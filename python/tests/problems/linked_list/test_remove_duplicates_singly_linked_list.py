import pytest

from problems.linked_list.remove_duplicates_singly_linked_list import ListNode, Solution


def build_linked_list(values):
    """Builds a singly linked list from a Python list and returns head."""
    if not values:
        return None

    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def linked_list_to_list(head, limit=10_000):
    """Converts a linked list to a Python list. limit avoids infinite loops."""
    out = []
    cur = head
    steps = 0
    while cur is not None:
        out.append(cur.val)
        cur = cur.next
        steps += 1
        if steps > limit:
            raise RuntimeError("Possible cycle detected while converting linked list.")
    return out


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 3, 2, 3, 4, 1, 2], [1, 3, 2, 4]),
        ([1, 1, 1, 1], [1]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([2, 2, 1, 1, 2], [2, 1]),
        ([0, 0, 1, 0, 1, 2, 2], [0, 1, 2]),
        ([], []),
    ],
)
def test_remove_duplicates(values, expected):
    head = build_linked_list(values)
    result = Solution().removeDuplicates(head)
    assert linked_list_to_list(result) == expected


def test_remove_duplicates_single_node():
    head = build_linked_list([7])
    result = Solution().removeDuplicates(head)
    assert linked_list_to_list(result) == [7]


def test_remove_duplicates_returns_same_head_reference_when_not_empty():
    head = build_linked_list([1, 2, 1])
    original_head = head

    result = Solution().removeDuplicates(head)

    # It should mutate in-place and return the (same) head node reference
    assert result is original_head
    assert linked_list_to_list(result) == [1, 2]
