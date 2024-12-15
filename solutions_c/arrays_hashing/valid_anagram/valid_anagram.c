#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

bool isAnagram(char *s, char *t);

int main(void)
{
	printf("%s\n", isAnagram("anagram", "nagaram") ? "true" : "false");
	assert(isAnagram("anagram", "nagaram") == true);
	printf("%s\n", isAnagram("nagaram", "anagramm") ? "true" : "false");
	assert(isAnagram("nagaram", "anagramm") == false);
	printf("%s\n", isAnagram("rat", "car") ? "true" : "false");
	assert(isAnagram("rat", "car") == false);
	printf("%s\n", isAnagram("a", "ab") ? "true" : "false");
	assert(isAnagram("a", "ab") == false);
	printf("%s\n", isAnagram("ab", "a") ? "true" : "false");
	assert(isAnagram("ab", "a") == false);
	return 0;
}

bool isAnagram(char *s, char *t)
{
	if (strlen(s) != strlen(t)) {
		return false;
	}

	int count[26] = {0};

	for (int i = 0; s[i] != '\0'; i++) {
		count[s[i] - 'a']++;
		count[t[i] - 'a']--;
	}

	for (int i = 0; i < 26; i++) {
		if (count[i] != 0) {
			return false;
		}
	}
	return true;
}
