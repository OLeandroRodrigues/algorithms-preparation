# 📝 BucketSort Proof

## 📚 Metadata
- **Origin**: Derived from *Counting Sort* and early mechanical card-sorting machines  
- **Inventor**: Harold H. Seward (formal algorithmic description)  
- **Institution**: Harvard University / IBM  
- **Year of Creation / Publication**: 1954  
- **Referenced by**: Donald E. Knuth, *The Art of Computer Programming*, Vol. 3, 1973  

## 📝 Description
Type: Non-comparative / Stable / Digit-based sorting algorithm 
Input: A sequence of `n` numbers `(a₁, a₂, …, aₙ)`, each represented with `d` digits in base `k` (commonly base 10). 
Output: A permutation `(a′₁, a′₂, …, a′ₙ)` such that `a′₁ ≤ a′₂ ≤ … ≤ a′ₙ`.
In other words, it produces the sorted order of the input numbers in increasing (or decreasing) order by processing their digits.

**Idea:**
Radix Sort does **not compare entire elements directly**. Instead, it leverages the **positional (digit-wise) representation** of numbers.  
It sorts the array **digit by digit**, starting from the **least significant digit (LSD)** or **most significant digit (MSD)**, and uses a **stable sorting subroutine** (commonly *Counting Sort*) on each digit to preserve order among equal keys.

**BUCKET-SORT**

## 📝 Pseudocode
cpp
``` 
BUCKET-SORT(A,n)
1 let B[0:n-1] bea new array
2 for i = 0 to n-1
3   make B[i] an empty list
4 for i = 1 to n
5   insert A[i] into list B[[n . A[i]]]
6 for i = 0 to n -1
7   sort list B[i] with insertion sort 
8 concatenate the lists B[0], B[1], ..., B[n -1] together in order 
9 return the concatenated lists

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
At the start of the distribution phase:

1. Each element `A[i]` has been assigned to **exactly one bucket** according to the mapping rule (for example, `index = floor(n * A[i])` when `A[i] ∈ [0,1)`).
2. All elements within each bucket `B[j]` satisfy the interval constraint:
   - For all `x ∈ B[j]` and `y ∈ B[j+1]`, it holds that `x ≤ y`.
3. No elements are duplicated or lost; the union of all buckets equals the original array.

During the concatenation phase:
- Before processing bucket `B[k]`, all previous buckets `B[0..k−1]` are **completely sorted** and contain elements strictly smaller than any element in `B[k]`.
- After merging `B[k]`, the prefix of the final array `A[0..end(B[k])]` is globally sorted.

This invariant guarantees that after all buckets are processed, the concatenation step yields a globally ordered array.

---

## 2. Correctness
The correctness of **Bucket Sort** relies on two fundamental properties:

1. **Distribution correctness:**  
   Each element is placed into its appropriate bucket range according to the mapping function.  
   Thus, for any two elements `x` and `y`:
   - If `bucket(x) < bucket(y)`, then `x < y`.  
   - Hence, no element from a lower-indexed bucket can be greater than an element from a higher-indexed bucket.

2. **Local sorting correctness:**  
   Each bucket is sorted internally by a stable sorting subroutine (such as Insertion Sort).  
   Therefore, within each `B[j]`, the condition  
   `B[j][p] ≤ B[j][q]` holds for all valid indices `p < q`.

By **mathematical induction** over the bucket index:
- **Base case:** Before processing any bucket, the output is trivially empty (sorted).  
- **Inductive step:**  
  Assume the concatenation of buckets `B[0..k−1]` is sorted.  
  Since all elements of `B[k]` are ≥ every element in the previous buckets, appending `B[k]` (after internal sorting) preserves the global ordering.  
- **Conclusion:**  
  After processing all buckets, the concatenation of `B[0..m−1]` yields a globally sorted array.

Therefore, Bucket Sort is **correct**: it produces a permutation of the input that is globally ordered in non-decreasing order.

---

## 3. Termination
Bucket Sort terminates because:

- The **distribution phase** iterates over all `n` elements exactly once, assigning each to a finite number of buckets.
- Each bucket is sorted by a deterministic, finite subroutine (e.g., Insertion Sort), which terminates after a bounded number of operations.
- The **concatenation phase** performs a single linear pass across the buckets.

Hence, the algorithm halts after a total of `O(n)` or `O(n + k)` steps (depending on the implementation), ensuring guaranteed termination.

At the end of the final concatenation:
- All elements from `A` appear exactly once in the output.
- The resulting array is globally sorted in ascending order.

---

## 4. Time Complexity
| Case        | Complexity    | Explanation                                          |
|-------------|---------------|------------------------------------------------------|
| Best Case   | O(n + k) | Elements are uniformly distributed across buckets; each bucket contains few elements, allowing near-linear total time              |
| Average     | O(n + k) | Expected linear behavior for uniformly distributed data within the target range                    |
| Worst Case  | O(n²) | All elements fall into a single bucket, reducing to the complexity of the inner sorting algorithm (typically Insertion Sort)|
| Space       | O(n + k)     | Requires auxiliary storage for buckets             |

When data is uniformly distributed in `[0, 1)` and the number of buckets is proportional to `n`, **Bucket Sort behaves as O(n)**.

---

## 5. Space Complexity

| Aspect           | Complexity                                       |
|------------------|--------------------------------------------------|
| Auxiliary Space  | O(n + k) (Space for all buckets plus the output array)     |
| In-Place?        | No (Requires additional memory for bucket lists)           |
| Stability        | Depends on subroutine (If the inner bucket sort is stable (e.g., Insertion Sort), then the overall algorithm is stable.)      |

---

## 6. Additional Notes
- **Bucket Sort** is a **distribution-based**, **non-comparative**, and often **stable** sorting algorithm.
- It is particularly effective when sorting **real numbers uniformly distributed over a known range**, typically `[0,1)`.
- The choice of **bucket count** and **distribution function** directly affects performance.
- When used with uniformly distributed data, it achieves **linear average time**.  
  However, poor distribution functions or skewed data may degrade performance to **quadratic time**.
- Bucket Sort is conceptually related to **Counting Sort** and **Radix Sort**, both of which exploit structural properties of the data rather than element comparisons.
- Common applications include:
  - Sorting floating-point data,
  - Histogram-based classification,
  - Parallel partitioning stages in graphics and simulations.


---

## 7. 📷 Handwritten Draft (optional)
My initial handwritten proof draft is available here:  
