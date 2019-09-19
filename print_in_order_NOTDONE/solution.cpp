#import <thread>
#import <iostream>
#import <vector>

class Foo {
  public:
    Foo() {

    }

    void first(std::function<void()> printFirst) {

      // printFirst() outputs "first". Do not change or remove this line.
      printFirst();
    }

    void second(std::function<void()> printSecond) {

      // printSecond() outputs "second". Do not change or remove this line.
      printSecond();
    }

    void third(std::function<void()> printThird) {

      // printThird() outputs "third". Do not change or remove this line.
      printThird();
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
  std::thread t1(fool.first());
}
