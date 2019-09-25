#include <stdio.h>
#include <stdlib.h>

int Atoi(char *str){
  
  char solution[99];
  int i=0;

  int isNeg = 0;
  // trim whitespace
  while(*str && *str == ' '){ 
    str++;
  }
  printf("str now %s\n", str);
  // get sign
  if(*str && *str == '-'){
    isNeg++;
    str++;
  }
  // get numbers until invalid input
  while(*str && *str >= '0' && *str <= '9'){
    solution[i] = *str;
    i++;
    str++;
  }
  // return
  printf("solution is %s\n", solution);
  return 1;
}

int a2i(const char *s)
{
 int sign=1;
 if(*s == '-')
        sign = -1;
 s++;
 int num=0;
 while(*s)
  {
    num=((*s)-'0')+num*10;
    s++;
  }
 return num*sign;
}

int main(){
  printf("%d\n",Atoi("1234"));
  printf("%d\n",Atoi("-1234"));
  printf("%d\n",Atoi("\0"));
  printf("%d\n",Atoi("          1234       "));
  /* printf("%d\n",a2i("1234")); */
}
