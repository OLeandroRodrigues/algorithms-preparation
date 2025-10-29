# 📝 Randomized QuickSort Proof

## 📚 Metadata
- **Creator / Inventor**: Sir Tony Hoare (base algorithm)
- **Randomization Concept Introduced by**: Robert Sedgewick & other algorithmic researchers during the 1970s–1980s
- **Country of Origin**: United Kingdom
- **Institution (if applicable)**: University of Oxford
- **Year of Creation / Publication**:
    - **Original QuickSort**: 1961 (C.A.R. Hoare, "Algorithm 64: Quicksort", Communications of the ACM)
    - **Randomized Variant Formalized:**: mid–1970s (introduced to ensure O(n log n) expected behavior independent of input order)

## 📝 Description

The **Randomized QuickSort** algorithm is an extension of Tony Hoare’s original QuickSort (1961).
It introduces a random pivot selection step to eliminate dependence on input order,
guaranteeing **expected O(n log n)** performance even on sorted or nearly sorted data.
All other steps — partitioning, recursion, and the divide-and-conquer structure — remain identical to the deterministic version.

Type: Divide-and-conquer
Input: A sequence of n number (a1, a2, ..., an)
Output: A permutation (a'1,a'2, ..., a'n) such that a'1 <= a'2 <= ... <= a'n
In other words, recording an array of numbers in decreasing or increasing way

**Divide** by partitioning (rearranging) the array A[p:r] into two (possibly empty)
subarrays A[p:q-1] (the **low side**) and A[q +1:r] (the **high side**) such
that each element in the low side of the partition is less than or equal to the
**pivot** A[q], which is, in turn, less than or equal to each element in the high side.
Compute the index q of the pivot as part of this partitioning procedure.
**Conquer** by calling quicksort recursively to sort each of the subarrays A[p:q-1]
and A[q+1:r].
**Combine** by doing nothing: because the two subarrays are already sorted, no work
is needed to combine them. All elements in A[p:q-1] are sorted and less than
or equal to A[q], and all elements in A[q+1:r] are sorted and greater than or
equal to the pivot A[q]. The entire subarray A[p:r] cannot help but be sorted!

**RANDOMIZED QUICKSORT**

## 📝 Pseudocode
The initial call is RANDOMIZED-QUICKSORT(A, p, r)
cpp
``` 
RANDOMIZED-QUICKSORT(A, p, r)
1   if p < r
2       // Randomly choose a pivot and partition the array around it
3       q = RANDOMIZED-PARTITION(A, p, r)
4
5       // Recursively sort the two subarrays
6       RANDOMIZED-QUICKSORT(A, p, q - 1)    // sort left side
7       RANDOMIZED-QUICKSORT(A, q + 1, r)    // sort right side

```

**Partitioning the array**
cpp
``` 
PARTITION(A, p, r)
1   x = A[r]                            // the pivot
2   i = p - 1                           // highest index into the low side
3   for j = p to r - 1                  // process each element other than pivot
4       if A[j] <= x                    // does the element belong on the low side?
5           i = i + 1                   // new slot in the low side
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
- [] Handwritten Draft (optional)  

---

## 1. Invariant
1.1. Invariant of PARTITION(A, p, r)

Let x = A[r] be the pivot.
During the loop for j = p to r - 1, the following invariant holds at the start of each iteration (and is preserved after each step):
- (I1) All elements in A[p..i] are <= x.
- (I2) All elements in A[i+1..j-1] are > x.
- (I3) The segment A[j..r-1] has not yet been processed.
- (I4) The pivot remains in A[r].

**Initialization:**
Before the loop, i = p - 1 and j = p, so both subarrays are empty and (I1)–(I4) trivially hold.

**Maintenance:**
If A[j] <= x, increment i and swap A[i] with A[j].
This keeps A[p..i] as elements <= x, and A[i+1..j-1] remains elements > x.
If A[j] > x, nothing changes except j++.

**Termination:**
At the end, swap A[i+1] and A[r].
Now:
- A[p..i] <= A[i+1] = x
- A[i+2..r] > A[i+1] = x
and i + 1 (the pivot’s index) is returned.

---

---

## 2. Correctness
**Proof by induction on subarray size** n = r - p + 1.

- **Base case** (n = 1):
    When p == r, there is only one element — trivially sorted.
-**Inductive step**:
    Assume correctness for all subarrays of size < n.
    In the current call, the algorithm chooses a random pivot, partitions around it, and obtains index q.
    By the PARTITION invariant:
    - A[p..q-1] <= A[q]
    - A[q+1..r] > A[q]
    Thus, the pivot A[q] is in its **final sorted position**.
    The recursive calls
    RANDOMIZED-QUICKSORT(A, p, q-1) and
    RANDOMIZED-QUICKSORT(A, q+1, r)
    sort both subarrays.

    By the induction hypothesis, both subarrays are correctly sorted after the recursive calls.
    Since all elements in the left subarray are ≤ pivot and all elements in the right subarray are ≥ pivot,
    the concatenation of these three segments forms a **fully sorted array** A[p..r].
---

## 3. Termination
Each call executes a finite PARTITION operation (O(n)) and makes **two recursive calls**, each on a **strictly smaller subarray**:
A[p..q-1] and A[q+1..r].

The recursion stops when p >= r, i.e., when the subarray has **zero or one element**.

Thus, the algorithm always terminates after a finite number of recursive steps.

---

## 4. Time Complexity
| Case        | Complexity |
|-------------|------------|
| Best Case   | O (n log n)|
| Average     | O (n log n)|
| Worst Case  | O (n log n)|
| Space       | O (log n)  |

---

## 5. Space Complexity

| Aspect           | Complexity                                       |
|------------------|--------------------------------------------------|
| Auxiliary Space  | O (1)                                            |
| In-Place?        | Yes (partitioning in-place)                      |
| Stability        | Not (default)                                    |

---

## 6. Additional Notes
- The Randomized QuickSort algorithm is a direct improvement of Hoare’s original QuickSort (1961), this small probabilistic modification eliminates the deterministic worst case (O(n²)).
- Despite its randomization, the algorithm remains **in-place** (O(1) extra space) and maintains **expected O(n log n)** time across all possible input distributions.

## 7. When to Use Randomized
Use Randomized QuickSort instead of the standard QuickSort when:
1. The input data may be already sorted or nearly sorted.
2. You cannot control the data distribution or its source.
3. You need stable performance over large datasets.
4. The sorting implementation may run repeatedly on different data patterns.

---

## 7. 📷 Handwritten Draft (optional)
My initial handwritten proof draft is available here:  