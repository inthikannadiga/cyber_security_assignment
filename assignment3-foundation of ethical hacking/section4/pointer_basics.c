#include <stdio.h>

int main() {

    int port = 80;          // normal integer variable
    int *ptr = &port;       // pointer storing address of port

    // printing using variable
    printf("Port value (using variable): %d\n", port);

    // printing using pointer
    printf("Port value (using pointer): %d\n", *ptr);

    // changing value using pointer
    *ptr = 443;

    // printing new value
    printf("Updated port value: %d\n", port);

    return 0;
}