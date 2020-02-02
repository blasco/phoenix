// int execve(const char *pathname, char *const argv[],
//           char *const envp[]);

#include <err.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
int main(void) {
  char *ptr = getenv("ExploitEducation");
  int size = strlen(ptr);
  printf("%i\n", size);
  return 1;
}
