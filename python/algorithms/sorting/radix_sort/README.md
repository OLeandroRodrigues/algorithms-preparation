# 📝 Radix Sort Proof

## 📚 Metadata
- **Creator / Inventor**: Harold H. Seward 
- **Country of Origin**: United States
- **Institution (if applicable)**: Harvard University / IBM
- **Year of Creation / Publication**: 1954

## 📝 Description
Type: Non-comparative / Stable / Digit-based sorting algorithm
Input: A sequence of n numbers (a₁, a₂, …, aₙ), each represented with d digits in base k (typically base 10).
Output: A permutation (a′₁, a′₂, …, a′ₙ) such that a′₁ ≤ a′₂ ≤ … ≤ a′ₙ.
In other words, it produces the sorted order of the input numbers in increasing (or decreasing) order by processing their digits.

**Idea:**
Rather than comparing elements directly, Radix Sort exploits the positional representation of numbers. It processes the array digit by digit, grouping and ordering the elements according to each digit’s value, using a stable sorting method (commonly Counting Sort ) at each pass.

**RADIX-SORT**

## 📝 Pseudocode
cpp
``` 
RADIX-SORT(A,p,r)
1 for i = 1 to d
2    use a stable sort to sort array A[1:n] on digit i

```

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
Focus on the **digit-by-digit sorting process** of **Radix Sort**.
Before the first iteration (processing the least significant digit), the array A[1:n] is in an **unsorted state**, but the **stable sort invariant** ensures that:
- After each pass p, the subarray A[1:n] is **partially ordered** according to the p least significant digits.
- The **relative order** of elements with identical digit values is preserved (stability invariant).
- Thus, after completing pass d (the number of digits), the array is globally sorted.

This invariant ensures that each iteration progressively refines the ordering by one digit, and stability guarantees that previous ordering decisions are never undone in later passes.

---

## 2. Correctness
At each digit position exp, Radix Sort performs a **stable counting sort** over all elements.
- When processing a digit value v = (A[i] // exp) % base, all elements are distributed into buckets indexed by v.
- The **stability** of the internal sort ensures that if two elements share the same digit v, their **original order is preserved** from prior passes.
- After collecting the elements from the buckets, the array becomes correctly ordered with respect to all digits processed so far.

By **mathematical induction**:
- **Base step:** after the first pass (least significant digit), numbers are sorted by their LSD.
- **Inductive step:** if the array is sorted by the first p digits, the next stable sort by digit p + 1 preserves that order while extending it to one more digit.
- **Conclusion:** after d passes, all d digits have been considered, and the array is globally sorted.

---

## 3. Termination
The algorithm iterates exactly **d times**, where **d** is the number of digits in the largest element.
Since each iteration performs a complete linear pass through the array (using Counting Sort), the process terminates after **d·n** operations.

At the end of the last pass:
- All digits from the least to the most significant have been processed.
- The array A[1:n] is globally sorted in ascending order.
- No further refinement is needed, as the stability invariant guarantees full ordering consistency.

---

## 4. Time Complexity
| Case        | Complexity    | Explanation                                          |
|-------------|---------------|------------------------------------------------------|
| Best Case   | O (d.(n + k)) | Linear passes per digit, stable buckets              |
| Average     | O (d.(n + k)) | Independent of input distribution                    |
| Worst Case  | O (d.(n + k)) | Deterministic upper bound (no recursion or branching)|
| Space       | O (n + k)     | Auxiliary arrays for counting and output             |

🔹 For fixed-width integers (like CPFs, d = 11, k = 10), this behaves as O(n).

---

## 5. Space Complexity

| Aspect           | Complexity                                       |
|------------------|--------------------------------------------------|
| Auxiliary Space  | O(n + k) (output array and counting buckets)     |
| In-Place?        | No (requires auxiliary array per pass)           |
| Stability        | Yes (stable counting ensures correct order)      |

---

## 6. Additional Notes
- **Radix Sort** is a **non-comparative**, **stable**, **digit-based sorting algorithm**.
- It is particularly efficient for large datasets of **fixed-length keys** such as CPFs, ZIP codes, or integer IDs.
- Unlike Quicksort, it does **not use recursion** and avoids branch mispredictions, leading to predictable memory access patterns.
- Its performance becomes superior to comparison-based sorts (like Quicksort or MergeSort) when handling datasets above **10⁵–10⁶ elements** of fixed width.
- In modern architectures, the linear behavior of **O(d·n)** with minimal branching makes Radix Sort an optimal choice for **massive key-based data pipelines** in databases and indexing systems.


---

## 7. 📷 Handwritten Draft (optional)
My initial handwritten proof draft is available here:  
