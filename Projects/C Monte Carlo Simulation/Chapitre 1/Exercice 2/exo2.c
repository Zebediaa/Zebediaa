#include <stdio.h>
#include <math.h>

unsigned int iran1 = 12;

double unif2(){

  unsigned int q=15;
  unsigned int p=17;
  unsigned int m=pow(2,31);
  iran1 = iran1^(iran1<<q);
  iran1 = iran1^(iran1>>p);

  return (double) iran1/2./m;
}


int main(void){

  double x;
  int i;
  for (i= 0; i < 10; i++) {
    x = unif2(); printf("x = %f\n",x);
  }
}
