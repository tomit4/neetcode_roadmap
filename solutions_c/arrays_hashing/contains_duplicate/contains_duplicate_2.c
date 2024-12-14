#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool containsDuplicate(int *nums, int numsSize);
int compare(const void *a, const void *b);

int compare(const void *a, const void *b) { return ((*(int *)a - *(int *)b)); }

/*
NOTE: Much more naive implementation,
and is slower at O(nlogn) time due to qsort
NOTE: Passes on Leetcode while more involved hash set solution does not (on
MASSIVE input test case)
*/
bool containsDuplicate(int *nums, int numsSize)
{
	qsort(nums, numsSize, sizeof(int), compare);

	for (int i = 1; i < numsSize; i++) {
		if (nums[i] == nums[i - 1]) {
			return true;
		}
	}
	return false;
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

	return 0;
}
