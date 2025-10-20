# 📝 QuickSort Sort Proof

## 📚 Metadata
- **Creator / Inventor**: Sir Tony Hoare 
- **Country of Origin**: Born (British Ceylon now it is Siri Lanka)
- **Institution (if applicable)**: University of Oxford
- **Year of Creation / Publication**: Published in 1961

## 📝 Description
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

**QUICKSORT**
## 📝 Pseudocode
cpp
``` 
QUICKSORT(A,p,r)
if p < r
    // Partition the subarray around the pivot, which ends up in A[q]
    q = PARTITION(A,p,r)
    QUICKSORT(A,p,q-1) // recursively sort the low side
    QUICKSORT(A,q + 1,r) // recursively sort the high side

```

## ✅ Proof Checklist
- [] Invariant  
- [] Correctness  
- [] Termination  
- [] Time Complexity  
- [] Space Complexity  
- [] Additional Notes  
- [] Handwritten Draft (optional)  

---

## 1. Invariant


---

## 2. Correctness


---

## 3. Termination


---

## 4. Time Complexity
| Case        | Complexity |
|-------------|------------|
| Best Case   |            |
| Average     |            |
| Worst Case  |            |
| Space       |            |

---

## 5. Space Complexity

| Aspect           | Complexity |
|------------------|------------|
| Auxiliary Space  |            |
| In-Place?        |            |
| Stability        |            |

---

## 6. Additional Notes


---

## 7. 📷 Handwritten Draft (optional)
My initial handwritten proof draft is available here:  
![handwritten draft](./assets/merge_sort_handwritten.png)