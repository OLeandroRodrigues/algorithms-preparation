# 📝 Queue Proof

## 📚 Metadata
- **Creator / Inventor**: Not attributed to a single individual
- **Country of Origin**: Concept emerged independently in multiple computing centers
- **Institution (if applicable)**: Early adoption in queueing theory (A.K. Erlang, 1909); formalized in computer science by the 1950s–1960s
- **Year of Creation / Publication**: Concept existed in telecommunication models (1909); adopted as an abstract data type in computing by the 1960s
- **Primary Reference**: Erlang, A. K. (1909). “The Theory of Probabilities and Telephone Conversations” — Nyt Tidsskrift for Matematik B, 20, 33–39
- **Related Concepts**: FIFO (First-In, First-Out), Buffer, Scheduling Queue, Job Queue, Message Queue
- **Typical Use Cases**: Task scheduling, I/O buffering, inter-process communication, print spooling, breadth-first search (BFS)

## 📝 Description
A **queue** is a linear data structure that stores elements in a **FIFO (First In, First Out)** order.
It operates much like a real-world waiting line — the **first element to enter** is the **first one** to leave.

Typical queue operations include:

- `enqueue(x)`: add an element x to the rear (back) of the queue.
- `dequeue()`: remove and return the element from the front of the queue.
- `peek()`: return the element at the front without removing it.
- `isEmpty()`: check whether the queue has no elements.
- `size()`: return the current number of elements.


## 📝 Pseudocode
cpp
```
ENQUEUE(Q,x)
1  Q[Q.tail] = x
2  if Q.tail == Q.size
3     Q.tail = 1 
4  else Q.tail = Q.tail + 1

DEQUEUE(Q)
1 x = Q[Q.head]
2 if Q.head == Q.size
3    Q.head = 1 
4 else Q.head = Q.head + 1
5 return x

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
The **head** of the queue always refers to the **oldest element** that has not yet been removed,
and the **tail** refers to the **most recently enqueued element**.

Formally, after each operation:

- All elements between the head and tail maintain their **insertion order**.
- The element at the head is always the **next to be dequeued**.
- The element at the tail is always the **most recently enqueued**.
- For every valid sequence of operations, the queue maintains the **FIFO (First In, First Out)** invariant.

---

## 2. Correctness
**Enqueue operation**
- Appends a new element at the **tail** (end) of the underlying list or linked structure.
- Maintains the invariant: all existing elements retain their relative order, and the new element becomes the most recent (tail).

**Dequeue operation**
- Removes and returns the element currently at the **head** of the queue.
- Maintains the invariant: after removal, the next oldest element becomes the new head, preserving FIFO order.

**Peek operation**
- Returns the element at the **head** without removing it, providing read-only access.

Therefore, for every valid sequence of `enqueue`, `dequeue`, and `peek`,
the queue’s observable behavior satisfies **FIFO — First In, First Out** semantics.

---

## 3. Termination
Every operation (`enqueue`, `dequeue`, `peek`, `isEmpty`, `size`) performs a **finite number of constant-time steps** and terminates deterministically.

- Each enqueue and dequeue performs one constant-time append/remove at the tail or head.
- There are no recursive calls or loops dependent on n.

Hence, all operations terminate in O(1) time for linked-list or pointer-based implementations.
(Note: Array-based queues may require O(n) in rare cases if resizing occurs.)

---

## 4. Time Complexity
Operation                 | Complexity    | Notes                                       |
|-------------------------|---------------|---------------------------------------------|
| enqueue(x)              | O(1)          | Insert element at tail                      |
| dequeue()               | O(1)          | Remove element from head                    |
| peek()                  | O(1)          | Access head element only                    |
| isEmpty()               | O(1)          | Boolean check on element count              |
| size()                  | O(1)          | Constant-time length lookup or counter read |

---

## 5. Space Complexity

| Aspect                  | Complexity     | Explanation                                              |
|-------------------------|----------------|----------------------------------------------------------|
| Auxiliary Space         | O(1)           | No extra buffers beyond internal storage                 |
|Total Space (n elements) | O(n)           | Stores all enqueued elements                             |
| In-Place?               | Yes            | All operations occur within the same underlying container|
| Stability               | Preserved      | The queue preserves insertion order (FIFO)               |

---

## 6. Additional Notes
The **Queue** is an **Abstract Data Type (ADT)** with **two access points**:

- **Head** → for removal (`dequeue`, `peek`)
- **Tail** → for insertion (`enqueue`)

- **Core property**: FIFO (First In, First Out).
-  **Typical use cases include**:
    - **Task scheduling** and CPU job queues
    - **I/O buffering** (e.g., print queues, network buffers)
    - **Message passing** in distributed systems
    - **Breadth-First Search (BFS)** in graph algorithms

Any violation of the invariant — e.g., attempting to `dequeue` or `peek` from an empty queue —
must raise an **exception** to ensure the data structure’s logical correctness.

---

## 7. 📷 Handwritten Draft (optional)
My initial handwritten proof draft is available here:  
