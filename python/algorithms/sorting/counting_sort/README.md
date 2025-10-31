# 📝 Counting Sort Proof

## 📚 Metadata
- **Creator / Inventor**: Harold H. Seward
- **Country of Origin**: United States
- **Institution (if applicable)**: MIT - Massachusetts Institute of Technology
- **Year of Creation / Publication**: 1954 (He implemented Sorting Count and its apllication in the radix sort)

## 📝 Description
Input: A sequence of n number (a1, a2, ..., an) where each element is an integer in the 
range [0,k], for some known k.
Output: A permutation (a'1,a'2, ..., a'n) such that a'1 <= a'2 <= ... <= a'n
In other words, reorder the array of integers in non-decreasing order.

## 📝 Pseudocode
cpp
``` 
COUNTING-SORT(A,n,k)
1  let B[1:n] and C[0:k] be news arrays
2  for i = 0 to k
3    C[i] = 0
4  for j = 1 to n
5    C[A[j]] = C[A[j]] + 1
6  // C[i] now contains the number of elements equal to i 
7  for i = 1 to k 
8    C[i] = C[i] + C[i - 1]
9  // C[i] now contains the number of elements less than or equal i 
10 // Copy A to B, starting from the end of A
11 for j = n downto 1
12   B[C[A[j]]] = A[j]
13   C[A[j]] = C[A[j]] - 1 // to handle duplicate values 


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
While building the count array C (the frequency array), after processing each element of the input array A[0..j], the value C[v] stores exactly how many times the integer v appears in A[0..j].

Later, while converting C into a prefix-sum array, after processing each index i, C[i] holds the number of elements in A that are ≤ i. This means C[i] represents the final position boundary for the value i in the sorted output.

---

## 2. Correctness
Once C is turned into prefix sums, C[x] tells us: "the last index in the output where the value x must appear."

Then, we iterate over the input array from right to left and place each element x = A[j] into its correct position in the output array B using C[x]. After placing, we decrement C[x].

Why this works:

- Every element is placed in a position that is reserved for its value.
- No two different values ever compete for the same slot (because different values use different ranges of indices in B).
- By going from right to left, equal elements keep their original relative order when written to B. This proves Counting Sort is stable.

As a result, after finishing this placement step, B is a non-decreasing ordering of A.

---

## 3. Termination
The algorithm is made of three loops:

1. Initialize C with zeros for all possible values 0..k.
This loop runs k + 1 iterations.

2. Count the occurrences of each value in A.
This loop runs n iterations.

3. Build prefix sums in C.
This loop runs k iterations.

4. Place each element of A into the result array B.
This loop runs n iterations.

All loops have fixed, finite bounds (n or k), so the algorithm always terminates.

---

## 4. Time Complexity
| Case        | Complexity |
|-------------|------------|
| Best Case   | O(n + k)   |
| Average     | O(n + k)   |
| Worst Case  | O(n + k)   |
| Space       | O(n + k)   |

---

## 5. Space Complexity

| Aspect           | Complexity |
|------------------|------------|
| Auxiliary Space  | O(1)       |
| In-Place?        | No         |
| Stability        | Yes        |

---

## 6. Additional Notes
Advantages:
- Linear time when the value range k is not much bigger than the input size n.
- Stable (preserves the relative order of equal elements).
- Does not use comparisons between elements.

Disadvantages:
- Needs extra memory proportional to k, so it can get expensive if the allowed values are very spread out (large k).
- Works naturally only for integer keys in a known, reasonably small range.

---

## 7. 📷 Handwritten Draft (optional)
My initial handwritten proof draft is available here:  

