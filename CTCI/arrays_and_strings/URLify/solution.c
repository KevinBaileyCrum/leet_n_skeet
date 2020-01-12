// replace spaces in string (in place) with '%20'
// assume enough space in string to do replacement
// len of original string is passed however enough room is allotted

#include <stdio.h>

void URLify(char* str, int strSize){
  int spaceCount = 0;
  for(int i=0; i<strSize; i++)
    if(str[i] == ' ') spaceCount++;
  for(int i=strSize-1; i>=0; i--){
    if(str[i] != ' ')
      str[i+(2*spaceCount)] = str[i];
    else {
      int shift = i+(2*spaceCount);
      // is there a cleaner C way of inserting multichar constants
      str[shift-2]   = '%';
      str[shift-1] = '2';
      str[shift] = '0';
      spaceCount--;
    }
  }
}

int main(){
  //          0123456789ABCDEF\0
  char a[] = "Mr John Smith    ";
  char b[] = "Mr John Smith BP O  D            ";

  URLify(a, 13);
  URLify(b, 21);

  printf("%s\n%s\n", a, b);
}
