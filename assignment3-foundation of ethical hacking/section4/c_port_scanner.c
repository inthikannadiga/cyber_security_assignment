#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int scan_port(int port) {

    int sock;
    struct sockaddr_in target;

    sock = socket(AF_INET, SOCK_STREAM, 0);

    target.sin_family = AF_INET;
    target.sin_port = htons(port);
    target.sin_addr.s_addr = inet_addr("127.0.0.1");

    int result = connect(sock, (struct sockaddr *)&target, sizeof(target));

    close(sock);

    return result;
}

int main() {

    int ports[] = {22, 80, 443, 3306};
    int n = 4;

    printf("Scanning localhost (127.0.0.1)...\n\n");

    for (int i = 0; i < n; i++) {

        int port = ports[i];

        if (scan_port(port) == 0) {
            printf("Port %d: OPEN\n", port);
        } else {
            printf("Port %d: CLOSED\n", port);
        }
    }

    return 0;
}