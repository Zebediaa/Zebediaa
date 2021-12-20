#include "stdio.h"
#include "math.h"

unsigned int iran1=1;
unsigned int iran2=10;

double unif(void) {

  unsigned int a = 69069;
  unsigned int b = 0;
  unsigned int m = pow(2,31);
  unsigned int q = 17;
  unsigned int p = 15;

  iran1 = (iran1*a + b);

  iran2 = iran2^(iran2<<q);
  iran2 = iran2^(iran2>>p);

  return (double) (iran1^iran2)/2./m;
}
