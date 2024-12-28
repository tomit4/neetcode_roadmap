#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define RED "\x1b[31m"
#define GREEN "\x1b[32m"
#define YELLOW "\x1b[33m"
#define BLUE "\x1b[34m"
#define MAGENTA "\x1b[35m"
#define CYAN "\x1b[36m"
#define BOLD "\x1b[1m"
#define RESET "\x1b[0m"

void randomize(void);
int gen_random(int max);
bool is_yes_or_no(char yes_or_no);

struct exercise {
	char exercise[60];
	int total_successes;
	int max_tries;
};

void print_total_score(int num_of_exercises, struct exercise exercises[]);

int main(void)
{
	int i, j, k;
	int num_of_exercises, num_of_tries;
	int num_completed = 0;
	bool exercises_completed = false;
	char yes_or_no;

	randomize();

	printf(BLUE BOLD "How Many Exercises Would You Like To Do? " RESET);
	scanf("%d", &num_of_exercises);

	struct exercise exercises[num_of_exercises];

	for (i = 0; i < num_of_exercises; i++) {
		printf(BLUE BOLD "Please enter exercise #%d: " RESET, i + 1);
		scanf("%59s", exercises[i].exercise);
	}

	printf(BLUE BOLD
	       "How Many Tries per exercise would you like to try? " RESET);
	scanf("%d", &num_of_tries);

	for (j = 0; j < num_of_exercises; j++) {
		exercises[j].total_successes = 0;
		exercises[j].max_tries = num_of_tries;
	}

	while (!exercises_completed) {
		k = gen_random(num_of_exercises) - 1;
		if (exercises[k].total_successes == num_of_tries) {
			continue;
		} else {
			print_total_score(num_of_exercises, exercises);
		}

		printf(GREEN BOLD "Please implement %s\n" RESET,
		       exercises[k].exercise);
		printf(GREEN BOLD
		       "Did you implement %s correctly? (y/n) " RESET,
		       exercises[k].exercise);
		do {
			yes_or_no = getchar();
		} while (isspace(yes_or_no));

		while (!is_yes_or_no(yes_or_no)) {
			printf(RED BOLD
			       "ﴫ error: please enter either 'y' or 'n' "
			       "ﴫ\n" RESET);
			printf(GREEN BOLD
			       "Did you implement %s correctly? (y/n) " RESET,
			       exercises[k].exercise);
			do {
				yes_or_no = getchar();
			} while (isspace(yes_or_no));
		}

		if (yes_or_no == 'y') {
			exercises[k].total_successes += 1;
			if (exercises[k].total_successes == num_of_tries) {
				num_completed++;
			}
			if (num_completed == num_of_exercises) {
				exercises_completed = true;
			}
		} else {
			exercises[k].total_successes = 0;
		}
	}

	printf(MAGENTA BOLD
	       "\n All exercises completed successfully! Good job! "
	       "\n" RESET);
	print_total_score(num_of_exercises, exercises);

	exit(EXIT_SUCCESS);
}

void randomize(void) { srand((unsigned)time(NULL)); }
int gen_random(int max) { return (rand() % max) + 1; }
bool is_yes_or_no(char yes_or_no)
{
	return (yes_or_no == 'y' || yes_or_no == 'n');
}

void print_total_score(int num_of_exercises, struct exercise exercises[])
{
	int i;
	printf(YELLOW BOLD "\nTotal Score:\n" RESET);
	for (i = 0; i < num_of_exercises; i++) {
		printf("%s: (%d/%d)\n", exercises[i].exercise,
		       exercises[i].total_successes, exercises[i].max_tries);
	}
	printf("\n");
}
