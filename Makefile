PY=python -m py_compile
.PHONY:
    test
test:
    python -m pytest

dev:
    python run.py