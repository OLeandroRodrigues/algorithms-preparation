# 📝 QuickSelect Proof

## 📚 Metadata
- **Creator / Inventor**:  C.A.R. (Tony) Hoare
- **Country of Origin**: England
- **Institution (if applicable)**: University of Oxford
- **Year of Creation / Publication**: 1961 — introduced in the same paper where Hoare presented QuickSort (“Algorithm 64: Quicksort”), published in Communications of the ACM.

## 📝 Description
Type: Divide-and-conquer (Selection Algorithm)
Input: A sequence of n numbers (a₁, a₂, ..., aₙ) and an integer k (1 ≤ k ≤ n)
Output: The element aₖ′ that would occupy the k-th position if the sequence
were sorted (without actually sorting the entire array).

In other words, Quickselect finds the k-th smallest (or largest) element in 
an unsorted array using partition-based selection, **achieving an expected time complexity of O(n)**.

## 📝 Pseudocode
The initial call is QUICKSELECT(A, p, r, k)
cpp
``` 
QUICKSELECT(A, p, r, k)
1  if p <= r
2      // Randomly choose a pivot and partition the array around it
3      q = RANDOMIZED-PARTITION(A, p, r)
4      
5      // Number of elements on the low side including the pivot
6      length = q - p + 1
7      
8      if k == length
9          return A[q]                  // pivot is the k-th smallest element
10     else if k < length
11         return QUICKSELECT(A, p, q - 1, k)      // search on the left side
12     else
13         return QUICKSELECT(A, q + 1, r, k - length) // search on the right side

```

**Partitioning the array**
cpp
``` 
PARTITION(A,p,r)
1   x = A[r]                            // the pivot
2   i = p -1                            // highest index into the low side
3   for j = p to r - 1                  // process each element other than pivot 
4       if A[j] <= x                    // does the element belong on the low side 
5           i = i+1                     // index of a new slot in the low side
6           exchange A[i] with A[j]     // put this element there
7   exchange A[i + 1] with A[r]         // pivot goes just to the right of the low side
8   return i + 1                        // new index of the pivot 
```

**Randomized Partition**
cpp
```
RANDOMIZED-PARTITION(A, p, r)
1   i = RANDOM(p, r)                    // choose random pivot index
2   exchange A[i] with A[r]             // move it to the end
3   return PARTITION(A, p, r) 
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
1.1. Invariant of PARTITION(A, p, r)

Let x = A[r] be the pivot. During the loop for j = p to r - 1, the following invariant holds at the start of each iteration (and is preserved after each step):

- (I1) All elements in A[p..i] are <= x.
- (I2) All elements in A[i+1..j-1] are > x.
- (I3) The segment A[j..r-1] has not yet been processed.
- (I4) The pivot remains in A[r].

---

## 2. Correctness
**Proof by induction on subarray size** n = r - p + 1:

- **Base case** (n = 1):
    When p == r, the function returns A[p], which is trivially the first (and only) smallest element. Correct.
-**Inductive step**:
    Assume correctness for all subarrays of size < n.
    In the current call, partition returns index q.
    By the PARTITION invariant, A[p..q-1] <= A[q] and A[q+1..r] > A[q].
    Hence, the pivot’s rank is length = q - p + 1.

    If k == length, return A[q] — the correct k-th smallest.

    If k < length, recurse on A[p..q-1]. The subproblem size is < n, so by the induction hypothesis, it returns the correct k-th smallest.

    If k > length, recurse on A[q+1..r] with adjusted k' = k - length. Again, the subproblem is smaller and correct by induction.

    Therefore, QUICKSELECT always returns the k-th order statistic.
---

## 3. Termination
Each call performs one finite PARTITION operation and at most **one recursive call** on a strictly smaller subarray 
(A[p..q-1] or A[q+1..r]). The recursion bottoms out when p == r. Thus, the algorithm **terminates**.

---

## 4. Time Complexity
| Case        | Complexity |
|-------------|------------|
| Best Case   |  O(n)      |
| Average     |  O(n)      |
| Worst Case  |  O(n^2)    |
| Space       |  O(1)      |

---

## 5. Space Complexity

| Aspect           | Complexity |
|------------------|------------|
| Auxiliary Space  |   O(1)     |
| In-Place?        |   Yes      |
| Stability        |   No       | 

---

## 6. Additional Notes
QuickSelect = "half QuickSort": same partition logic, but recursion occurs on only one side.

---

## 7. 📷 Handwritten Draft (optional)
My initial handwritten proof draft is available here:  
