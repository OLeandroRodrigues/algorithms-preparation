# 📝 Circular Linked List Proof

## 📚 Metadata
- **Creator / Inventor**: Not attributed to a single individual  
- **Country of Origin**: Emerged alongside early pointer-based list structures  
- **Institution (if applicable)**: Described in classical computer science literature from the 1960s onward  
- **Year of Creation / Publication**: Formal descriptions appear around 1960  
- **Primary Reference**: *Introduction to Algorithms* — Cormen, Leiserson, Rivest, Stein (CLRS)  
- **Related Concepts**: Node, Pointer, Head, Tail, Next Reference, Cyclic Structures, Circular Buffer, Josephus Problem, Round-Robin Scheduling  
- **Typical Use Cases**: Round-robin algorithms, circular buffers, task scheduling, game turn rotation, any system requiring cyclic iteration  

---

## 📝 Description

A **circular linked list** is a variation of the singly linked list in which the **last node points back to the first node**, forming a continuous cycle:

```
 head
  ↓
[A] → [B] → [C]
 ^           ↓
 └───────────┘
```

In the classic version using a single **tail** pointer:

- Each node stores:
  1. a **value**, and  
  2. a **next** pointer (reference to the next node)  
- The list maintains only a pointer to the **tail**.  
- The **head** is always defined as `tail.next`.  

Properties:

- Empty list: `tail = null`.  
- Non-empty list:
  - `tail.next` is the **head**.
  - Following `next` from head eventually returns to head, after visiting all nodes.

Typical operations:

- `addFirst(x)` — insert at the logical head  
- `addLast(x)` — insert at the logical tail  
- `removeFirst()` — remove the head  
- `getFirst()` — return head value  
- `getLast()` — return tail value  
- `find(x)` — cycle-aware search  
- `isEmpty()` / `size()`  

---

## 📝 Pseudocode

```cpp
STRUCT Node:
    value
    next

STRUCT CircularList:
    tail
    size

INIT(L):
    L.tail = null
    L.size = 0


IS_EMPTY(L):
1  return (L.tail == null)


HEAD(L):
1  if L.tail == null: error "empty list"
2  return L.tail.next


ADD_FIRST(L, x):
1  n = new Node(x)
2  if L.tail == null:
3      L.tail = n
4      n.next = n
5  else:
6      n.next = L.tail.next
7      L.tail.next = n
8  L.size = L.size + 1


ADD_LAST(L, x):
1  ADD_FIRST(L, x)
2  L.tail = L.tail.next


REMOVE_FIRST(L):
1  if L.tail == null: error "empty list"
2  head = L.tail.next
3  v = head.value
4  if head == L.tail:
5      L.tail = null
6  else:
7      L.tail.next = head.next
8  L.size = L.size - 1
9  return v


GET_FIRST(L):
1  if L.tail == null: error "empty list"
2  return L.tail.next.value


GET_LAST(L):
1  if L.tail == null: error "empty list"
2  return L.tail.value


FIND(L, x):
1  if L.tail == null:
2      return null
3  current = L.tail.next
4  do:
5      if current.value == x:
6          return current
7      current = current.next
8  while current != L.tail.next
9  return null
```

---

## ✅ Proof Checklist
- [x] Invariant  
- [x] Correctness  
- [x] Termination  
- [x] Time Complexity  
- [x] Space Complexity  
- [x] Additional Notes  
- [ ] Handwritten Draft (optional)  

---

## 1. Invariant

At any point during operation:

1. **Structural Form**  
   - If empty: `tail = null` and `size = 0`.  
   - If non-empty: `tail != null` and `size ≥ 1`.  

2. **Tail–Head Relation**  
   - `head = tail.next`.  
   - Walking `next` exactly `size` times starting from head returns to head.  

3. **Cycle Integrity**  
   - The list contains exactly **one simple directed cycle**.  
   - All nodes are reachable from `tail.next`.  

4. **Size Accuracy**  
   - `size` equals the number of nodes reachable in one full cycle traversal.

These invariants ensure the structure remains **valid, consistent, circular, and connected**.

---

## 2. Correctness

### ADD_FIRST

- **Empty list**:  
  - The new node points to itself (`n.next = n`) and `tail = n`.  
  - The list becomes a 1-node cycle; invariants are satisfied.

- **Non-empty list**:  
  - The new node is inserted before the current head:  
    - `n.next = tail.next`  
    - `tail.next = n`  
  - The cycle is preserved. The head changes, but all nodes are still in a single cycle.

### ADD_LAST

- Implemented as:
  1. `addFirst(x)`  
  2. `tail = tail.next` (advance tail to the newly inserted node)  

Because the list is circular, advancing `tail` to `tail.next` after `addFirst` makes the new node the last node, correctly implementing insertion at the tail without breaking the cycle.

### REMOVE_FIRST

- **One-node list** (`head == tail`):  
  - After removal, `tail` is set to `null`, `size` becomes 0.  
  - The list is now empty, which matches the invariants for the empty state.

- **Multi-node list**:  
  - `head = tail.next`  
  - `tail.next = head.next` bypasses the old head, linking tail directly to the second node.  
  - Remaining nodes still form one simple cycle.  
  - `size` decreases by 1, staying consistent with the number of nodes.

### GET_FIRST / GET_LAST

- They simply read:
  - `getFirst()` → `tail.next.value`  
  - `getLast()` → `tail.value`  
- No mutation is performed; invariants are trivially preserved.

### FIND

- Starts from `head = tail.next` and loops until it either:
  - Finds a node with value `x`, or  
  - Returns to `head` after a full cycle.  
- Because the structure is guaranteed to be a single simple cycle:
  - All nodes are visited at most once.  
  - If `x` is present, it will be found before returning to head.  
  - If not, the algorithm safely terminates when it re-encounters head.

Thus, every operation preserves the invariants and implements its intended behavior correctly.

---

## 3. Termination

- `addFirst`, `addLast`, `removeFirst`, `getFirst`, `getLast`, `isEmpty`, `size`  
  - Each consists of a finite number of assignments, checks, and pointer manipulations.  
  - They contain **no loops** → always terminate in constant time.

- `find(x)`  
  - Contains a loop that advances `current = current.next` each iteration.  
  - Due to the circular invariant, after at most `size` steps we return to the starting node (`head`).  
  - The loop condition explicitly checks for that, guaranteeing termination.

Therefore, all operations are **finite and deterministic**.

---

## 4. Time Complexity

| Operation       | Complexity | Notes                                      |
|-----------------|------------|--------------------------------------------|
| `addFirst(x)`   | O(1)       | Constant pointer updates                   |
| `addLast(x)`    | O(1)       | Implemented via `addFirst` + tail shift   |
| `removeFirst()` | O(1)       | Removes logical head                       |
| `getFirst()`    | O(1)       | Direct access to `tail.next`              |
| `getLast()`     | O(1)       | Direct access to `tail`                   |
| `find(x)`       | O(n)       | May visit every node once in the cycle    |
| `isEmpty()`     | O(1)       | Checks `tail == null`                     |
| `size()`        | O(1)       | Maintained as a counter                   |

Here, `n` is the number of elements in the list.

---

## 5. Space Complexity

| Aspect                      | Complexity | Explanation                                      |
|----------------------------|------------|--------------------------------------------------|
| Auxiliary Space             | O(1)       | Only a few local variables                       |
| Total Space (n nodes)       | O(n)       | One node per element                             |
| Node Overhead               | O(1)       | Each node stores one pointer (`next`) and value |
| In-Place?                   | Yes        | Operations mutate the list directly              |
| Circularity Overhead        | O(1)       | Just one extra pointer: `tail`                   |

---

## 6. Additional Notes

- Circular linked lists are ideal when the structure must **naturally wrap around**, such as in:
  - Round-robin process scheduling  
  - Multiplayer turn-based games  
  - Circular buffers and queues  
  - Token ring protocols  
  - Classic algorithmic puzzles like the **Josephus problem**

- Compared to a regular singly linked list:
  - There is no `null` at the end; termination conditions for traversal must be explicitly based on cycle detection (e.g., “stop when we return to head” or “after size steps”).  

- Compared to a doubly linked list:
  - Uses less memory (only `next`, not `prev`).  
  - But does not support backward traversal or O(1) deletion of an arbitrary node without knowing its predecessor.

---

## 7. 📷 Handwritten Draft (optional)

