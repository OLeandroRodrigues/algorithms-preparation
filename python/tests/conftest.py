import sys
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent       # .../python/tests
PY_DIR     = TESTS_DIR.parent                     # .../python
REPO_ROOT  = PY_DIR.parent                        # .../ (root)

sys.path.append(str(REPO_ROOT))  # to import 'problems' from root
sys.path.append(str(PY_DIR))     # to import 'algorithms', 'data_structures' from python/