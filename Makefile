CC = g++
CFLAGS = -I. -g

test: 
	$(CC) test.cpp -o test $(CFLAGS)

all: test

.PHONY: clean

clean:
	rm test
	