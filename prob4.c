/*
coded by: rakeeb
coded for: implimenting tranformation method
*/


#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//run: gcc prob4.c -lm
//out: ./a.out

int main()
{
	int numpoints = 10000 , i ; 
	double  rand_no_arr[numpoints], uniform_rand[numpoints],non_uni_rand_no[numpoints] ;
    
    

  for (i = 1; i <= numpoints; i++) 
  {
    rand_no_arr[i] = rand() ; // random no generation
    uniform_rand[i] = rand_no_arr[i]/(double)RAND_MAX;  // normalization(random no between 0 and 1)
    
    if(uniform_rand[i] != 0)
    {
       non_uni_rand_no[i] = -0.5* log((double)uniform_rand[i] );
    }
    else
    {
    	non_uni_rand_no[i] = 0;
    }

    
  }
  // storing data in prob4.txt file
  FILE *data;
  data = fopen("prob4.txt","w");
  for(i = 1;i<= numpoints; i++)
  {
  	fprintf(data, "%f\n",non_uni_rand_no[i] );
  }
  
	return 0;
    
}

