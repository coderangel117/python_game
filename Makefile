main:
	python3 main.py
clean:
	rm -f *.json

tests=python -m unittest -v -b

ALLMODULES=$(patsubst %.py, %.py, $(wildcard test_*.py))
all:
	${tests} ${ALLMODULES}

% : test_%.py
	${RUNTEST} test_$@