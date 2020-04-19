#include <thread>
#include <mutex>
#include <condition_variable>
#include <iostream>
#include <vector>

class Foo {
   private:
      void printFirst() {
         std::cout << "first";
      }

      void printSecond() {
         std::cout << "second";
      }

      void printThird() {
         std::cout << "third";
      }

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
         // printFirst() outputs "first". Do not change or remove this line.
         /* printFirst(); */
      }

      void second() {
         std::unique_lock<std::mutex> lck(mtx);
         condVar.wait(lck, [this]() { return count == 2;});
         std::cout << "second";
         ++count;
         condVar.notify_all();
         // printSecond() outputs "second". Do not change or remove this line.
         /* printSecond(); */
      }

      void third() {
         std::unique_lock<std::mutex> lck(mtx);
         condVar.wait(lck, [this]() { return count == 3;});
         std::cout << "third";
         ++count;
         condVar.notify_all();
         // printThird() outputs "third". Do not change or remove this line.
         /* printThird(); */
      }
};

int main(){

   /* std::thread t1(printFirst); */
   /* std::thread t2(printSecond); */
   /* std::thread t3(printThird); */

   /* t1.join(); */
   /* t2.join(); */
   /* t3.join(); */

   /* std::vector<int> input1 {1, 2, 3}; */
   /* std::vector<int> input2 {3, 2, 1}; */
   /* std::vector<int> input3 {2, 1, 1}; */

   Foo fool;
   std::thread t1(&Foo::first, &fool);
   std::thread t2(&Foo::second, &fool);
   std::thread t3(&Foo::third, &fool);

   t3.join();
   t2.join();
   t1.join();

}
