// Last updated: 4/7/2026, 7:13:23 PM
1#include <stdio.h>
2#include <string.h>
3
4int firstMatchingIndex(char* s) {
5    // why 2 * i < strlen works but not i < strlen(n) / 2
6    for (int i = 0; 2 * i < strlen(s);i++){
7        // you forgot to n-i-1 you only had -i-1 which wouldve technically worked in python but not C
8        if (s[i] == s[strlen(s)-i-1]){
9            return i;
10        }
11    }
12    return -1;
13}