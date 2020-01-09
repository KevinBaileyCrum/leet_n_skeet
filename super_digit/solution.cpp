#include <iostream>
#include <vector>

int superDigit(std::string n, int k){
  if(k>0){
    std::string nNew;
    for(; k>0; --k){
      nNew += n;
    }
    n = nNew;
    /* std::cout << nNew << std::endl; */
  }
  
  if(n.length() == 1){
    return std::stoi(n);
  } else {
    int accum = 0;
    for(auto digit : n){
      /* std::cout << digit << std::endl; */
      accum += std::atoi(&digit);
      /* std::cout << "accum " << accum << std::endl; */
    }
    /* std::cout << accum << std::endl; */
    return superDigit(std::to_string(accum), 0);
  }
}

int main(){
  std::vector<int> results;
  results.push_back(superDigit("9875", 4));
  results.push_back(superDigit("148", 3));
  results.push_back(superDigit("0", 3));
  /* results.push_back(superDigit("9875", 4)); */

  for(auto num : results)
    std::cout << num << std::endl;
}
