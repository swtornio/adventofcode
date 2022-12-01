/*

File read heavily lifted from https://solarianprogrammer.com/2019/04/03/c-programming-read-file-lines-fgets-getline-implement-portable-getline/

# Read input file input.txt
# Add up calories for each elf, separated by blank lines
# Store as highest number, if higher than previous
# Submit total for elf with most calories
#
# Part 2 - report total of top 3 elves

*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (void) {
    FILE *fp = fopen("input.txt", "r");
    if (fp== NULL) {
        perror("Unable to open file");
        exit(1);
    }

    // Read lines using POSIX function getline
    // Won't work on windows
    char *line = NULL;
    char *p;
    size_t len = 0;
    long highest = 0;
    long second = 0;
    long third = 0;
    long current = 0;

    while(getline(&line, &len, fp) != -1) {
        if (strlen(line) > 1) {
            current += strtol(line, &p, 10);
        } else {
            if (current > third) {
                if (current > second) {
                    if (current > highest) {
                        third = second;
                        second = highest;
                        highest = current;
                    } else {
                        third = second;
                        second = current;
                    }
                } else {
                    third = current;
                }
            }
            current = 0;
        } 
        // printf("line: %s", line);
        // printf("length: %lu\n", strlen(line));
    }

    printf("Highest load is %lu\n", highest);
    printf("Second load is %lu\n", second);
    printf("Third load is %lu\n", third);

    fclose(fp);
    free(line);
}