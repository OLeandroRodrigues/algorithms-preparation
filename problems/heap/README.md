# 🧮 Heap Problems

This folder contains **problem-solving exercises related to Heaps and Priority Queues**.  
Each problem is implemented in two complementary styles:

| Version | File suffix | Description |
|----------|--------------|--------------|
| **From Scratch** | `_from_scratch.py` | Implements all necessary heap logic manually (interview-style). |
| **Repo-based** | `_repo_based.py` | Reuses data structures from [`/python/data_structures`](../../python/data_structures) such as `MaxHeap` or `PriorityQueueBuiltin`. |

---

## 📂 Current Problems

| Problem | From Scratch | Repo-based | Description | Time Complexity |
|----------|---------------|-------------|--------------|----------------|
| **Top K Elements** | [`top_k_elements_from_scratch.py`](./top_k_elements_from_scratch.py) | [`top_k_elements_repo_based.py`](./top_k_elements_repo_based.py) | Find the **k largest elements** in an unsorted array using a heap. | O(n log k) |

---

## 🧠 Learning Goals

- Understand how a **heap maintains the heap property** via `heapify_up` and `heapify_down`.
- Implement a **priority queue manually** and analyze its asymptotic behavior.
- Practice **using** a pre-built heap structure for clean, production-like solutions.
- Compare trade-offs between “From Scratch” (control, explicit complexity) and “Repo-based” (modularity, clarity).

---

## ⚙️ How to Run Tests

Each file includes lightweight `pytest` tests at the bottom.  
From the repository root, run:

```bash
cd problems
pytest heap -q