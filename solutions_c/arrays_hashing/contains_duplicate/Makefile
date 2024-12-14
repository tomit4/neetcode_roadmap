CC=gcc
CFLAGS=-Wall -Wextra -Werror -Wpedantic -std=c99
INPUT_FILE=./contains_duplicate_2.c
OUTPUT_FILE=../../../bin/arrays_hashing/contains_duplicate

contains_duplicate:
	$(CC) $(CFLAGS) -o  $(OUTPUT_FILE) $(INPUT_FILE)

execute:
	$(OUTPUT_FILE)

grind:
	valgrind --leak-check=full -s $(OUTPUT_FILE)
