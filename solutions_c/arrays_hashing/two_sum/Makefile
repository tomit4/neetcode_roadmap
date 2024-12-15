CC=gcc
CFLAGS=-Wall -Wextra -Werror -Wpedantic -std=c2x
BIN_DIR=../../../bin/arrays_hashing
OUTPUT_FILE=$(BIN_DIR)/two_sum
INPUT_FILE=./two_sum_2.c

$(OUTPUT_FILE):
	$(CC) $(CFLAGS) -o $(OUTPUT_FILE) $(INPUT_FILE)

execute:
	$(OUTPUT_FILE)

grind:
	valgrind --leak-check=full -s $(OUTPUT_FILE)
