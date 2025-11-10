# 📝 Stack Proof

## 📚 Metadata
- **Creator / Inventor**: Friedrich L. Bauer and Klaus Samelson  
- **Country of Origin**: Germany  
- **Institution (if applicable)**: Technical University of Munich  
- **Year of Creation / Publication**: Concept formalized in 1957 (published 1964)  
- **Primary Reference**: Bauer, F. L., & Samelson, K. (1964). “Sequential Formula Translation” — *Communications of the ACM, 7(3), 114–115*  
- **Related Concepts**: LIFO (Last-In, First-Out), Recursion Stack, Call Stack, Stack Frame  
- **Typical Use Cases**: Expression evaluation, parsing, recursion management, undo/redo systems, DFS traversal  

## 📝 Description
A **stack** is a linear data structure that stores elements in a **LIFO (Last In, First Out)** order.
It works similarly to a stack of physical objects — such as plates or books — where the **last item placed on top** is the **first one to be removed**.

Typical stack operations include:
- push(x): add an element x to the top of the stack.
- pop(): remove and return the element from the top.
- peek(): return the top element without removing it.
- isEmpty(): check whether the stack is empty.


## 📝 Pseudocode
cpp
```
STACK-EMPTY(S)
1 if S.top == 0 
2    return TRUE
3 else return FALSE

PUSH(S,x)
1 if S.top == S.size
2    error "overflow"
3 else S.top == S.top + 1
4    S[S.top] = x 

POP(S)
1 if STACK-EMPTY(S)
2    error "underflow"
3 else S.top = S.top - 1
4    return S[S.top + 1]
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
At any point during the execution:
The top of the stack always refers to the most recently inserted element that has not yet been removed.

Formally, after each operation:

- All elements below the top remain unchanged.
- The relative order of elements in the stack corresponds exactly to the order in which they were pushed.
- Thus, for every valid sequence of operations, the stack maintains the LIFO property invariant.

---

## 2. Correctness
**Push operation**
- Appends a new element at the top (end of the underlying list).
- Maintains the invariant because the new element becomes the last inserted (top).

**Pop operation**
- Removes and returns the element currently at the top.
- Maintains the invariant because all remaining elements preserve their original order.

**Peek operation**
- Returns the top element without removal, ensuring read-only access.

Therefore, for every valid sequence of `push`, `pop`, and `peek`, the stack’s observable behavior satisfies **LIFO — Last In, First Out** semantics.

---

## 3. Termination
Every operation (`push`, `pop`, `peek`, `is_empty`, `size`) performs a **finite number of steps** and terminates deterministically:

- Each `push` and `pop` performs one constant-time append/remove.
- There are no **recursive calls or loops** dependent on `n`.
Hence, all operations terminate in O(1) time.

---

## 4. Time Complexity
Operation                 | Complexity    | Notes                       |
|-------------------------|---------------|-----------------------------|
| push(x)                 | O(1)          | Append element to top       |
| pop()                   | O(1)          | Remove element from top     |
| peek()                  | O(1)          | Access top element only     |
| is_empty()              | O(1)          | Boolean check               |
| size()                  | O(1)          | Constant-time length lookup |

---

## 5. Space Complexity

| Aspect                  | Complexity     | Explanation                                   |
|-------------------------|----------------|------------------------------------------------
| Auxiliary Space         | O(1)           | No extra buffers needed beyond the stack list |
|Total Space (n elements) | O(n)           | Stores all pushed elements                    |
| In-Place?               | Yes            | All operations occur within the same container|
| Stability               | Not applicable | Stack is not a sorting structure              |

---

## 6. Additional Notes
- The **Stack** is an **abstract data type (ADT)** with a single access point — the **top**.
- Widely used in:
        **Function call management** (call stack).
        **Undo/Redo** systems.
        **Expression evaluation** (postfix, infix).
        **Depth-first search (DFS)** in graphs.

Any violation of the invariant (e.g., popping an empty stack) raises an **exception** to preserve correctness.

---

## 7. 📷 Handwritten Draft (optional)
My initial handwritten proof draft is available here:  
