#include <stdio.h>
#include <math.h>
#include "unif.h"

int main(void){
  const int Nsub=15,Nsin=10000;
  double xnin[Nsub],phi[Nsub],fun[Nsub],dx,x,xmin=0,xmax=3;
  int  i,j;
  dx = (xmax-xmin)/Nsub;
  for(i=0;i<Nsub;i++){phi[i]=0;}
  for(i=0;i<Nsin;i++){
    //
    x = -log(1-unif())/3;
    //
    j = floor((x-xmin)/dx);
    if(j>=0&&j<Nsub){phi[j]+=1;}
  }

  for(j=0;j<Nsub;j++){
  xnin[j]=(j+0.5)*dx;
  phi[j]=phi[j]/(dx*Nsin);

  //
  fun[j]=3*exp(-3*xnin[j]);
  //
  printf("\t%f\t%e\t%e\n",xnin[j],phi[j],fun[j]);
  }
}


// 3
