# 📝 Binary Search Proof
## 📚 Metadata
* **Creator / Inventor:** First formally described by John Mauchly
* **Country of Origin:** United States
* **Institution (if applicable):** Early computer science / ENIAC research
* **Year of Creation / Publication:** 1946–1949
* **Primary Reference:** *The Art of Computer Programming* — Donald E. Knuth, Volume 3
* **Related Concepts:** Sorted Arrays, Divide-and-Conquer, Logarithmic Time, Recursion, Iteration, Decision Procedures
* **Typical Use Cases:** Fast lookup in sorted arrays, decision problems, optimization problems, monotonic predicate search, boundary finding

---

## 📝 Description

**Binary Search** is an efficient algorithm for searching in **sorted arrays**, running in **O(log n)** time.

The algorithm maintains two pointers (`left` and `right`) that define the current search interval.
At each iteration:

* Compute the midpoint `mid`
* Compare the target with `A[mid]`
* Discard half of the search space

Visual intuition:

```
Array:  2   5   9   14   18   21   30
          ←--- search space ---→

mid = 14 → compare and eliminate half
```

---

## 🔍 Operation

Binary Search relies on two core principles:

### **1. Precondition**

The array **must be sorted**.

### **2. Loop Invariants**

At every iteration:

* If the target exists, it **must be between `left` and `right`**.
* The search interval **shrinks monotonically**.
* The midpoint `mid` always lies inside the interval.

---

## 📝 Pseudocode (Iterative Binary Search)

```cpp
BINARY_SEARCH(A, n, target):
1  left = 0
2  right = n - 1
3  
4  while left <= right:
5      mid = left + (right - left) / 2   // safe mid computation
6      
7      if A[mid] == target:
8          return mid
9      else if A[mid] < target:
10         left = mid + 1
11     else:
12         right = mid - 1
13 
14 return -1   // not found
```

---

## 1. Invariant

Throughout execution, the following remain true:

* The target (if it exists) is always within the interval `[left, right]`.
* The interval shrinks strictly at each iteration.
* The array remains sorted throughout the search.
* The midpoint `mid` is always a valid index.

---

## 2. Correctness

Binary Search is correct because:

* It preserves the loop invariant at every step.
* It terminates only when:

  * The target is found, or
  * The interval becomes empty (`left > right`).
* If the interval becomes empty, the invariant guarantees that the target cannot exist in the array.

---

## 3. Termination

The algorithm always terminates because:

* Each iteration reduces the search space by roughly half.
* The interval size is finite.
* Therefore, the number of iterations is at most `⌊log₂ n⌋ + 1`.

---

## 4. Time Complexity

```
Best Case:    O(1)
Worst Case:   O(log n)
Average Case: O(log n)
```

---

## 5. Space Complexity

### Iterative Version

```
O(1)
```

### Recursive Version

```
O(log n)   // recursion depth
```

---

## 6. Additional Notes

* Requires a **sorted array**.
* Forms the basis of classic techniques such as:

  * Lower Bound / Upper Bound
  * Binary Search on Answer
  * Search in monotonic predicates
  * Ternary Search (variant for unimodal functions)
* Extremely common in algorithmic interviews and competitive programming.

---

## 7. Handwritten Draft (optional)

(Insert your handwritten proof attempts, invariants, sketches, or diagrams.)

---

