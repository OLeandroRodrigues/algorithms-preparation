# 🧮 Algorithms Preparation (Python · Java · C#)

[![CI](https://github.com/OLeandroRodrigues/algorithms-preparation/actions/workflows/ci.yml/badge.svg)](https://github.com/OLeandroRodrigues/algorithms-preparation/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Java](https://img.shields.io/badge/Java-11-orange.svg)](https://www.oracle.com/java/)
[![C#](https://img.shields.io/badge/C%23-.NET%207-blueviolet.svg)](https://dotnet.microsoft.com/)

This repository contains my **data structures and algorithms practice**,  
with a focus on **Big Tech interviews** and **formal proofs of correctness and complexity**.

---

## 📌 Languages

- **Python** → chosen for its **clarity and conciseness**, ideal for interviews.  
- **Java**   → a **compiled, strongly typed language**, aligned with my **OCP Java SE 11 certification preparation**.  
- **C#**     → a **compiled language**, leveraging **13+ years of enterprise experience**.  

---

## 📂 Structure

- `python/`    → Python implementations (algorithms, data structures, problems, tests)
- `java/`      → Java implementations (same structure as above)
- `csharp/`    → C# implementations (same structure as above)
- `templates/` → Reusable README templates (algorithm_readme.md, ds_readme.md, problem_readme.md)

---

## 🧪 Tests

- **Python**  → [Python tests](./python/tests/)  
- **Java**    → [Java tests](./java/tests/)  
- **C#**      → [C# tests](./csharp/tests/)  

Each implementation has unit tests covering correctness and edge cases.  

---

## 🐳 Running with Docker

Build the image and run **all tests (Python + Java + C#)** in one step:

```bash
docker build -t algorithms-prep .
docker run --rm -it algorithms-prep
```

This image automatically:
- Uses a dedicated Python virtualenv at `/opt/venv` (PEP 668 safe).  
- Provides a `python` symlink for cross-platform compatibility (`python` → `python3`).  
- Runs tests for **Python, Java, and C#** in sequence via [`run_all_tests.sh`](./run_all_tests.sh).

---

## 💻 Running Locally (without Docker)

You can also run tests directly on your machine:

### Windows (PowerShell)

Run the PowerShell script for the language you want to test:

```powershell
# Java
cd java
.\run_tests.ps1

# C#
cd csharp
.\run_tests.ps1

```

### Linux / macOS (bash)

Run the shell script for the language you want to test:

```bash
# Java
cd java
./run_tests.sh

# C#
cd csharp
./run_tests.sh

# Python
cd python
./run_tests.sh
```

---

## 🚀 Roadmap

- [ ] Search (all languages)  
- [x] Sorting (all languages)  
- [ ] Dynamic Programming (all languages)
- [ ] Graphs (all languages)
- [ ] Trees (all languages)
- [ ] Greedy (all languages)
- [ ] Backtracking (all languages)
- [ ] Patterns (all languages)

---

## 🎯 Purpose

This repository is more than just coding solutions:  

- Practice of **core CS fundamentals** (search, sorting, trees, graphs, DP, greedy, backtracking).  
- Each algorithm/data structure folder includes its **theoretical background**: proof of correctness, termination arguments, and complexity analysis.  
- Demonstration of versatility across **concise scripting (Python)** and **compiled OOP languages (Java & C#)**.  
- Highlights both the **engineering perspective** (clean, production-ready code, unit tests) and the **theoretical perspective** (formal reasoning, invariants, and handwritten drafts).  

---

📷 Each algorithm may include **visuals** such as diagrams, step-by-step traces, or scanned handwritten notes.  
These are stored in the algorithm’s own `assets/` folder and referenced inside its local `README.md`.

--- 

## ⚙️ Continuous Integration

All tests are executed automatically via **GitHub Actions**.
See workflow file: [`.github/workflows/ci.yml`](.github/workflows/ci.yml).

---