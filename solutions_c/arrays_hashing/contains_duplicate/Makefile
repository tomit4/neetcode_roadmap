CC=gcc
CFLAGS=-Wall -Wextra -Werror -Wpedantic -std=c2x
OBJ_DIR=./build
BIN_DIR=../../../bin/arrays_hashing
OUTPUT_FILE=$(BIN_DIR)/contains_duplicate

SOURCES=contains_duplicate.c hashset.c superfasthash.c
OBJECTS=$(patsubst %.c,$(OBJ_DIR)/%.o,$(SOURCES))

all: $(OUTPUT_FILE)

$(OUTPUT_FILE): $(OBJECTS) | $(BIN_DIR)
	$(CC) $(CFLAGS) -o $@ $^

$(OBJ_DIR)/%.o: %.c | $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJ_DIR):
	mkdir -p $(OBJ_DIR)

$(BIN_DIR):
	mkdir -p $(BIN_DIR)

clean:
	rm -r $(OBJ_DIR) $(OUTPUT_FILE)

execute:
	$(OUTPUT_FILE)

grind:
	valgrind --leak-check=full -s $(OUTPUT_FILE)
