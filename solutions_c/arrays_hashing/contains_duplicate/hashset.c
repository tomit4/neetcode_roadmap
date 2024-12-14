#include "hashset.h"
#include "superfasthash.h"
#include <errno.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Create a new hash set
HashSet *createHashSet(int capacity)
{
	HashSet *set = (HashSet *)malloc(sizeof(HashSet));
	if (set == NULL) {
		fprintf(stderr,
			"Error: malloc failed to allocate memory for hash set. "
			"Error: %s\n",
			strerror(errno));
		exit(EXIT_FAILURE);
	}
	set->buckets = (Node **)calloc(capacity, sizeof(Node *));
	if (set->buckets == NULL) {
		fprintf(stderr,
			"Error: calloc failed to allocate memory for hash set "
			"buckets. Error: %s\n",
			strerror(errno));
		free(set);
		exit(EXIT_FAILURE);
	}
	set->capacity = capacity;
	set->size = 0;
	return set;
}

// Insert a value into the hash set
bool insert(HashSet *set, int value)
{
	unsigned int index = SuperFastHash(value, set->capacity);
	Node *current = set->buckets[index];

	// Check if the value already exists
	while (current != NULL) {
		if (current->value == value) {
			return false; // Duplicate found
		}
		current = current->next;
	}

	// Insert the new value
	Node *newNode = (Node *)malloc(sizeof(Node));
	if (newNode == NULL) {
		fprintf(stderr,
			"Error: malloc failed to allocat ememory for a new "
			"node. Error: %s\n",
			strerror(errno));
		exit(EXIT_FAILURE);
	}
	newNode->value = value;
	newNode->next = set->buckets[index];
	set->buckets[index] = newNode;
	set->size++;

	return true;
}

void freeHashSet(HashSet *set)
{
	for (int i = 0; i < set->capacity; i++) {
		Node *current = set->buckets[i];
		while (current != NULL) {
			Node *temp = current;
			current = current->next;
			free(temp);
		}
	}
	free(set->buckets);
	free(set);
}
