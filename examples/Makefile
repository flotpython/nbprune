EXAMPLES = $(shell find . -name "*.py" \
		     | egrep -- 'corrige|howto|teacher')

all: run-files run-output

run-files:
	nbprune $(EXAMPLES)

run-output:
	nbprune -o example0.nb.py example1-corrige.nb.py

sha1:
	shasum example?.nb.py

clean:
	rm -f example?.nb.py

.PHONY: all run-files run-output sha1 clean
