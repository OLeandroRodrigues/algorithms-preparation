# 🧪 Running Python Tests

This repository has multiple languages (`python/`, `java/`, `csharp/`).  
👉 **All Python tests must be run from inside the `python/` folder.**

---

## ⚙️ Setup

```bash
cd python
python -m venv .venv

# Activate environment
# Linux/Mac:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Run Tests (inside `python/`)

Run all tests:
```bash
pytest
```

Verbose output:
```bash
pytest -v
```

Run a specific folder or file:
```bash
pytest tests/sorting/insertion_sort
pytest tests/sorting/insertion_sort/test_insertion_sort.py
```

---

✨ That’s it! With this setup, you can run and extend the Python test suite.  
