#include <stdio.h>
#include <math.h>
#include "unif.h"

int main(void){
  const int Nsub=3,Nsim=10000;
  int i,j;
  double xni[Nsub],phi[Nsub],fun[Nsub],u;
  for(i=0;i<Nsub;i++){phi[i]=0;}
  for(i=0;i<Nsim;i++){
    //
    u=unif();
    j=0;
    if (u<6./11) {
      j=0;
    }
    else{
      if (u<9./11) {
         j=1;
      }
      else{
        j=2;
      }
    }

    //
    if(j>=0&&j<Nsub){phi[j]+=1;}
  }

  for(j=0;j<Nsub;j++){
    xni[j] = 1+j;
    phi[j] = (phi[j]/(Nsim));
    //
    fun[j] = 6./11/(1+j);
    //

    printf("\t%f\t%e\t%e\n",xni[j],phi[j],fun[j]);

  }

}

// 5
