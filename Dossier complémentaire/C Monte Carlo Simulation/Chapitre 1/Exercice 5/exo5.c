#include "stdio.h"
#include "math.h"
#include "unif.h"
#define N 10000

int main(void) {

  double xmi[N];
  double phi[N];
  double x;
  int i;

  printf("\nValeur de xmi\n");printf(" \n");
  for (i = 0; i < N; i++) {
    xmi[i] = unif();
    phi[i] = xmi[i]/N;

    printf("%f\n",xmi[i]);
    // printf("for %e\n",x);
  }

  printf("\nValeur de phi\n");printf(" \n");
  for (i = 0; i < N; i++) {

    printf("%f\n",phi[i]);
  }
  return 0;
}
