#include <stdio.h>
#include <math.h>
unsigned int k = 11531;

double unif1(){

  unsigned int a=69069,b=0,m=pow(2,31);
  k = (a*k+b);
  return (double) k/2./m;
}

int main(void) {
  int i;
  double x;
  for(i=0;i<10;i++)
  {
    x=unif1();
    printf("pour le %i nous avons %f \n",i,x);
  }

}
