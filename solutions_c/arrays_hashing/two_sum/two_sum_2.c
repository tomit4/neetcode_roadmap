#include <assert.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <uthash.h>

struct hashTable {
	int key;
	int value;
	UT_hash_handle hh;
};

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

int *twoSum(int *nums, int numsSize, int target, int *returnSize)
{
	struct hashTable *hashTable = NULL, *item, *tmpItem;

	for (int i = 0; i < numsSize; i++) {
		HASH_FIND_INT(hashTable, &nums[i], item);
		if (item) {
			int *result = malloc(sizeof(int) * 2);
			result[0] = item->value;
			result[1] = i;
			*returnSize = 2;
			HASH_ITER(hh, hashTable, item, tmpItem)
			{
				HASH_DEL(hashTable, item);
				free(item);
			}
			return result;
		}
		item = malloc(sizeof(struct hashTable));
		item->key = target - nums[i];
		item->value = i;
		HASH_ADD_INT(hashTable, key, item);
	}
	HASH_ITER(hh, hashTable, item, tmpItem)
	{
		HASH_DEL(hashTable, item);
		free(item);
	}
	*returnSize = 0;
	return NULL;
}
