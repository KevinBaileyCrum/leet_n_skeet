#include <thread>
#include <mutex>
#include <condition_variable>
#include <iostream>
#include <vector>

class ZeroEvenOdd {
   private:
      int n;
      std::mutex mtx;
      std::condition_variable cv;
      /* std::condition_variable zeroSwitch; */
      int count;
      int zeroSwitch;

   public:
      ZeroEvenOdd(int n) {
         this->n = n;
         count = 1;
         zeroSwitch = 0;
      }

      // printNumber(x) outputs "x", where x is an integer.
      void zero(std::function<void(int)> printNumber) {
         for (int i=0; i<n; ++i) {
            std::unique_lock<std::mutex> lck(mtx);
            cv.wait(lck, [this]{return zeroSwitch % 2 == 0;});
            printNumber(0);
            ++zeroSwitch;
            lck.unlock();
            cv.notify_all();
         }
      }

      void even(std::function<void(int)> printNumber) {
         for (int i=2; i<=n; i+=2) {
            std::unique_lock<std::mutex> lck(mtx);
            cv.wait(lck, [this]{return count % 2 == 0 && zeroSwitch % 2 != 0;});
            printNumber(i);
            ++count;
            ++zeroSwitch;
            lck.unlock();
            cv.notify_all();
         }

      }

      void odd(std::function<void(int)> printNumber) {
         for (int i=1; i<=n; i+=2) {
            std::unique_lock<std::mutex> lck(mtx);
            cv.wait(lck, [this]{return count % 2 != 0 && zeroSwitch % 2 != 0;});
            printNumber(i);
            ++count;
            ++zeroSwitch;
            lck.unlock();
            cv.notify_all();
         }
      }
};

int main() {
   ZeroEvenOdd Z(5);

   std::thread t1(&ZeroEvenOdd::odd,  &Z, [](int x){std::cout << x;});
   std::thread t2(&ZeroEvenOdd::even, &Z, [](int x){std::cout << x;});
   std::thread t3(&ZeroEvenOdd::zero, &Z, [](int x){std::cout << x;});

   t1.join();
   t2.join();
   t3.join();
   std::cout << std::endl;

   ZeroEvenOdd Y(10);

   std::thread t4(&ZeroEvenOdd::odd,  &Y, [](int x){std::cout << x;});
   std::thread t5(&ZeroEvenOdd::even, &Y, [](int x){std::cout << x;});
   std::thread t6(&ZeroEvenOdd::zero, &Y, [](int x){std::cout << x;});

   t4.join();
   t5.join();
   t6.join();
   std::cout << std::endl;


   ZeroEvenOdd X(0);

   std::thread t7(&ZeroEvenOdd::odd,  &X, [](int x){std::cout << x;});
   std::thread t8(&ZeroEvenOdd::even, &X, [](int x){std::cout << x;});
   std::thread t9(&ZeroEvenOdd::zero, &X, [](int x){std::cout << x;});

   t7.join();
   t8.join();
   t9.join();
   std::cout << std::endl;
}
