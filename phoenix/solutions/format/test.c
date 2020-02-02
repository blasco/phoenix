#include <stdio.h>

int main(int argc, char **argv) {
    char buffer[16] = "hi %d";
    printf("size of buf: %lu", sizeof(buffer));
    char dest[32];
    sprintf(dest, buffer);
    printf("\n");
    printf("%s", dest);
    printf("\n");
    printf("%s", buffer);
}
