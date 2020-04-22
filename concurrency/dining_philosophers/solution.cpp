/* rendition of the dining philosophers problem.  Why they used forks instead of chopsticks I have */
/* no idea */
/* The philosophers' ids are numbered from 0 to 4 in a clockwise order. Implement the function void wantsToEat(philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork) where: */

/* philosopher is the id of the philosopher who wants to eat. */
/* pickLeftFork and pickRightFork are functions you can call to pick the corresponding forks of that philosopher. */
/* eat is a function you can call to let the philosopher eat once he has picked both forks. */
/* putLeftFork and putRightFork are functions you can call to put down the corresponding forks of that philosopher. */
/* The philosophers are assumed to be thinking as long as they are not asking to eat (the function is not being called with their number). */
/* Five threads, each representing a philosopher, will simultaneously use one object of your class to simulate the process. The function may be called for the same philosopher more than once, even before the last call ends. */

#include <thread>
#include <mutex>
#include <condition_variable>
#include <iostream>
#include <vector>

class DiningPhilosophers {
   private:
      const std::vector<int> forks {0, 1, 2, 3, 4};
      std::mutex mtx;
   public:
      DiningPhilosophers() {
         std::cout << "instance of dining philosphers created" << std::endl;

      }

      void wantsToEat(
         int philosopher,
         std::function<void()> pickLeftFork,
         std::function<void()> pickRightFork,
         std::function<void()> eat,
         std::function<void()> putLeftFork,
         std::function<void()> putRightFork) 
      {
         std::unique_lock<std::mutex> lck(mtx);
         const int leftFork = forks[(philosopher - 1) % 5];
         const int rightFork = forks[philosopher];
         std::cout << "philosopher " << philosopher << "left " << leftFork << "right " << rightFork << std::endl;
         lck.unlock();
      }
};

int main() {

   // Each thread represents a philosopher 
   // n represents how many times they eat
   // output[i] = [a, b, c] 
   // a is philo id
   // b is fork { 1: left, 2: right }
   // c is operation { 1: pick, 2: put, 3: eat }

   DiningPhilosophers dine;
   std::thread t0(
         &DiningPhilosophers::wantsToEat, 
         &dine, 
         0,
         [](){std::cout << "[0, 1, 1], ";},
         [](){std::cout << "[0, 2, 1], ";},
         [](){std::cout << "[0, 0, 3], ";},
         [](){std::cout << "[0, 1, 2], ";},
         [](){std::cout << "[0, 2, 2], ";}
         );

   std::thread t1(
         &DiningPhilosophers::wantsToEat, 
         &dine, 
         1,
         [](){std::cout << "[1, 1, 1], ";},
         [](){std::cout << "[1, 2, 1], ";},
         [](){std::cout << "[1, 0, 3], ";},
         [](){std::cout << "[1, 1, 2], ";},
         [](){std::cout << "[1, 2, 2], ";}
         );

   std::thread t2(
         &DiningPhilosophers::wantsToEat, 
         &dine, 
         2,
         [](){std::cout << "[2, 1, 1], ";},
         [](){std::cout << "[2, 2, 1], ";},
         [](){std::cout << "[2, 0, 3], ";},
         [](){std::cout << "[2, 1, 2], ";},
         [](){std::cout << "[2, 2, 2], ";}
         );

   std::thread t3(
         &DiningPhilosophers::wantsToEat, 
         &dine, 
         3,
         [](){std::cout << "[3, 1, 1], ";},
         [](){std::cout << "[3, 2, 1], ";},
         [](){std::cout << "[3, 0, 3], ";},
         [](){std::cout << "[3, 1, 2], ";},
         [](){std::cout << "[3, 2, 2], ";}
         );

   std::thread t4(
         &DiningPhilosophers::wantsToEat, 
         &dine, 
         4,
         [](){std::cout << "[4, 1, 1], ";},
         [](){std::cout << "[4, 2, 1], ";},
         [](){std::cout << "[4, 0, 3], ";},
         [](){std::cout << "[4, 1, 2], ";},
         [](){std::cout << "[4, 2, 2], ";}
         );

   t0.join();
   t1.join();
   t2.join();
   t3.join();
   t4.join();
   std::cout << std::endl;
}
