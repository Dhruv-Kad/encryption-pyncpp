#include <fstream>
#include <iostream>
#include <string>

// C++ bruteforcer to test python
int main() {
  std::ifstream file;
  file.open("blackout");
  std::string line;
  while (std::getline(file, line)) {
    std::cout << line << '\n';
  }
  file.close();
}
