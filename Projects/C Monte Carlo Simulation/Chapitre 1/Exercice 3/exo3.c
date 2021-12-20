#include "stdio.h"
#include "math.h"

unsigned int iran1 = 1;
unsigned int iran2 = 10;
unsigned int m = pow(2,31) ;

int unif1(){

  unsigned int a=69069;
  unsigned int b=0;


  iran1 = (a*iran1 + b);
  return (double) iran1;
}

int unif2(){
  unsigned int q = 15 ;
  unsigned int p = 17 ;
  iran2 = iran2^(iran2<<q);
  iran2 = iran2^(iran2>>p);

  return (double) iran2;

}

int main(){

  double x;
  unsigned int i;

  for (i = 0; i < 10; i++) {
    x = (unif1()^unif2())/2./m;
    printf("%e\n",x);
  }
}
