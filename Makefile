PY = python3

DAA: DAA.py
	$(PY) $< -D 8.8.8.8 -T 127.0.0.1
