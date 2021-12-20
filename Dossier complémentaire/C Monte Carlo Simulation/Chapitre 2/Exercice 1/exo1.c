#include <stdio.h>
#include <math.h>
#include "unif.h"


int main(void){
  const int Nsub = 15,Nsin = 10000;
  double xmi[Nsub],phi[Nsub],fun[Nsub],xmin=0,xmax=3,dx,x;
  int i,j;

  dx = (xmax-xmin)/Nsub;
  for(j=0;j<Nsub;j++){phi[j]=0;}
  for(i=0;i<Nsin;i++){

    x = -log(1-unif());
    j = floor((x-xmin)/dx);
    if(j>=0&&j<Nsub){phi[j]+=1;}

    // printf("\t%f\n",x);

  }

for (j = 0; j<Nsub ; j++) {
  xmi[j] = ((j+0.5)*dx);
  phi[j] = (phi[j]/(dx*Nsim));

  fun[j] = exp(-xmi[j]);

  printf("\t%f\t%e\t%e\n",xmi[j],phi[j],fun[j]);
  }
}
