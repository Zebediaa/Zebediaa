#include "stdio.h"
#include "math.h"
#include "unif.h"

int main(void) {
  
  double x;
  int i;

  for (i = 0; i < 10; i++) {
    x = unif();
    printf("for %e\n",x);
  }

  return 0;
}
