PY = python3

all: DAA
DAA: DAA.py
	sudo $(PY) $< -D 8.8.8.8 -T 127.0.0.1

sniffer: sniffer.py
	sudo $(PY) $<
