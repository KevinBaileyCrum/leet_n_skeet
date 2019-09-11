#include <stdio.h>
#include <math.h>

int reverse(int x)
{
  int isNeg = 0;
  if(x<0)
  {
    isNeg = 1;
    x *= -1;
  }
  int power = (int) log10(x);
  int accum = 0;
  for(int i=0; i<=power; ++i)
  {
    int curr = x % (int)pow(10,i+1); 
    curr = curr / (int)pow(10,i);
    accum += curr*(int)pow(10, power-i);
  }
  return isNeg?accum*=-1:accum;
}

int main()
{
  reverse(1234);
}
