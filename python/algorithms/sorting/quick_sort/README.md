# 📝 QuickSort Proof

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
The initial call is QUICKSORT(A,1,n)
cpp
``` 
QUICKSORT(A,p,r)
1 if p < r
2    // Partition the subarray around the pivot, which ends up in A[q]
3    q = PARTITION(A,p,r)
4    QUICKSORT(A,p,q-1) // recursively sort the low side
5    QUICKSORT(A,q + 1,r) // recursively sort the high side

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
Focus on PARTITION(A,p,r). Prior to thr first interation of the loop, we have i = p -1 
and j = p. Because no values lie between p and i and no values lie between i + 1 
and j - 1, the first two conditions of the loop invariant are trivially satisfied. The 
assigned in line 1 satisfies the third condition. 

---

## 2. Correctness
Showing what happens when A[j] > x: the only action in the loop is to increment j. After j
has been incremented, the second condition holds for A[j -1] and all other entries remain
unchanged. Now, what happens when A[j] <= x: the loop increments i, swaps A[i] and A[j], 
and then increments j. Because of the swap, we now have than A[i] <= x, and condition 1 is satisfied.
Similary , we also have that A[j-1] > x, since the item that was swapped into A[j - 1] is by the
invariant, greater than x.

---

## 3. Termination
Since the loop makes exactly r - p iterations, it terminates, whereupon j = r. At that point, the 
unexamined subarray A[j:r-1] is empty, and every entry in the array belongs to one of the other 
three sets described by the invariant. Thus, the values in the array have been partitioned into 
three sets: those less than or equal x (the low side), those greater than x (the high side), and 
a singleton set containing x (the pivot).

---

## 4. Time Complexity
| Case        | Complexity |
|-------------|------------|
| Best Case   | O (n log n)|
| Average     | O (n log n)|
| Worst Case  | O (n^2)    |
| Space       | O (log n)  |

---

## 5. Space Complexity

| Aspect           | Complexity                                       |
|------------------|--------------------------------------------------|
| Auxiliary Space  | O (log n) average or O (n) worse case            |
| In-Place?        | Yes (partitioning in-place)                      |
| Stability        | Not (default)                                    |

---

## 6. Additional Notes
In general, when we only need to use memory (RAM) rather than disk storage, using Quicksort is the best choice. 
Languages such as C/C++ and Python use Quicksort or its variants to ensure high processing speed.


---

## 7. 📷 Handwritten Draft (optional)
My initial handwritten proof draft is available here:  
![handwritten draft](./assets/merge_sort_handwritten.png)