#include <thread>
#include <mutex>
#include <condition_variable>
#include <iostream>
#include <vector>

// make global to allow for copy ctor() when pushing back into the vector
/* std::mutex mtx; */                    
/* std::condition_variable condVar; */ 

class FooBar {
   private:
      /* int n; */
      int flip; // condition variable used for foo vs bar state:
                // zero is foo and 1 is bar
      std::mutex mtx;
      std::condition_variable condVar; 
   public:
      int n;
      FooBar(int n) {
         this->n = n;
         flip = 0;
      }

      /* void foo(function<void()> printFoo) { */
      void foo() {

         for (int i = 0; i < n; i++) {
            std::unique_lock<std::mutex> lck(mtx); // aquire lock for condVar
            condVar.wait(lck, [this]{return flip==0;});  // on wait, realease lock until condition
            // printFoo() outputs "foo". Do not change or remove this line.
            /* printFoo(); */
            std::cout << "foo";
            ++flip;
            lck.unlock();                          // unlock before notifying to avoid waking up thread only to block again
            condVar.notify_one();
         }
      }

      /* void bar(function<void()> printBar) { */
      void bar() {

         for (int i = 0; i < n; i++) {
            std::unique_lock<std::mutex> lck(mtx); // acquires lock, notice lock is scoped but mtx is not
            condVar.wait(lck, [this]{return flip==1;});
            // printBar() outputs "bar". Do not change or remove this line.
            /* printBar(); */
            std::cout << "bar";
            --flip;
            lck.unlock();
            condVar.notify_one();
         }
      }
};

int main() {
   FooBar fb1(1);
   FooBar fb2(2);
   FooBar fb0(0);
   FooBar fb10(10);

   std::vector<FooBar> foobars;
   foobars.push_back(fb1);
   foobars.push_back(fb2);
   foobars.push_back(fb0);
   foobars.push_back(fb10);

   for (auto & element : foobars) {
      std::cout << element.n << " ";
      std::thread t1(&FooBar::foo, &element);
      std::thread t2(&FooBar::bar, &element);
      t1.join();
      t2.join();
      std::cout << std::endl;
   }
   
   /* std::thread t1(&FooBar::foo, &fb2); */
   /* std::thread t2(&FooBar::bar, &fb2); */
   /* t1.join(); */
   /* t2.join(); */
}
