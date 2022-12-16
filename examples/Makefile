EXAMPLES1 = $(shell ls .teacher/*)
EXAMPLES2 = $(shell ls ../*/.teacher/*)


all: run-files run-output check-jupyter

run-files: run-files1 run-files2

run-files1:
	nbprune -v $(EXAMPLES1) || :

run-files2:
	nbprune -v $(EXAMPLES2) || :

check-jupyter:
	nbprune -jv $(EXAMPLES1) || :

run-output:
	nbprune -o myoutput1.nb.py .teacher/example1-corrige.nb.py

sha1:
	shasum example[0-9]?nb.{py,md}

clean:
	rm -f example[0-9]?nb.{py,md} myoutput*

.PHONY: all run-files run-output sha1 clean
