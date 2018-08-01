/**
Description : Project Euler Problem 3 - What is the largest prime factor of the number 600851475143
Author : Lalit D. Chandwani
Version : 1.0 , 27 June 2018
Last Modified : 27 June 2018
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
  clock_t begin = clock();
  //Declarations
  long number = 600851475143;
  long largestFactor = 0;

  int counter = 2;
  //Loop for getting the factors, using concept of square root.
  while(counter * counter <= number){
    //If divisible, then largest factor should be updated and number should be divided.
    if(number % counter == 0){
      number = number / counter;
      largestFactor = counter;
    }
    else{
      counter = counter + 1;
    }
  }
  if(number > largestFactor){//The remaining number will be a prime and can be used to divide the main number.
    largestFactor = number;
  }
  //printf("%d\n", number);
  printf("Largest Factor: %d\n", largestFactor);
  clock_t end = clock();
  double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
  printf("Time taken: %lf Seconds\n", time_spent);
  return EXIT_SUCCESS;
}
