#include <iostream>
#include "HelloWorld.h"

HelloWorld::HelloWorld(){
}

HelloWorld::~HelloWorld(){
}

void HelloWorld::print(){
  str = "Hello, world!";
  std::cout << str << std::endl;

}
