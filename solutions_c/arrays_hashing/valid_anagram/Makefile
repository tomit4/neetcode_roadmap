CC=gcc
CFLAGS=-Wall -Wextra -Werror -Wpedantic -std=c2x
BIN_DIR=../../../bin/arrays_hashing
OUTPUT_FILE=$(BIN_DIR)/valid_anagram
INPUT_FILE=./valid_anagram.c

$(OUTPUT_FILE):
	$(CC) $(CFLAGS) -o $(OUTPUT_FILE) $(INPUT_FILE)

execute:
	$(OUTPUT_FILE)
