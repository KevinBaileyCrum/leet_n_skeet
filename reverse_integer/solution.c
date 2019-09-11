#include <stdio.h>
#include <math.h>
#include <limits.h>

int reverse(int x)
{
  long n = x;
  int isNeg = 0;
  if (n<0)
  {
    isNeg = 1;
    n *= -1;
  }
  int power = (int) log10(n);
  long accum = 0;
  for (int i=0; i<=power; ++i)
  {
    long curr = n % (int)pow(10,i+1); 
    curr = curr / (int)pow(10,i);
    accum += curr*(int)pow(10, power-i);
  }
  if (accum > INT_MAX){
    return 0;
  }
  if (isNeg) accum*=-1;
  return (int)accum;
}

int main()
{
  printf("%d\n",reverse(6789));
  printf("%u\n",reverse(1534236469));
}
