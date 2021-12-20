#include <stdio.h>
#include <math.h>
#include "unif.h"

int main(void){
  const int Nsub=15,Nsim=10000;
  int i,j;
  double xni[Nsub],phi[Nsub],fun[Nsub],xmin=0,xmax=2*3.14159,x,dx=((xmax-xmin)/Nsub);
  for(i=0;i<Nsub;i++){phi[i]=0;}
  for(i=0;i<Nsub;i++){
    double p,a = (1-exp(-xmax));
    //
    for(;;){
      x = -log(1-unif()*a);
      p = fabs(sin(x));
      if(unif()<p){break;}
    }
    //
    j = floor((x-xmin)/dx);
    if(j>=0&&j<15){phi[j]+=1;}
  }

  for(j=0;j<Nsub;j++){
    xni[j] = (j+0.5)*dx;
    phi[j] = (phi[j]/(dx*Nsim));
    //
    fun[j] = 1.837737*fabs(sin(xni[j]))*exp(-xni[j]);
    //

    printf("\t%f\t%e\t%e\n",xni[j],phi[j],fun[j]);

  }

}

// 4
