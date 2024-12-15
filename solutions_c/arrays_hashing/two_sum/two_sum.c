#include <assert.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int key;
	int value;
} HashTable;

int hash(int key, int size);
void add_to_hash_table(HashTable *table, int size, int key, int value);
int *twoSum(int *nums, int numsSize, int target, int *returnSize);

int main(void)
{
	int nums1[] = {2, 7, 11, 15};
	int target1 = 9;
	int returnSize1;
	int *result1 = twoSum(nums1, 4, target1, &returnSize1);
	printf("[%d, %d]\n", result1[0], result1[1]);
	assert((result1[0] == 0 && result1[1] == 1) ||
	       (result1[0] == 1 && result1[1] == 0));
	free(result1);
	int nums2[] = {3, 2, 4};
	int target2 = 6;
	int returnSize2;
	int *result2 = twoSum(nums2, 3, target2, &returnSize2);
	printf("[%d, %d]\n", result2[0], result2[1]);
	assert((result2[0] == 1 && result2[1] == 2) ||
	       (result2[0] == 2 && result2[1] == 1));
	free(result2);

	int nums3[] = {3, 3};
	int target3 = 6;
	int returnSize3;
	int *result3 = twoSum(nums3, 2, target3, &returnSize3);
	printf("[%d, %d]\n", result3[0], result3[1]);
	assert((result3[0] == 0 && result3[1] == 1) ||
	       (result3[0] == 1 && result3[1] == 0));
	free(result3);

	int nums4[] = {-10, -1, -18, -19};
	int target4 = -19;
	int returnSize4;
	int *result4 = twoSum(nums4, 4, target4, &returnSize4);
	printf("[%d, %d]\n", result4[0], result4[1]);
	assert((result4[0] == 1 && result4[1] == 2) ||
	       (result4[0] == 2 && result4[1] == 1));
	free(result4);

	exit(EXIT_SUCCESS);
}

int hash(int key, int size) { return (key % size + size) % size; }

void add_to_hash_table(HashTable *table, int size, int key, int value)
{
	int index = hash(key, size);
	while (table[index].key != INT_MIN) {
		index = (index + 1) % size;
	}
	table[index].key = key;
	table[index].value = value;
}

int find_in_hash_table(HashTable *table, int size, int key)
{
	int index = hash(key, size);
	while (table[index].key != INT_MIN) {
		if (table[index].key == key) {
			return table[index].value;
		}
		index = (index + 1) % size;
	}
	return INT_MIN;
}

int *twoSum(int *nums, int numsSize, int target, int *returnSize)
{
	int hash_table_size = numsSize * 2;
	HashTable *hash_table = malloc(sizeof(HashTable) * hash_table_size);
	if (hash_table == NULL) {
		fprintf(stderr,
			"Error: Memory allocation for hash table failed.\n");
		exit(EXIT_FAILURE);
	}
	for (int i = 0; i < hash_table_size; i++) {
		hash_table[i].key = INT_MIN;
	}

	for (int i = 0; i < numsSize; i++) {
		int diff = target - nums[i];
		int found_index =
		    find_in_hash_table(hash_table, hash_table_size, diff);
		if (found_index != INT_MIN) {
			int *result = malloc(2 * sizeof(int));
			if (result == NULL) {
				fprintf(stderr, "Error: Memory allocation for "
						"result array failed.\n");
				exit(EXIT_FAILURE);
			}
			result[0] = found_index;
			result[1] = i;
			*returnSize = 2;
			free(hash_table);
			return result;
		}
		add_to_hash_table(hash_table, hash_table_size, nums[i], i);
	}
	*returnSize = 0;
	free(hash_table);
	return NULL;
}
