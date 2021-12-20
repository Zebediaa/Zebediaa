#include <stdio.h>
#include <math.h>

unsigned int iran1=12589,iran2=84255,m=pow(2,31);

double unif(){

  int a=69069,b=0,q=15,p=17;
  iran1 = (iran1*a +b);
  iran2 = iran2^(iran2<<q);
  iran2 = iran2^(iran2>>p);

  return (double) (iran1^iran2)/2./m;
}
