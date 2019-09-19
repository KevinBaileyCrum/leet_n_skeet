#import <thread>
#import <iostream>

void printFirst(){
  std::cout<<"first"<<std::endl;
}

void printSecond(){
  std::cout<<"second"<<std::endl;
}

void printThird(){
  std::cout<<"third"<<std::endl;
}

int main(){
  std::thread t1(printFirst);
  std::thread t2(printSecond);
  std::thread t3(printThird);

  t1.join();
  t2.join();
  t3.join();
}
