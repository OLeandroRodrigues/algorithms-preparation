# 📝 Doubly Linked List Proof

## 📚 Metadata
- **Creator / Inventor**: Not attributed to a single inventor
- **Country of Origin**: Developed conceptually alongside early pointer-based data structures
- **Institution (if applicable)**: Described in classical computer science literature from the 1960s onward
- **Year of Creation / Publication**: Formal descriptions appear around 1960
- **Primary Reference**: Cormen, Leiserson, Rivest, Stein — Introduction to Algorithms (CLRS)
- **Related Concepts**: Node, Pointer, Prev Reference, Next Reference, Sentinel Node, Deque
- **Typical Use Cases**: Efficient bidirectional traversal, deletion/insertion in O(1) at arbitrary positions, LRU caches, text editors, browser history navigation

## 📝 Description
A **doubly linked list** is a linear data structure composed of nodes, where **each node contains**:


1. a **value**, and
2. a reference (**prev pointer**) to the previous node, and.
3. a reference (**next pointer**) to the next node.

The structure supports **bidirectional traversal**:

prev ← **[node]** → next

Access typically starts at the **head** (first node), and if maintained, a **tail** pointer references the last node, enabling O(1) insertion at both ends.

Typical operations:

- `push_front(x)` — insert at the beginning
- `push_back(x)` — insert at the end (O(1) with tail)
- `insert_after(node, x)`
- `insert_before(node, x)`
- `pop_front()` — remove first element
- `pop_back()` — remove last element
- `remove(node)` — remove an arbitrary node in O(1)
- `find(value)`
- `isEmpty() / size()`

Unlike singly linked lists, a doubly linked list allows efficient deletion/insertion even when only the target node is known, since both neighbors are directly accessible.

## 📝 Pseudocode
cpp
```
STRUCT Node:
    value
    prev
    next

PUSH_FRONT(L, x):
1  n = new Node(x)
2  n.next = L.head
3  n.prev = null
4  if L.head != null:
5      L.head.prev = n
6  L.head = n
7  if L.tail == null:
8      L.tail = n

PUSH_BACK(L, x):
1  n = new Node(x)
2  n.prev = L.tail
3  n.next = null
4  if L.tail != null:
5      L.tail.next = n
6  L.tail = n
7  if L.head == null:
8      L.head = n

INSERT_AFTER(node, x):
1  if node == null: error
2  n = new Node(x)
3  n.prev = node
4  n.next = node.next
5  if node.next != null:
6      node.next.prev = n
7  node.next = n
8  if L.tail == node:
9      L.tail = n

POP_FRONT(L):
1  if L.head == null: error "empty list"
2  v = L.head.value
3  L.head = L.head.next
4  if L.head != null:
5      L.head.prev = null
6  else:
7      L.tail = null
8  return v

REMOVE(L, node):
1  if node.prev != null:
2      node.prev.next = node.next
3  else:
4      L.head = node.next
5  if node.next != null:
6      node.next.prev = node.prev
7  else:
8      L.tail = node.prev
9  return node.value


```

## ✅ Proof Checklist
- [x] Invariant  
- [x] Correctness  
- [x] Termination  
- [x] Time Complexity  
- [x] Space Complexity  
- [x] Additional Notes  
- [ ] Handwritten Draft (optional)  

## 1. Invariant
At any point during execution:
- `head` points to the **first node**, or `null` if the list is empty.
- `tail` points to the **last node**, or `null` if the list is empty.
- Every node satisfies:
    * `node.next.prev == node` (for all nodes except the last)
    * `node.prev.next == node` (for all nodes except the first)
- The sequence of `next` pointers produces a **linear chain from head to tail**.
- The sequence of `prev` pointers produces a **reverse linear chain from tail to head**.
- There are **no cycles**, unless intentionally implemented using a sentinel or circular version.

These invariants ensure the structure is **well-formed, bidirectionally consistent, and acyclic**.

---

## 2. Correctness
**Insertion (push_front, push_back, insert_after, insert_before)**
- All insert operations correctly update **both** `next` and `prev` pointers of neighboring nodes.
- Updates maintain bidirectional consistency:
    * `If A.next = B, then B.prev = A.`

**Deletion (pop_front, pop_back, remove)**
- Removing a node reconnects its neighbors without needing traversal.
- Edge cases (removing head or tail) properly adjust list boundaries.
- When list becomes empty, `head = tail = null`.

**Traversal**
Forward traversal (`head → next → ...`) and backward traversal (`tail → prev → ...`) always reach `null` within a finite number of steps, confirming correctness and absence of cycles.

---

## 3. Termination
Every operation runs as a **finite sequence** of pointer updates:

- All modifications (`push_front`, `push_back`, `insert_after`, `remove`, `pop_front`, `pop_back`) run in **O(1)** time, with no loops.
- Traversal operations (`find`, reverse find) iterate at most **n steps**, where n is the size of the list.

Therefore, all procedures terminate deterministically.

---

## 4. Time Complexity
Operation               | Complexity                      | Notes                                   |
|-----------------------|---------------------------------|-----------------------------------------|
| push_front(x)         | O(1)                            | Update head and neighbor pointers       |         
| push_back(x)          | O(1)                            | Update tail and neighbor pointers       |
| insert_after(node, x) | O(1)                            | Requires direct reference to node       |
| insert_before(node, x)| O(1)                            | Symmetric to insert_after               |
| pop_front()           | O(1)                            | Remove head                             |
| pop_back()            | O(1)                            | Remove tail                             |
| remove(node)          | O(1)                            | Remove arbitrary node without traversal |
| find(x)               | O(1)                            | Sequential traversal                    |
| reverse_find(x)       | O(1)                            | Optional backward traversal             |
| size()                | O(1) with counter O(n) without  | Same as singly linked                   |



---

## 5. Space Complexity

| Aspect                   | Complexity     | Explanation                                              |
|--------------------------|----------------|----------------------------------------------------------|
| Auxiliary Space          | O(1)           | Only pointer manipulation                                |
| Total Space (n elements) | O(n)           | One node per element                                     |
| Node Overhead            | O(1)           | Two pointers per node: prev and next                     |
| In-Place?                | Yes            | Operations modify existing structure                     |
| Bidirectionality Cost    | Extra O(n)     | Additional prev pointer per node                         |

---

## 6. Additional Notes
- Doubly linked lists are ideal when **removal and insertion anywhere in the list** must be performed in **constant time**.
- Common real-world applications:
    * **LRU caches** (e.g., browser caching algorithms)
    * **text editors** (cursor movement both forward and backward)
    * **browser history** (navigate back/forward efficiently)
    * **deques** (double-ended queues)
- They eliminate the need to traverse the list for deletion, unlike singly linked lists where the predecessor must be found.
- Main limitation: increased memory cost and slightly more complex pointer management.

---

## 7. 📷 Handwritten Draft (optional)
My initial handwritten proof draft is available here:  
