# 📝 Singly Linked List Proof

## 📚 Metadata
- **Creator / Inventor**: Not attributed to a single individual
- **Country of Origin**: Concept appeared in early computing and mathematical list manipulation
- **Institution (if applicable)**: Popularized in classical computer science literature in the 1950s–1960s
- **Year of Creation / Publication**: Formal use in CS appears around 1955–1960
- **Primary Reference**: Cormen, Leiserson, Rivest, Stein — Introduction to Algorithms (CLRS)
- **Related Concepts**: Node, Pointer, Head, Tail, Next Reference
- **Typical Use Cases**: Dynamic memory structures, chaining in hash tables, adjacency lists in graphs, frequent insert/delete operations

## 📝 Description
A **singly linked list** is a linear data structure composed of nodes, each containing:

1. a **value**, and
2. a reference (**next pointer**) to the next node in the sequence.

The list is accessed through its **head**.
If a **tail** pointer is maintained, insertion at the end becomes O(1).

Typical operations:

- `push_front(x)` — insert at the beginning
- `push_back(x)` — insert at the end (O(1) with tail)
- `insert_after(node, x)`
- `pop_front()` — remove first element
- `remove_after(node)`
- `find(value)`
- `isEmpty() / size()`

The structure allows efficient insertion and deletion when the target node is known, but **random access is O(n)** since traversal is required.

## 📝 Pseudocode
cpp
```
STRUCT Node:
    value
    next

PUSH_FRONT(L, x):
1  n = new Node(x)
2  n.next = L.head
3  L.head = n
4  if L.tail == null:
5      L.tail = n

PUSH_BACK(L, x):
1  n = new Node(x)
2  if L.tail == null:
3      L.head = L.tail = n
4  else:
5      L.tail.next = n
6      L.tail = n

POP_FRONT(L):
1  if L.head == null:
2      error "empty list"
3  v = L.head.value
4  L.head = L.head.next
5  if L.head == null:
6      L.tail = null
7  return v

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
At any moment during execution:

- `head always` points to the **first node** in the list, or `null` if the list is empty.
- If maintained, `tail` always points to the **last node**, and `tail.next = null`.
- Every node’s `next` pointer either references the next node in sequence or is `null` (end-of-list).
- Traversing from `head` via `next` references yields **all nodes in order** without cycles.
- Insertions and deletions maintain a **single, linear chain** of nodes.

This invariant guarantees that the list is **well-formed, acyclic, and linearly ordered**.

---

## 2. Correctness
**Insertion (push_front, push_back)**
- `push_front` updates only two pointers: the new node’s `next` and the list’s `head`.
- `push_back`updates `tail.next` and the new `tail`, preserving sequence order.
- No existing links between nodes are altered incorrectly.

**Deletion (pop_front, remove_after)**
- `pop_front` moves the head pointer to the next node, preserving the remaining list.
- If the list becomes empty, `tail = null`, maintaining consistency.
- `remove_after(node)` reconnects node → successor correctly.

**Traversal & Search**

- Starting at `head`, repeated application of `next` eventually reaches `null`, ensuring no infinite loop if invariant holds.

Thus every operation preserves the logical structure of a **singly linked chain of nodes**.

---

## 3. Termination
Every operation consists of a **finite sequence** of pointer reads and writes:

- `push_front`, `push_back`, `pop_front`, `remove_after` all run in **constant time** with no loops.
- Traversal-based operations (`find`, computing size without counter) perform at most **n steps**, where n is the number of nodes.

Therefore, all procedures terminate deterministically.

---

## 4. Time Complexity
Operation                 | Complexity                                  | Notes                                       |
|-------------------------|---------------------------------------------|---------------------------------------------|
| push_front(x)           | O(1)                                        | Adjusts head pointer                        |         
| push_back(x)            | O(1) with tail, O(n) without tail           | Remove element from head                    |
| insert_after(node, x)   | O(1)                                        | Requires pointer to node                    |
| pop_front()             | O(1)                                        | Move head pointer                           |
| remove_after(node)      | O(1)                                        | Reconnect pointers                          |
| find(key)               | O(1)                                        | Sequential traversal                        |
| size()                  | O(1) with counter; O(n) otherwise           | Counter optional                            |


---

## 5. Space Complexity

| Aspect                  | Complexity     | Explanation                                              |
|-------------------------|----------------|----------------------------------------------------------|
| Auxiliary Space         | O(1)           | Only pointer manipulation                                |
|Total Space (n elements) | O(n)           | One node per element                                     |
|Node Overhead            | O(1)           | One next pointer per node                                |
| In-Place?               | Yes            | Structure mutates itself                                 |
| Stability               | Preserved      | Node order is maintained                                 |

---

## 6. Additional Notes
- Singly linked lists are ideal when **insertions and deletions dominate** over indexed access.
- Widely used in:
    * hash table chaining
    * adjacency lists in graph structures
    * memory allocators and free lists
    * undo/redo logs

- They eliminate array resizing and avoid shifting large blocks of memory.
- The main limitation: **no direct indexing**, requiring O(n) traversal.

---

## 7. 📷 Handwritten Draft (optional)
My initial handwritten proof draft is available here:  
