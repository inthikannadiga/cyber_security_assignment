#include <stdio.h>
#include <string.h>

int main() {

    char buffer[16];   // small buffer of size 16

    printf("Enter some text: ");
    scanf("%s", buffer);   // taking input

    // copying using unsafe function
    char copy[16];
    strcpy(copy, buffer);

    printf("You entered: %s\n", copy);

    return 0;
}

/*
1. What happens with long input?
If the user enters more than 16 characters, it overflows the buffer and starts overwriting nearby memory.

2. Why is this dangerous?
It can crash the program or even allow attackers to execute malicious code by overwriting important memory.

3. How would you fix it?
Use safer functions like strncpy() or fgets() which limit the number of characters copied.
*/