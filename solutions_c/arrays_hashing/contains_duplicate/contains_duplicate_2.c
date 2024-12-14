#include <assert.h>
#include <errno.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INITIAL_CAPACITY 16 // Initial size of the hash set
#define LOAD_FACTOR 0.75    // Maximum load factor before resizing

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

// Hash function: simple modulo-based hashing
unsigned int hash(int value, int capacity)
{
	return (unsigned int)(value % capacity);
}

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
	unsigned int index = hash(value, set->capacity);
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

bool containsDuplicate(int *nums, int numsSize)
{
	HashSet *set = createHashSet(INITIAL_CAPACITY);
	for (int i = 0; i < numsSize; i++) {
		if (!insert(set, nums[i])) {
			freeHashSet(set);
			return true; // Duplicate found
		}
	}

	freeHashSet(set);
	return false; // No duplicates
}

int main(void)
{
	int nums1[] = {1, 2, 3, 1};
	int nums2[] = {1, 2, 3, 4};
	int nums3[] = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};

	printf("%s\n", containsDuplicate(nums1, 4) ? "true" : "false");
	assert(containsDuplicate(nums1, 4) == true);
	printf("%s\n", containsDuplicate(nums2, 4) ? "true" : "false");
	assert(containsDuplicate(nums2, 4) == false);
	printf("%s\n", containsDuplicate(nums3, 10) ? "true" : "false");
	assert(containsDuplicate(nums3, 10) == true);

	exit(EXIT_SUCCESS);
}
