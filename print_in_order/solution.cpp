#include <thread>
#include <mutex>
#include <condition_variable>
#include <iostream>
#include <vector>

class Foo {
      public:
         int count;
         std::mutex mtx;
         std::condition_variable condVar;
      Foo() {
         count = 1;
      }

      void first() {
         std::unique_lock<std::mutex> lck(mtx);
         std::cout << "first";
         ++count;
         condVar.notify_all();
      }

      void second() {
         std::unique_lock<std::mutex> lck(mtx);
         condVar.wait(lck, [this]() { return count == 2;});
         std::cout << "second";
         ++count;
         condVar.notify_all();
      }

      void third() {
         std::unique_lock<std::mutex> lck(mtx);
         condVar.wait(lck, [this]() { return count == 3;});
         std::cout << "third";
         ++count;
         condVar.notify_all();
      }
};

int main(){
   Foo fool;
   std::thread t1(&Foo::first, &fool);
   std::thread t2(&Foo::second, &fool);
   std::thread t3(&Foo::third, &fool);

   t3.join();
   t2.join();
   t1.join();
}
