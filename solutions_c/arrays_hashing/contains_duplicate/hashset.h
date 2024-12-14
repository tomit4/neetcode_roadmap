#ifndef HASHSET_H
#define HASHSET_H

#include <stdbool.h>
#include <stdint.h>

#define INITIAL_CAPACITY 100000 // Initial size of the hash set
#define LOAD_FACTOR 0.75	// Maximum load factor before resizing

// Node structure for handling collisions using chaining
typedef struct Node {
	int value;
	struct Node *next;
} Node;

// Hash set structure
typedef struct HashSet {
	Node **buckets; // Current capacity of the hash set
	int capacity;	// Number of elements in the hash set
	int size;
} HashSet;

uint32_t SuperFastHash(int value, int capacity);
HashSet *createHashSet(int capacity);
bool insert(HashSet *set, int value);
void freeHashSet(HashSet *set);

#endif
