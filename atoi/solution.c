#include <stdio.h>
#define  int_max 2147483647
#define  int_min -2147483648

int Atoi(char *str){
  long number = 0;
  int sign = 1;
  // trim whitespace
  while(*str && *str == ' '){ 
    str++;
  }
  // get sign
  if(*str && (*str == '-' || *str == '+')){
    if(*str == '-') sign = -1;
    str++;
  }
  // get numbers until invalid input
  while(*str && *str >= '0' && *str <= '9'){
    if(sign*number > int_max) return int_max;
    if(sign*number < int_min) return int_min;
    number = (*str-'0') + (number*10); // subtract 48
    str++;
  }
  // return
  number *=sign;
  if(number>int_max) return int_max;
  if(number<int_min) return int_min;
  return (int)number; 
}

int main(){
  printf("%d\n",Atoi(" these are words 1234"));
  printf("%d\n",Atoi("-1234 these are words"));
  printf("%d\n",Atoi("\0"));
  printf("%d\n",Atoi("          1234       "));
  printf("%d\n",Atoi("12"));
  printf("%d\n",Atoi("2147483647"));
  printf("%d\n",Atoi("-2147483648"));
  printf("%d\n",Atoi("2147483648"));  // ret int max
  printf("%d\n",Atoi("-2147483649")); // ret int min
  printf("%d\n",Atoi("999999999990000")); // ret int max
  printf("%d\n",Atoi("12"));
  /* printf("%d\n",a2i("1234")); */
}
