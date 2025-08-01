#ifndef __HELLO_WORLD_H__
#define __HELLO_WORLD_H__
#include <iostream>
class HelloWorld {
  public:
    HelloWorld();
    ~HelloWorld();
    void print();

  private:
    std::string str;

};
#endif
