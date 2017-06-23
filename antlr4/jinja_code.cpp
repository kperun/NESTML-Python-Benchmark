#include "iostream"
#include <math.h>


int main(){
   std::cout << "Starting computation test_calculation" << std::endl;
   std::cout << "Declare variables..." << std::endl;
   
   std::cout << "Declare a with pow(10,2)" << std::endl;
   int a = (int)pow(10,2);
   
   std::cout << "Declare b with 22" << std::endl;
   int b = (int)22;
   
   std::cout << "Declare c with 33" << std::endl;
   int c = (int)33;
   
   std::cout << "Start computation..." << std::endl;
   
   std::cout << "Compute a=a*2" << std::endl;
   a = a*2;
   std::cout << "Compute b=b+a/10" << std::endl;
   b = b+a/10;
   std::cout << "Compute c=a+b+c" << std::endl;
   c = a+b+c;
   std::cout << "The results are:" << std::endl;
   
   std::cout << "a=" << a << std::endl;
   
   std::cout << "b=" << b << std::endl;
   
   std::cout << "c=" << c << std::endl;
   
   return 0;
}