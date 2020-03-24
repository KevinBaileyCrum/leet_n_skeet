/* Given an array of characters, compress it in-place. */
/* The length after compression must always be smaller than or equal to the original array. */
/* Every element of the array should be a character (not int) of length 1. */
/* After you are done modifying the input array in-place, return the new length of the array. */

/* All characters have an ASCII value in [35, 126]. */
/* 1 <= len(chars) <= 1000 */

#include <iostream>
#include <vector>

/* compress in place and return length of array */
int compress(std::vector<char> &chars){
   char pre = chars[0];
   int cCount = 0;
   int cIndex = 0;
      std::cout << chars.back();
   for (char i=0; i<chars.size(); ++i){
      if (chars[i] != pre || i == chars.back()){
			if (cCount > 0){
				chars[cIndex + 1] = cCount + '0';
            std::cout << cCount + '0' << std::endl;
			}
         pre = chars[i];
         cIndex = i;
         cCount = 0;
      } else {
         ++cCount;
      }
   }
   for (auto c : chars){
      std::cout << c << ' ';
   }
   return chars.size();
}

int main(){
   std::vector<std::vector<char> > charList  {
      {'a','a','b','b','c','c','c'},
      /* {'a'}, */
      /* {'a','b','b','b','b','b','b','b','b','b','b','b','b'}, */
      /* {} */
   };

   for (auto &vec : charList){
      compress(vec);
   }
   
	std::cout << std::endl;
}
