# 🧩 Problems (Python Only)

This folder contains **algorithmic problems** implemented in **two complementary styles**:

---

## 🧱 Naming Convention

Each problem has **two versions**, reflected in the filename:

| Version | File suffix | Purpose |
|----------|--------------|----------|
| 🧩 **From Scratch** | `_from_scratch.py` | Interview-style implementation where all necessary data structures are coded manually, without imports. |
| 🧩 **Repo-based** | `_repo_based.py` | Engineering-style solution reusing the data structures and algorithms implemented in [`/python`](../python). |

**Example (Heap topic):**
```bash
heap/
├── top_k_elements_from_scratch.py # manual heap implementation (interview-style)
├── top_k_elements_repo_based.py # uses PriorityQueue or MaxHeap from the repo
└── README.md
```

## ⚙️ Running Tests

All problem tests are located under:
```bash
python/tests/problems/
```

To run the test for a specific problem, execute from the project root:
```bash
pytest python/tests/problems/heap/test_find_k_pairs_with_smallest_sum_from_scratch.py -v
```

Or to run **all problem tests**:
```bash
pytest python/tests/problems -v
```

