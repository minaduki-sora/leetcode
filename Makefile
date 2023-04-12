CC = g++
CFLAGS = -I. -g

test: test.cpp
	$(CC) test.cpp -o test $(CFLAGS)

all: test

.PHONY: clean

clean:
	rm test
	